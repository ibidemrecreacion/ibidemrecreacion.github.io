#!/usr/bin/env python3
"""
add_castra_legionis_editions_2026-08.py

Añade el histórico completo de ediciones del festival Castra Legionis
(aportado por Ibidem) y rellena "festivalEdition" en cada actividad de
fasti que se celebró en Castra Legionis, deduciendo la edición a partir
del año de la fecha de la actividad.

Uso: python3 add_castra_legionis_editions_2026-08.py
"""

import json
import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
datos_path = os.path.join(script_dir, '..', 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

EDITIONS = [
    {'edition': 'I', 'year': 2012},
    {'edition': 'II', 'year': 2013},
    {'edition': 'III', 'year': 2014},
    {'edition': 'IV', 'year': 2015},
    {'edition': 'V', 'year': 2016},
    {'edition': 'VI', 'year': 2017},
    {'edition': 'Especial', 'year': 2019, 'note': 'Transición y enfoque en el ejército romano'},
    {'edition': 'VII', 'year': 2022, 'note': 'Reinicio y cambio a formato bienal'},
    {'edition': 'VIII', 'year': 2024, 'note': 'Temática "Origines: Desde Troya a Heraclea"'},
    {'edition': 'IX', 'year': 2026, 'note': 'Edición actual: "Odisea. Un relato mediterráneo"'},
]
YEAR_TO_EDITION = {e['year']: e['edition'] for e in EDITIONS}

castra = next(f for f in data['festivales'] if f['name'] == 'Castra Legionis')
castra['editions'] = EDITIONS

def year_of(date_str):
    m = re.search(r'(\d{4})', date_str or '')
    return int(m.group(1)) if m else None

updated = []
for act in data['fasti']:
    if act.get('festivalId') != castra['id']:
        continue
    year = year_of(act['date'])
    edition = YEAR_TO_EDITION.get(year)
    if edition and act.get('festivalEdition') != edition:
        act['festivalEdition'] = edition
        updated.append((act['id'], act['title'], year, edition))

with open(datos_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# ── Validación ────────────────────────────────────────────────────────
with open(datos_path, encoding='utf-8') as f:
    reloaded = json.load(f)

castra2 = next(f for f in reloaded['festivales'] if f['name'] == 'Castra Legionis')
assert len(castra2['editions']) == 10
for act in reloaded['fasti']:
    if act.get('festivalId') == castra2['id']:
        assert act.get('festivalEdition'), 'Actividad de Castra Legionis sin edición: id ' + str(act['id'])

print('OK — editions añadidas al festival Castra Legionis (%d ediciones).' % len(castra2['editions']))
print('Actividades actualizadas con festivalEdition:')
for u in updated:
    print('  id', u[0], '|', u[1], '|', u[2], '-> edición', u[3])
