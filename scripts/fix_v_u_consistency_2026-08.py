#!/usr/bin/env python3
"""
fix_v_u_consistency_2026-08.py

Unifica a la grafía epigráfica clásica (V en vez de U) los títulos de
actividades que estaban mezclando ambas formas para el mismo nombre:

- "Nuptiae Constantiniana"                         -> "Nvptiae Constantiniana"
- "Nuptiae in Emerita"                              -> "Nvptiae in Emerita"
- "Nuptiae. El ritual del matrimonio en la Roma pagana" -> "Nvptiae. El ritual del matrimonio en la Roma pagana"
- "Convivium" (x2)                                  -> "Convivivm"

El resto de apariciones de cada familia ya usaban V ("Nvptiae in vicvs" x4,
"Convivivm, protocolo y gastronomía en Roma"), así que esto las deja a
todas coherentes entre sí.

Actualiza tanto fasti.title como imagina.eventTitle (mismo id), que ya
estaban sincronizados antes de este cambio.

Uso: python3 fix_v_u_consistency_2026-08.py
"""

import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
datos_path = os.path.join(script_dir, '..', 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

RENAMES = {
    'Nuptiae Constantiniana': 'Nvptiae Constantiniana',
    'Nuptiae in Emerita': 'Nvptiae in Emerita',
    'Nuptiae. El ritual del matrimonio en la Roma pagana': 'Nvptiae. El ritual del matrimonio en la Roma pagana',
    'Convivium': 'Convivivm',
}

changed_ids = []
for act in data['fasti']:
    if act['title'] in RENAMES:
        old = act['title']
        act['title'] = RENAMES[old]
        changed_ids.append(act['id'])

for alb in data['imagina']:
    if alb['eventTitle'] in RENAMES:
        alb['eventTitle'] = RENAMES[alb['eventTitle']]

with open(datos_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# ── Validación ──────────────────────────────────────────────────────────
with open(datos_path, encoding='utf-8') as f:
    reloaded = json.load(f)

fasti_by_id = {f['id']: f for f in reloaded['fasti']}
mismatches = [a['id'] for a in reloaded['imagina']
              if fasti_by_id.get(a['id']) and fasti_by_id[a['id']]['title'] != a['eventTitle']]
assert not mismatches, 'Desincronía fasti/imagina tras el cambio: ' + str(mismatches)

for old in RENAMES:
    assert not any(f['title'] == old for f in reloaded['fasti']), 'Aún queda "' + old + '" sin renombrar'

nvptiae_titles = {f['title'] for f in reloaded['fasti'] if f['title'].lower().startswith('nvptiae') or f['title'].lower().startswith('nuptiae')}
convivium_titles = {f['title'] for f in reloaded['fasti'] if 'onviv' in f['title'].lower()[:9]}
assert all(t.startswith('Nvptiae') for t in nvptiae_titles), nvptiae_titles
assert all(t.startswith('Convivivm') for t in convivium_titles), convivium_titles

print('OK — %d actividades renombradas (fasti + imagina sincronizados):' % len(changed_ids))
for i in changed_ids:
    print('  id', i, '->', fasti_by_id[i]['title'])
print()
print('Familia Nvptiae final:', sorted(nvptiae_titles))
print('Familia Convivivm final:', sorted(convivium_titles))
