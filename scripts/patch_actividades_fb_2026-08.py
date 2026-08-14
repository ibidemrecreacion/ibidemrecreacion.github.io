#!/usr/bin/env python3
"""
patch_actividades_fb_2026-08.py
Ejecutar DESPUÉS de add_actividades_fb_2026-08.py.

Con el texto completo del recopilatorio ya disponible, se enriquecen las
descripciones de varias actividades y se resuelve la fecha exacta de
Nuptiae Constantiniana (id 53), que quedó como provisional.

Deducción de la fecha de Nuptiae Constantiniana:
El post "La velatio de la novia" (1 mayo 2016) dice que la actividad se
realizó "este pasado Domingo". El 1 de mayo de 2016 fue domingo, luego
"el pasado domingo" es el 24 de abril de 2016 (también domingo). Coincide
con el rango del Natale di Roma 2016 (21-24 abril). Fecha confirmada:
24 de abril de 2016.

Corrección adicional en id 61 (Vinieron de donde nace el sol): el rodaje
se realizó en el Parque Neolítico de la Draga (Banyoles, Girona) y en
Muel (Zaragoza), no en Alicante -- Alicante es donde se ubica el
santuario del Pla de Petracos que retrata el documental, pero no el lugar
de grabación.

Uso: colocar en scripts/ en la raíz del repo y ejecutar:
    python3 scripts/patch_actividades_fb_2026-08.py
"""

import json
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
datos_path = os.path.join(repo_root, 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

by_id = {e['id']: e for e in data['fasti']}

REQUIRED_IDS = [46, 47, 49, 53, 61]
missing = [i for i in REQUIRED_IDS if i not in by_id]
if missing:
    print(f"  ERROR: faltan los ids {missing} en fasti. "
          f"¿Has ejecutado antes add_actividades_fb_2026-08.py?")
    sys.exit(1)

PATCHES = {
    46: {
        "desc": "Taller de creación de adornos personales en marfil, hueso, nácar y carey "
                "(peines, agujas, alfileres, collares y brazaletes) usados por la aristocracia "
                "de las villae romanas entre los siglos IV y VII, con la asociación de mujeres "
                "Dominga Valdecañas.",
    },
    47: {
        "desc": "Taller de reconstrucción de los elementos decorativos textiles de las túnicas "
                "del Bajo Imperio: clavi, orbiculi y tabulae en lino y lana, con su evolución "
                "posterior hacia motivos vegetales polícromos de influencia sasánida.",
    },
    49: {
        "desc": "Recreación teatralizada del culto a los antepasados y las imagines maiorum, "
                "con un coro de manes inspirado en un fragmento de Lucano.",
    },
    53: {
        "date": "24 de abril de 2016",
        "desc": "Recreación del ritual matrimonial cristiano bajo el dominio constantiniano "
                "-- la velatio con el flammeum, la pronuba y la bendición sacerdotal en "
                "sustitución del auspicio pagano -- presentada en el Circo Máximo con motivo "
                "del Natale di Roma.",
    },
    61: {
        "location": {"locality": "Banyoles (Girona) y Muel (Zaragoza)",
                     "place": "Parque Neolítico de la Draga — rodaje para el MARQ"},
        "desc": "Participación en el rodaje del audiovisual del MARQ sobre el santuario "
                "neolítico del Pla de Petracos (Alicante), con dirección artística de José "
                "Montesinos Moreno y dirección de Jorge Molina Lamothe.",
    },
}

for eid, fields in PATCHES.items():
    by_id[eid].update(fields)

# --- Validación round-trip ---
serialized = json.dumps(data, ensure_ascii=False, indent=2)
reparsed = json.loads(serialized)
assert reparsed == data, "El JSON no sobrevive al round-trip"

# --- Comprobación de presencia de los cambios clave ---
assert '"date": "24 de abril de 2016"' in serialized
assert "Banyoles" in serialized

with open(datos_path, 'w', encoding='utf-8') as f:
    f.write(serialized + '\n')

print(f"  \u2713 {len(PATCHES)} actividades enriquecidas (ids {sorted(PATCHES)})")
print("  \u2713 Fecha de Nuptiae Constantiniana confirmada: 24 de abril de 2016")
print("  \u2713 Round-trip JSON validado")
print("  Recuerda ejecutar generate_og_pages.py o dejar que lo haga el Action tras el push.")
