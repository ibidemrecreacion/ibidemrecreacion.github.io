#!/usr/bin/env python3
"""
fix17_actividades_faltantes.py
Añade dos actividades que faltaban en fasti/imagina:
  - Sit tibi terra levis, 27 sept. 2014, Fuente Álamo (misma obra ya documentada)
  - El juicio de Paris, 11 jun. 2016, Mérida, dentro del festival Emerita
    Ludica (mismo día que Nvptiae in Emerita, id 23, a la que se retro-
    enlaza también con ese festival).
"""
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
datos_path = os.path.join(script_dir, '..', 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

PLACEHOLDER_URI = "https://cdn.jsdelivr.net/gh/ibidemrecreacion/ibidemrecreacion.github.io@main/assets/img/General/opus_in_fieri.svg"
PLACEHOLDER_CAPTION = "Estamos trabajando en incorporar el reportaje gráfico de esta actividad."

fasti_ids = {f['id'] for f in data['fasti']}
imagina_ids = {a['id'] for a in data['imagina']}
assert fasti_ids == imagina_ids
next_id = max(fasti_ids) + 1  # 80

# --- 1) Sit tibi terra levis, Fuente Álamo, 27 sept 2014 ---
id_sit_tibi = next_id
data['fasti'].append({
    "id": id_sit_tibi,
    "title": "Sit tibi terra levis",
    "date": "27 de septiembre de 2014",
    "location": {"locality": "Puente Genil (Córdoba)", "place": "Villa romana de Fuente Álamo"},
    "desc": "Recreación teatralizada del culto a los antepasados y las imagines maiorum, con un coro de manes inspirado en un fragmento de Lucano.",
    "tags": ["Funerario"],
    "format": "Rito escenificado",
    "festivalId": None,
    "collaboratorIds": []
})
data['imagina'].append({
    "id": id_sit_tibi,
    "eventTitle": "Sit tibi terra levis",
    "date": "27 de septiembre de 2014",
    "location": {"locality": "Puente Genil (Córdoba)", "place": "Villa romana de Fuente Álamo"},
    "coverImage": PLACEHOLDER_URI,
    "images": [{"src": PLACEHOLDER_URI, "caption": PLACEHOLDER_CAPTION}]
})
print(f"  ✓  fasti/imagina[{id_sit_tibi}] Sit tibi terra levis (Fuente Álamo, 27 sept 2014) añadido")

# --- 2) Festival Emerita Ludica (nuevo) ---
next_festival_id = max(f['id'] for f in data['festivales']) + 1  # 16
data['festivales'].append({"id": next_festival_id, "name": "Emerita Ludica"})
print(f"  ✓  festivales[{next_festival_id}] 'Emerita Ludica' creado")

# Retro-enlazamos Nvptiae in Emerita (id 23) al festival, ya que fue el mismo día
nvptiae_emerita = next((f for f in data['fasti'] if f['id'] == 23), None)
assert nvptiae_emerita and nvptiae_emerita['title'] == 'Nvptiae in Emerita'
nvptiae_emerita['festivalId'] = next_festival_id
print("  ✓  fasti[23] 'Nvptiae in Emerita' enlazado a Emerita Ludica")

# --- 3) El juicio de Paris, Mérida, 11 jun 2016 (mismo día, festival Emerita Ludica) ---
id_juicio_paris = next_id + 1
data['fasti'].append({
    "id": id_juicio_paris,
    "title": "El juicio de Paris",
    "date": "11 de junio de 2016",
    "location": {"locality": "Mérida (Badajoz)", "place": ""},
    "desc": "Conferencia recreada sobre el mito del Juicio de Paris y su representación en los mosaicos tardorromanos, dentro del festival Emerita Ludica.",
    "tags": ["Vida cotidiana"],
    "format": "Conferencia recreada",
    "festivalId": next_festival_id,
    "collaboratorIds": []
})
data['imagina'].append({
    "id": id_juicio_paris,
    "eventTitle": "El juicio de Paris",
    "date": "11 de junio de 2016",
    "location": {"locality": "Mérida (Badajoz)", "place": ""},
    "coverImage": PLACEHOLDER_URI,
    "images": [{"src": PLACEHOLDER_URI, "caption": PLACEHOLDER_CAPTION}]
})
print(f"  ✓  fasti/imagina[{id_juicio_paris}] El juicio de Paris (Mérida, 11 jun 2016) añadido")

with open(datos_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"  ✓  fasti/imagina ahora tienen {len(data['fasti'])} entradas cada uno")
