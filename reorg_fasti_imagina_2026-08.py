#!/usr/bin/env python3
"""
reorg_fasti_imagina_2026-08.py

1) Añade una nueva actividad a fasti: "Fvnvs immaturvm" en la necrópolis
   de Carmona (Sevilla), 29 de agosto de 2020.

2) Renumera TODOS los ids de fasti e imagina en orden cronológico
   ascendente (del más antiguo al más reciente). El id de cada álbum de
   imagina se mantiene igual al id de la actividad de fasti a la que
   corresponde (convención ya usada por el frontend: PageActivityDetail /
   attachCover enlazan por igualdad de id).

3) Crea, para cada actividad de fasti que no tenga aún álbum de imagina,
   una galería placeholder con una única imagen (SVG embebido, sin
   depender de ningún archivo externo) y el caption "Estamos trabajando
   en incorporar el reportaje gráfico de esta actividad.", de forma que
   sea Ibidem quien vaya sustituyendo esa imagen y caption editando
   datos.json directamente, sin tener que pedir el cambio de código.

Uso: python3 reorg_fasti_imagina_2026-08.py
"""

import json
import os
import re
from urllib.parse import quote

script_dir = os.path.dirname(os.path.abspath(__file__))
datos_path = os.path.join(script_dir, '..', 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

# ── 0) Nueva actividad: Fvnvs immaturvm en Carmona ─────────────────────────
NEW_TEMP_ID = 100000  # id provisional único, se sustituye al renumerar
new_activity = {
    "id": NEW_TEMP_ID,
    "title": "Fvnvs immaturvm",
    "date": "29 de agosto de 2020",
    "location": {
        "locality": "Carmona (Sevilla)",
        "place": "Necrópolis"
    },
    "desc": "Recreación de los ritos fúnebres (funus) de un niño en una familia patricia de la Antigua Roma, en la necrópolis de Carmona.",
    "tags": ["Funerario"],
    "format": "Rito escenificado"
}
data['fasti'].append(new_activity)

# ── 1) Parseo de fechas en español (réplica de parseDate del frontend) ────
MONTHS = {
    'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
    'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10,
    'noviembre': 11, 'diciembre': 12
}

def parse_date_key(date_str):
    """Devuelve (year, month, day) para ordenar cronológicamente.
    Réplica del comportamiento de parseDate() en index.html: recorre
    todos los tokens y se queda con el último día/mes/año válido
    encontrado, para ser coherente con rangos tipo '19 al 21 de...' o
    '8 y 29 de agosto de...'."""
    if not date_str:
        return (0, 0, 1)
    s = date_str.lower().replace('de ', '').replace(',', '')
    parts = re.split(r'[\s\u2013\u2014-]+', s.strip())
    month, day, year = None, None, None
    for p in parts:
        p = p.strip('.')
        if not p:
            continue
        if p in MONTHS:
            month = MONTHS[p]
        elif p.isdigit() and int(p) > 31:
            year = int(p)
        elif p.isdigit():
            day = int(p)
    if year is None:
        # fecha totalmente irreconocible -> se manda al principio (como
        # new Date(0) en JS), no debería darse tras las correcciones previas
        return (0, 0, 1)
    if month is None:
        month = 1
    if day is None:
        day = 1
    return (year, month, day)

# ── 2) Ordenar fasti cronológicamente y construir el mapeo de ids ─────────
fasti_sorted = sorted(
    data['fasti'],
    key=lambda f: (parse_date_key(f['date']), f['id'])
)

id_map = {}
for new_id, act in enumerate(fasti_sorted, start=1):
    id_map[act['id']] = new_id

for act in fasti_sorted:
    act['id'] = id_map[act['id']]

data['fasti'] = fasti_sorted

# ── 3) Remapear ids de imagina existentes y sincronizar sus datos ─────────
for alb in data['imagina']:
    old_id = alb['id']
    if old_id not in id_map:
        raise SystemExit(f"ERROR: álbum imagina id={old_id} no corresponde a ninguna actividad de fasti.")
    new_id = id_map[old_id]
    alb['id'] = new_id
    fasti_match = next(f for f in data['fasti'] if f['id'] == new_id)
    alb['eventTitle'] = fasti_match['title']
    alb['date'] = fasti_match['date']
    alb['location'] = fasti_match['location']

# ── 4) Placeholder SVG "obra en curso" para actividades sin galería ───────
PLACEHOLDER_SVG = """<svg xmlns='http://www.w3.org/2000/svg' width='800' height='600' viewBox='0 0 800 600'>
<rect width='800' height='600' fill='#F5EFE3'/>
<rect x='24' y='24' width='752' height='552' fill='none' stroke='#9A2A2A' stroke-width='2'/>
<text x='400' y='265' font-family='Georgia, Cambria, serif' font-size='42' fill='#9A2A2A' text-anchor='middle' letter-spacing='6'>OPVS IN FIERI</text>
<text x='400' y='305' font-family='Georgia, Cambria, serif' font-style='italic' font-size='18' fill='#7A7A52' text-anchor='middle'>(obra en curso)</text>
<line x1='330' y1='330' x2='470' y2='330' stroke='#7A7A52' stroke-width='1'/>
<text x='400' y='372' font-family='Georgia, Cambria, serif' font-size='17' fill='#2D2D2D' text-anchor='middle'>Estamos trabajando en incorporar</text>
<text x='400' y='398' font-family='Georgia, Cambria, serif' font-size='17' fill='#2D2D2D' text-anchor='middle'>el reportaje gráfico de esta actividad</text>
</svg>"""
PLACEHOLDER_URI = "data:image/svg+xml," + quote(PLACEHOLDER_SVG, safe='')
PLACEHOLDER_CAPTION = "Estamos trabajando en incorporar el reportaje gráfico de esta actividad."

existing_imagina_ids = {a['id'] for a in data['imagina']}
created = 0
for act in data['fasti']:
    if act['id'] in existing_imagina_ids:
        continue
    data['imagina'].append({
        "id": act['id'],
        "eventTitle": act['title'],
        "date": act['date'],
        "location": act['location'],
        "coverImage": PLACEHOLDER_URI,
        "images": [
            {"src": PLACEHOLDER_URI, "caption": PLACEHOLDER_CAPTION}
        ]
    })
    created += 1

data['imagina'] = sorted(data['imagina'], key=lambda a: a['id'])

# ── 5) Guardar y validar ────────────────────────────────────────────────
with open(datos_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open(datos_path, encoding='utf-8') as f:
    reloaded = json.load(f)

fasti_ids = [f['id'] for f in reloaded['fasti']]
imagina_ids = [a['id'] for a in reloaded['imagina']]

assert len(fasti_ids) == len(set(fasti_ids)), "IDs duplicados en fasti!"
assert len(imagina_ids) == len(set(imagina_ids)), "IDs duplicados en imagina!"
assert set(fasti_ids) == set(imagina_ids), "fasti e imagina no tienen exactamente los mismos ids (no es una biyección)!"
assert fasti_ids == sorted(fasti_ids), "fasti no está ordenado por id!"
assert imagina_ids == sorted(imagina_ids), "imagina no está ordenado por id!"
assert fasti_ids == list(range(1, len(fasti_ids) + 1)), "Los ids de fasti no son consecutivos 1..N!"

# La actividad nueva debe existir con su fecha correcta
carmona = next(f for f in reloaded['fasti'] if f['title'] == 'Fvnvs immaturvm'
               and f['location']['locality'].startswith('Carmona'))
assert carmona['date'] == '29 de agosto de 2020'

# El orden cronológico debe ser monótono no decreciente
keys = [parse_date_key(f['date']) for f in reloaded['fasti']]
assert keys == sorted(keys), "El array de fasti no quedó en orden cronológico ascendente!"

print(f"OK — {len(fasti_ids)} actividades en fasti, {len(imagina_ids)} álbumes en imagina.")
print(f"  Nueva actividad añadida: Fvnvs immaturvm, Carmona, id={carmona['id']}")
print(f"  Álbumes placeholder creados: {created}")
print(f"  Ids: 1..{len(fasti_ids)} en ambos arrays, ordenados cronológicamente.")
