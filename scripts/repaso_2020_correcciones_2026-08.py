#!/usr/bin/env python3
"""
repaso_2020_correcciones_2026-08.py

A partir del repaso cronológico del usuario (documento hasta 2020, 42 hitos)
aplica:

1. Correcciones sobre entradas existentes:
   - id 50: renombrada "Las mujeres en la Prehistoria" (era la conferencia
     recreada; el enterramiento calcolítico es una actividad distinta, "El
     presente eterno"). Fecha 13/12/2015 se mantiene. Format -> Conferencia
     recreada.
   - id 58: misma actividad que "I Encuentro de Recreación histórica de
     Torreparedones"; fecha corregida a 09/10/2016 (antes 25/02/2017) y
     título actualizado.
   - id 6: nombre original "Los objetos que nos hablan de los vivos"
     (renombrada después "Objetos que cuentan historias"); se añade esta
     última como tag-alias de búsqueda, igual que Fraternitas Iurata/
     Adelfopoiesis.
   - id 22: fecha corregida a agosto de 2020 (rodaje); el dato de marzo de
     2021 era el estreno, que se traslada a la descripción.
   - id 1: sin cambios (ya estaba correctamente en Córdoba).
   - id 18/19: sin cambios (ambas actividades coexisten el 21/09/2019 en el
     Castra Legionis de ese año).

2. Nueve actividades nuevas (2014-2015), ids 69-77.

Uso:
    python3 repaso_2020_correcciones_2026-08.py
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATOS_PATH = os.path.join(SCRIPT_DIR, "..", "datos.json")

with open(DATOS_PATH, encoding="utf-8") as f:
    data = json.load(f)

fasti = data["fasti"]
by_id = {e["id"]: e for e in fasti}

# ─── 1. Correcciones ─────────────────────────────────────────────────────────

e50 = by_id[50]
e50["title"] = "Las mujeres en la Prehistoria"
e50["desc"] = "Conferencia recreada sobre el papel de la mujer en la Prehistoria, en el Museo Arqueológico de Sevilla."
e50["format"] = "Conferencia recreada"
assert e50["date"] == "13 de diciembre de 2015"

e58 = by_id[58]
e58["title"] = "I Encuentro de Recreación histórica de Torreparedones"
e58["date"] = "9 de octubre de 2016"
e58["desc"] = "Participación en el desfile de la Legio I Vernácula en el yacimiento íbero-romano de Torreparedones, en Baena (Córdoba)."

e6 = by_id[6]
e6["title"] = "Los objetos que nos hablan de los vivos"
if "Objetos que cuentan historias" not in e6["tags"]:
    e6["tags"].append("Objetos que cuentan historias")

e22 = by_id[22]
e22["date"] = "agosto de 2020"
e22["desc"] = "Rodaje de las escenas de dramatización del documental Al-Ándalus: el legado, de Canal de Historia, estrenado en marzo de 2021."

# ─── 2. Nuevas actividades (2014-2015) ──────────────────────────────────────
nuevas = [
    {
        "id": 69,
        "title": "Malaca romana",
        "date": "13 de septiembre de 2014",
        "location": {"locality": "Málaga", "place": ""},
        "desc": "Participación en el festival Malaca Romana junto a la Legio I Vernácula de Gilena.",
        "format": "Institucional",
        "tags": []
    },
    {
        "id": 70,
        "title": "Nvptiae in vicvs",
        "date": "20 de septiembre de 2014",
        "location": {"locality": "Puente Genil (Córdoba)", "place": "Villa romana de Fuente Álamo"},
        "desc": "Recreación de una boda según el ritual tradicional romano, estrenada en las jornadas Aspectos de la vida cotidiana en una villa romana de la Bética.",
        "format": "Rito escenificado",
        "tags": ["Mujer", "Vida cotidiana"]
    },
    {
        "id": 71,
        "title": "Itálica viva: indumentaria militar del Bajo Imperio",
        "date": "27 de septiembre de 2014",
        "location": {"locality": "Santiponce (Sevilla)", "place": "Itálica"},
        "desc": "Exhibición del vestuario de un militar romano del siglo IV d.C., junto a la Legio I Vernácula, y explicación sobre la indumentaria tardoantigua a cargo de José Montesinos Moreno y Carolina Bernabé Palos, dentro del festival Itálica Viva.",
        "format": "Conferencia recreada",
        "tags": ["Vida cotidiana"]
    },
    {
        "id": 72,
        "title": "Nupcias en la Antigüedad Tardía",
        "date": "14 de diciembre de 2014",
        "location": {"locality": "Córdoba", "place": "Teatro romano"},
        "desc": "Recreación de una boda según el ritual tradicional romano en el Teatro romano de Córdoba.",
        "format": "Rito escenificado",
        "tags": ["Mujer"]
    },
    {
        "id": 73,
        "title": "Visita al CEIP Virgen de Tíscar de Quesada",
        "date": "7 de junio de 2015",
        "location": {"locality": "Quesada (Jaén)", "place": "CEIP Virgen de Tíscar"},
        "desc": "Actividad de divulgación en el centro educativo, junto a la Legio I Vernácula de Gilena.",
        "format": "Institucional",
        "tags": []
    },
    {
        "id": 74,
        "title": "El presente eterno",
        "date": "11 de junio de 2015",
        "location": {"locality": "Gilena (Sevilla)", "place": "Yacimiento arqueológico El Negrón"},
        "desc": "Recreación del enterramiento calcolítico de la cueva artificial Antoniana I de Gilena, en el yacimiento arqueológico de El Negrón.",
        "format": "Rito escenificado",
        "tags": ["Prehistoria"]
    },
    {
        "id": 75,
        "title": "El mosaico y las Artes en el Bajo Imperio",
        "date": "19 de agosto de 2015",
        "location": {"locality": "Casariche (Sevilla)", "place": ""},
        "desc": "Conferencia recreada sobre el mosaico y las artes decorativas en el Bajo Imperio, junto a la Legio VII Gemina.",
        "format": "Conferencia recreada",
        "tags": ["Vida cotidiana"]
    },
    {
        "id": 76,
        "title": "La religión en el ámbito militar",
        "date": "7 de noviembre de 2015",
        "location": {"locality": "Santiponce (Sevilla)", "place": "Conjunto arqueológico de Itálica"},
        "desc": "Conferencia recreada sobre la religión en el ámbito militar romano, junto a la Legio I Vernácula, la Legio V Hispalense y Sexto Mario.",
        "format": "Conferencia recreada",
        "tags": ["Religión"]
    },
    {
        "id": 77,
        "title": "I Congreso de jóvenes investigadores de la Prehistoria en Andalucía",
        "date": "25 de noviembre de 2015",
        "location": {"locality": "", "place": ""},
        "desc": "Participación en el I Congreso de jóvenes investigadores de la Prehistoria en Andalucía.",
        "format": "Institucional",
        "tags": ["Prehistoria"]
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
