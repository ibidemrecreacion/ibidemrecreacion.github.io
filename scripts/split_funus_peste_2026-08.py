#!/usr/bin/env python3
"""
split_funus_peste_2026-08.py

Corrige un error de catalogación: el 8 y el 29 de agosto de 2020 se
hicieron DOS recreaciones de "Fvnvs en tiempos de peste" en la necrópolis
de Carmona (no una con dos fechas + un "Fvnvs immaturvm" aparte el 29,
como constaba hasta ahora).

1) La actividad existente (id con fecha "8 y 29 de agosto de 2020") se
   queda solo con el 8 de agosto.
2) Se crea una nueva actividad "Fvnvs en tiempos de peste" el 29 de
   agosto de 2020, con la misma ubicación/etiquetas/formato.
3) Se elimina la actividad "Fvnvs immaturvm" del 29 de agosto de 2020
   (fasti + su álbum de imagina), que no debió existir como tal.
4) Se renumeran fasti e imagina cronológicamente (ids 1..N, siempre
   coincidiendo el id del álbum con el de su actividad), igual que en la
   reorganización anterior, y se crea un álbum placeholder para la
   actividad nueva.

Uso: python3 split_funus_peste_2026-08.py
"""

import json
import os
import re
from urllib.parse import quote

script_dir = os.path.dirname(os.path.abspath(__file__))
datos_path = os.path.join(script_dir, '..', 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

# ── 1) Localizar la actividad combinada y el Fvnvs immaturvm a eliminar ──
combined = next((f for f in data['fasti']
                  if f['title'] == 'Fvnvs en tiempos de peste'
                  and f['date'] == '8 y 29 de agosto de 2020'), None)
if combined is None:
    raise SystemExit('ERROR: no se encontró "Fvnvs en tiempos de peste" (8 y 29 de agosto de 2020).')

wrong_immaturvm = next((f for f in data['fasti']
                         if f['title'] == 'Fvnvs immaturvm'
                         and f['date'] == '29 de agosto de 2020'
                         and f['location']['locality'].startswith('Carmona')), None)
if wrong_immaturvm is None:
    raise SystemExit('ERROR: no se encontró el "Fvnvs immaturvm" del 29 de agosto de 2020 en Carmona.')

wrong_id = wrong_immaturvm['id']

# ── 2) La actividad combinada pasa a ser solo la del 8 de agosto ────────
combined['date'] = '8 de agosto de 2020'

# ── 3) Nueva actividad: Fvnvs en tiempos de peste, 29 de agosto ─────────
NEW_TEMP_ID = 100000
new_activity = {
    'id': NEW_TEMP_ID,
    'title': 'Fvnvs en tiempos de peste',
    'date': '29 de agosto de 2020',
    'location': dict(combined['location']),
    'desc': combined['desc'],
    'tags': list(combined['tags']),
    'format': combined['format']
}
data['fasti'].append(new_activity)

# ── 4) Eliminar el Fvnvs immaturvm erróneo (fasti + imagina) ────────────
data['fasti'] = [f for f in data['fasti'] if f['id'] != wrong_id]
data['imagina'] = [a for a in data['imagina'] if a['id'] != wrong_id]

# ── 5) Renumeración cronológica (misma lógica que reorg_fasti_imagina) ──
MONTHS = {
    'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
    'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10,
    'noviembre': 11, 'diciembre': 12
}

def parse_date_key(date_str):
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
        return (0, 0, 1)
    if month is None:
        month = 1
    if day is None:
        day = 1
    return (year, month, day)

fasti_sorted = sorted(data['fasti'], key=lambda f: (parse_date_key(f['date']), f['id']))
id_map = {}
for new_id, act in enumerate(fasti_sorted, start=1):
    id_map[act['id']] = new_id
for act in fasti_sorted:
    act['id'] = id_map[act['id']]
data['fasti'] = fasti_sorted

for alb in data['imagina']:
    old_id = alb['id']
    if old_id not in id_map:
        raise SystemExit(f'ERROR: álbum imagina id={old_id} no corresponde a ninguna actividad de fasti.')
    new_id = id_map[old_id]
    alb['id'] = new_id
    fasti_match = next(f for f in data['fasti'] if f['id'] == new_id)
    alb['eventTitle'] = fasti_match['title']
    alb['date'] = fasti_match['date']
    alb['location'] = fasti_match['location']

# ── 6) Placeholder para la actividad nueva (única sin álbum) ────────────
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
        "images": [{"src": PLACEHOLDER_URI, "caption": PLACEHOLDER_CAPTION}]
    })
    created += 1

data['imagina'] = sorted(data['imagina'], key=lambda a: a['id'])

# ── Guardar ───────────────────────────────────────────────────────────
with open(datos_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# ── Validación ────────────────────────────────────────────────────────
with open(datos_path, encoding='utf-8') as f:
    reloaded = json.load(f)

fasti_ids = [f['id'] for f in reloaded['fasti']]
imagina_ids = [a['id'] for a in reloaded['imagina']]
assert len(fasti_ids) == len(set(fasti_ids)), 'IDs duplicados en fasti!'
assert len(imagina_ids) == len(set(imagina_ids)), 'IDs duplicados en imagina!'
assert set(fasti_ids) == set(imagina_ids), 'fasti e imagina no coinciden en ids!'
assert fasti_ids == sorted(fasti_ids) == list(range(1, len(fasti_ids) + 1)), 'ids de fasti no son 1..N consecutivos y ordenados!'
keys = [parse_date_key(f['date']) for f in reloaded['fasti']]
assert keys == sorted(keys), 'fasti no quedó en orden cronológico!'

peste = [f for f in reloaded['fasti'] if f['title'] == 'Fvnvs en tiempos de peste']
assert len(peste) == 2, 'Deberían quedar exactamente 2 actividades "Fvnvs en tiempos de peste": ' + str(peste)
assert {p['date'] for p in peste} == {'8 de agosto de 2020', '29 de agosto de 2020'}
assert not any(f['title'] == 'Fvnvs immaturvm' and f['date'] == '29 de agosto de 2020'
               and f['location']['locality'].startswith('Carmona') for f in reloaded['fasti']), \
    'El Fvnvs immaturvm erróneo del 29 de agosto sigue presente'

print('OK — %d actividades en fasti, %d álbumes en imagina.' % (len(fasti_ids), len(imagina_ids)))
print('Álbumes placeholder nuevos creados:', created)
print()
print('Familia "Fvnvs en tiempos de peste" final:')
for p in sorted(peste, key=lambda x: x['id']):
    print('  id', p['id'], '|', p['date'])
