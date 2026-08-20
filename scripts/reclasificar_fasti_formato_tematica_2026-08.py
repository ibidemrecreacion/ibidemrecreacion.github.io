#!/usr/bin/env python3
"""
reclasificar_fasti_formato_tematica_2026-08.py

1. Introduce un eje "format" (nuevo campo) independiente de "tags"
   (que pasa a contener solo temática) en cada entrada de fasti.
   Vocabulario cerrado:
     FORMATOS  = Rito escenificado, Conferencia recreada, Espectáculo,
                 Taller, Rodaje, Institucional
     TEMATICAS = Funerario, Mujer, Vida cotidiana, Religión, Al-Ándalus,
                 Prehistoria, Social, Lucha, Emperador
   El tag "Adelfopoiesis" en el id 19 se conserva como alias de búsqueda
   (no forma parte del vocabulario oficial de temática).

2. Añade dos actividades futuras:
   - id 67 "Convivivm, protocolo y gastronomia en Roma" (17-10-2026,
     Casa Árabe, Córdoba, festival Lux Historiae, organiza Sexto Mario)
   - id 68 "Sillicernivm o cómo comer con los muertos" (31-10-2026,
     Criptopórtico, Monturque, Munda Mortis XVIII edición)

Uso:
    python3 reclasificar_fasti_formato_tematica_2026-08.py
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATOS_PATH = os.path.join(SCRIPT_DIR, "..", "datos.json")

with open(DATOS_PATH, encoding="utf-8") as f:
    data = json.load(f)

fasti = data["fasti"]

# id -> (format, tematica_tags)
CLASIFICACION = {
    1:  ("Espectáculo", ["Vida cotidiana", "Social"]),
    2:  ("Conferencia recreada", ["Vida cotidiana", "Mujer"]),
    3:  ("Rito escenificado", ["Vida cotidiana", "Mujer"]),
    4:  ("Rito escenificado", ["Funerario"]),
    5:  ("Rito escenificado", ["Vida cotidiana", "Mujer"]),
    6:  ("Conferencia recreada", ["Vida cotidiana", "Mujer"]),
    7:  ("Rito escenificado", ["Mujer", "Vida cotidiana"]),
    8:  ("Conferencia recreada", ["Al-Ándalus", "Mujer", "Vida cotidiana"]),
    9:  ("Espectáculo", ["Social"]),
    10: ("Rodaje", ["Prehistoria"]),
    11: ("Espectáculo", ["Social", "Vida cotidiana"]),
    12: ("Espectáculo", ["Social"]),
    13: ("Conferencia recreada", ["Mujer", "Vida cotidiana"]),
    14: ("Rito escenificado", ["Funerario"]),
    15: ("Rito escenificado", ["Vida cotidiana", "Mujer"]),
    16: ("Espectáculo", ["Social"]),
    17: ("Rito escenificado", ["Mujer", "Vida cotidiana"]),
    18: ("Espectáculo", ["Social"]),
    19: ("Rito escenificado", ["Social", "Adelfopoiesis"]),
    20: ("Rodaje", []),
    21: ("Conferencia recreada", ["Funerario"]),
    22: ("Rodaje", ["Al-Ándalus"]),
    23: ("Espectáculo", ["Al-Ándalus"]),
    24: ("Rito escenificado", ["Vida cotidiana", "Mujer"]),
    25: ("Conferencia recreada", ["Religión"]),
    26: ("Rito escenificado", ["Funerario"]),
    27: ("Conferencia recreada", ["Religión"]),
    28: ("Conferencia recreada", ["Mujer", "Vida cotidiana"]),
    29: ("Conferencia recreada", ["Vida cotidiana", "Mujer"]),
    30: ("Rito escenificado", ["Religión"]),
    31: ("Rito escenificado", ["Vida cotidiana", "Mujer"]),
    32: ("Rito escenificado", ["Mujer", "Vida cotidiana"]),
    33: ("Conferencia recreada", ["Mujer", "Vida cotidiana"]),
    34: ("Conferencia recreada", ["Vida cotidiana", "Mujer"]),
    35: ("Conferencia recreada", ["Vida cotidiana", "Mujer"]),
    36: ("Espectáculo", ["Emperador"]),
    37: ("Espectáculo", ["Emperador"]),
    38: ("Rito escenificado", ["Funerario"]),
    39: ("Espectáculo", ["Emperador"]),
    40: ("Rito escenificado", ["Social"]),
    41: ("Rito escenificado", ["Social"]),
    42: ("Espectáculo", ["Lucha"]),
    43: ("Rito escenificado", ["Funerario"]),
    44: ("Rito escenificado", ["Funerario"]),
    45: ("Espectáculo", ["Lucha"]),
    46: ("Taller", ["Vida cotidiana"]),
    47: ("Taller", ["Vida cotidiana"]),
    48: ("Institucional", ["Vida cotidiana"]),
    49: ("Rito escenificado", ["Funerario"]),
    50: ("Rito escenificado", ["Prehistoria"]),
    51: ("Institucional", []),
    52: ("Institucional", []),
    53: ("Rito escenificado", ["Mujer", "Religión"]),
    54: ("Rito escenificado", ["Mujer"]),
    55: ("Rito escenificado", ["Vida cotidiana", "Mujer"]),
    56: ("Conferencia recreada", ["Vida cotidiana"]),
    57: ("Rito escenificado", ["Mujer"]),
    58: ("Institucional", []),
    59: ("Rito escenificado", ["Funerario"]),
    60: ("Institucional", []),
    61: ("Rodaje", ["Prehistoria"]),
    62: ("Institucional", []),
    63: ("Rito escenificado", ["Funerario"]),
    64: ("Rito escenificado", ["Funerario"]),
    65: ("Institucional", ["Religión"]),
    66: ("Rito escenificado", ["Vida cotidiana"]),
}

assert set(CLASIFICACION) == {e["id"] for e in fasti}, "Faltan ids por clasificar"

for ev in fasti:
    fmt, tem = CLASIFICACION[ev["id"]]
    ev["format"] = fmt
    ev["tags"] = tem

# ─── Nuevas actividades futuras ─────────────────────────────────────────────
nuevas = [
    {
        "id": 67,
        "title": "Convivivm, protocolo y gastronomia en Roma",
        "date": "17 de octubre de 2026",
        "location": {"locality": "Córdoba", "place": "Casa Árabe"},
        "desc": "Banquete recreado que explora el protocolo y la gastronomía de las clases aristocráticas romanas, dentro del festival Lux Historiae, organizado por Sexto Mario.",
        "format": "Espectáculo",
        "tags": ["Vida cotidiana", "Social"]
    },
    {
        "id": 68,
        "title": "Sillicernivm o cómo comer con los muertos",
        "date": "31 de octubre de 2026",
        "location": {"locality": "Monturque (Córdoba)", "place": "Criptopórtico"},
        "desc": "Recreación del sillicernium, el banquete funerario romano compartido junto a la tumba del difunto, dentro de Munda Mortis (XVIII edición).",
        "format": "Rito escenificado",
        "tags": ["Funerario"]
    },
]
fasti.extend(nuevas)

# ─── Validaciones ────────────────────────────────────────────────────────────
FORMATOS_VALIDOS = {"Rito escenificado", "Conferencia recreada", "Espectáculo",
                     "Taller", "Rodaje", "Institucional"}
for ev in fasti:
    assert ev["format"] in FORMATOS_VALIDOS, ev

ids = [e["id"] for e in fasti]
assert len(ids) == len(set(ids)), "IDs duplicados"

with open(DATOS_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open(DATOS_PATH, encoding="utf-8") as f:
    reloaded = json.load(f)
print("OK — fasti:", len(reloaded["fasti"]))
