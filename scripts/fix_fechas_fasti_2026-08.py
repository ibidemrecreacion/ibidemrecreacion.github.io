#!/usr/bin/env python3
"""
fix_fechas_fasti_2026-08.py
Corrige 3 discrepancias de fecha detectadas al cotejar el archivo de
Facebook con datos.json:
  - id 26 (Fvnvs, Monturque Ayuntamiento): 18 oct 2021 -> 30 oct 2021
  - id 24 (Dies lvstricvs, Fuente Álamo):   31 jul 2021 -> 30 jul 2021
  - id 21 (Fvnvs en tiempos de peste, Carmona): 8 y 9 ago 2020 -> 8 y 29 ago 2020

Uso: colocar en scripts/ en la raíz del repo y ejecutar:
    python3 scripts/fix_fechas_fasti_2026-08.py
"""

import json
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
datos_path = os.path.join(repo_root, 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

FIXES = {
    26: ("18 de octubre de 2021", "30 de octubre de 2021"),
    24: ("31 de julio de 2021", "30 de julio de 2021"),
    21: ("8 y 9 de agosto de 2020", "8 y 29 de agosto de 2020"),
}

applied = []
for evt in data.get('fasti', []):
    if evt['id'] in FIXES:
        old_expected, new_date = FIXES[evt['id']]
        if evt['date'] != old_expected:
            print(f"  AVISO: id {evt['id']} tiene fecha '{evt['date']}', "
                  f"se esperaba '{old_expected}'. Revisar manualmente.")
            continue
        evt['date'] = new_date
        applied.append(evt['id'])

missing = set(FIXES) - set(applied)
if missing:
    print(f"  AVISO: no se encontraron o no se pudieron corregir los ids {missing}")
    sys.exit(1)

# --- Validación round-trip ---
serialized = json.dumps(data, ensure_ascii=False, indent=2)
reparsed = json.loads(serialized)
assert reparsed == data, "El JSON no sobrevive al round-trip"

with open(datos_path, 'w', encoding='utf-8') as f:
    f.write(serialized + '\n')

print(f"  \u2713 Fechas corregidas para ids {sorted(applied)}")
print("  \u2713 Round-trip JSON validado")
print("  Recuerda ejecutar generate_og_pages.py o dejar que lo haga el Action tras el push.")
