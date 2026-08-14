#!/usr/bin/env python3
"""
add_actividades_fb_2026-08.py
Da de alta en fasti las actividades detectadas en el recopilatorio de
Facebook que faltaban en datos.json. IDs 46-61, no colisionan con los
existentes (1-45).

NOTA sobre id 53: en la ronda de organización previa se etiquetó por error
como "Fvnvs: Nuptiae Constantiniana". Es una boda, no un funeral, así que
aquí se corrige a "Nuptiae Constantiniana" para que normalizeTitle() no la
agrupe con la familia Fvnvs.

Uso: colocar en scripts/ en la raíz del repo y ejecutar:
    python3 scripts/add_actividades_fb_2026-08.py
"""

import json
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
datos_path = os.path.join(repo_root, 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

existing_ids = {e['id'] for e in data['fasti']}

NUEVAS = [
    {
        "id": 46,
        "title": "Eborarium",
        "date": "14 de marzo de 2014",
        "location": {"locality": "Puente Genil (Córdoba)", "place": "Villa romana de Fuente Álamo"},
        "desc": "Taller sobre la elaboración de adornos personales en marfil, hueso, nácar y carey del Bajo Imperio, con la asociación de mujeres Dominga Valdecañas.",
        "tags": ["Taller", "Vida cotidiana"]
    },
    {
        "id": 47,
        "title": "Taller de tejidos",
        "date": "10 de mayo de 2014",
        "location": {"locality": "Puente Genil (Córdoba)", "place": "Villa romana de Fuente Álamo"},
        "desc": "Taller de reconstrucción de los elementos decorativos textiles (clavi, orbiculi, tabulae) de las túnicas del Bajo Imperio.",
        "tags": ["Taller", "Vida cotidiana"]
    },
    {
        "id": 48,
        "title": "Vida cotidiana en las villas romanas de la Antigüedad Tardía",
        "date": "19 al 21 de septiembre de 2014",
        "location": {"locality": "Puente Genil (Córdoba)", "place": "Villa romana de Fuente Álamo"},
        "desc": "Jornadas de recreación centradas en la vida cotidiana en las villae romanas de la Antigüedad Tardía.",
        "tags": ["Vida cotidiana"]
    },
    {
        "id": 49,
        "title": "Sit tibi terra levis",
        "date": "18 de octubre de 2014",
        "location": {"locality": "Santiponce (Sevilla)", "place": "Itálica"},
        "desc": "Recreación del culto a los antepasados y las imagines maiorum en el yacimiento de Itálica.",
        "tags": ["Rito", "Funerario"]
    },
    {
        "id": 50,
        "title": "Enterramiento calcolítico de la cueva Antoniana I",
        "date": "13 de diciembre de 2015",
        "location": {"locality": "Sevilla", "place": "Museo Arqueológico"},
        "desc": "Recreación del enterramiento calcolítico de la cueva artificial Antoniana I de Gilena, dentro de la exposición «Las mujeres en la Prehistoria».",
        "tags": ["Prehistoria"]
    },
    {
        "id": 51,
        "title": "I Jornadas de recreacionismo histórico y museos",
        "date": "19 al 22 de mayo de 2016",
        "location": {"locality": "Sevilla", "place": "Museo Arqueológico (MAS)"},
        "desc": "Conferencia, mesa redonda y actividades de recreación con motivo del Día Internacional de los Museos.",
        "tags": ["Institucional"]
    },
    {
        "id": 52,
        "title": "Tarraco Viva 2016",
        "date": "27 al 29 de mayo de 2016",
        "location": {"locality": "Tarragona", "place": "Tarraco Viva"},
        "desc": "Participación con stand institucional junto a la Legio I Vernácula y la Legio VII Gémina, presentando el proyecto Consilium Baeticae.",
        "tags": ["Institucional"]
    },
    {
        "id": 53,
        "title": "Nuptiae Constantiniana",
        "date": "21 de abril de 2016",
        "location": {"locality": "Roma (Italia)", "place": "Circo Máximo — Natale di Roma"},
        "desc": "Recreación del ritual matrimonial cristiano bajo el dominio constantiniano, presentada con motivo del Natale di Roma. Fecha provisional dentro del programa (21-24 de abril).",
        "tags": ["Rito", "Mujer"]
    },
    {
        "id": 54,
        "title": "Nuptiae in Emerita",
        "date": "11 de junio de 2016",
        "location": {"locality": "Mérida (Badajoz)", "place": ""},
        "desc": "Recreación de una boda según el ritual tradicional romano en Mérida.",
        "tags": ["Rito", "Mujer"]
    },
    {
        "id": 55,
        "title": "Dies lvstricvs. Cómo nacer en Roma",
        "date": "15 de junio de 2016",
        "location": {"locality": "Mérida (Badajoz)", "place": ""},
        "desc": "Reconstrucción del parto de una patricia romana y sus implicaciones morales, religiosas y sociales.",
        "tags": ["Vida cotidiana", "Rito", "Mujer"]
    },
    {
        "id": 56,
        "title": "Indumentaria masculina del Bajo Imperio",
        "date": "30 de septiembre de 2016",
        "location": {"locality": "Cártama (Málaga)", "place": ""},
        "desc": "Recreación de indumentaria masculina del Bajo Imperio junto a la Legio VII Gemina: obispo, general, militar, posesor y sirviente.",
        "tags": ["Vida cotidiana"]
    },
    {
        "id": 57,
        "title": "Nuptiae. El ritual del matrimonio en la Roma pagana",
        "date": "3 de diciembre de 2016",
        "location": {"locality": "Antequera (Málaga)", "place": "Museo de Antequera"},
        "desc": "Recreación del ritual matrimonial romano pagano en el Museo de Antequera.",
        "tags": ["Rito", "Mujer"]
    },
    {
        "id": 58,
        "title": "Yacimiento íbero-romano de Torreparedones",
        "date": "25 de febrero de 2017",
        "location": {"locality": "Baena (Córdoba)", "place": "Torreparedones"},
        "desc": "Colaboración con la Legio I Vernácula, la Legio V Hispalense y Lusitania Romana en el yacimiento íbero-romano de Torreparedones.",
        "tags": ["Institucional"]
    },
    {
        "id": 59,
        "title": "Fvnvs: Los funerales de Acilia Plecusa",
        "date": "11 de marzo de 2017",
        "location": {"locality": "Antequera (Málaga)", "place": "Museo de Antequera"},
        "desc": "Recreación del funeral de una aristócrata de Singilia Barba, expuesta en el atrio de la casa con plañideras y las imagines maiorum, en el Museo de Antequera.",
        "tags": ["Rito", "Funerario"]
    },
    {
        "id": 60,
        "title": "II Jornadas Hispano-Visigodas de Cabra",
        "date": "21 al 22 de abril de 2017",
        "location": {"locality": "Cabra (Córdoba)", "place": ""},
        "desc": "Colaboración con Traditio Malacitana en las II Jornadas Hispano-Visigodas de Cabra.",
        "tags": ["Institucional"]
    },
    {
        "id": 61,
        "title": "Vinieron de donde nace el sol",
        "date": "2016",
        "location": {"locality": "Castell de Castells (Alicante)", "place": "Pla de Petracos / MARQ"},
        "desc": "Participación en el rodaje del documental del MARQ sobre el santuario neolítico del Pla de Petracos.",
        "tags": ["Prehistoria", "Rodaje"]
    },
]

conflicts = existing_ids & {e['id'] for e in NUEVAS}
if conflicts:
    print(f"  ERROR: los ids {conflicts} ya existen en fasti. Abortando.")
    sys.exit(1)

data['fasti'].extend(NUEVAS)

# --- Validación round-trip ---
serialized = json.dumps(data, ensure_ascii=False, indent=2)
reparsed = json.loads(serialized)
assert reparsed == data, "El JSON no sobrevive al round-trip"

# --- Comprobación: todos los títulos nuevos están presentes en el resultado ---
for e in NUEVAS:
    assert e['title'] in serialized, f"Falta el título '{e['title']}' tras la serialización"

with open(datos_path, 'w', encoding='utf-8') as f:
    f.write(serialized + '\n')

print(f"  \u2713 {len(NUEVAS)} actividades nuevas añadidas a fasti (ids {NUEVAS[0]['id']}-{NUEVAS[-1]['id']})")
print("  \u2713 Round-trip JSON validado")
print("  \u2713 Comprobación de presencia de títulos: OK")
print("  Recuerda ejecutar generate_og_pages.py o dejar que lo haga el Action tras el push.")
print("  Pendiente: confirmar fecha exacta de 'Nuptiae Constantiniana' (id 53) dentro del programa 21-24 abril 2016.")
