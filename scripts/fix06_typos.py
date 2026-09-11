#!/usr/bin/env python3
"""
fix06_typos.py
Corrige erratas puntuales detectadas en la auditoría:
  - "Fuente Álaml" -> "Fuente Álamo"  (fasti/imagina id 79)
  - "Fvnvs immatvrvm" -> "Fvnvs immaturvm"  (id 79, consistencia con id 34/44/57/69)
  - "Kalenda en Cordvba" -> "Kalendas in Cordvba"  (imagina id 38)
  - "Calendas in Cordvba" -> "Kalendas in Cordvba"  (imagina id 62)
  - Espacio literal en el nombre de archivo de imagina id 63 -> %20 explícito
"""
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
datos_path = os.path.join(script_dir, '..', 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

fixes = []

def fix_fasti_imagina(id_, field_path, old, new):
    for coll_name in ('fasti', 'imagina'):
        for item in data[coll_name]:
            if item['id'] == id_:
                obj = item
                *path, last = field_path
                for p in path:
                    obj = obj[p]
                if obj.get(last) == old:
                    obj[last] = new
                    fixes.append(f"{coll_name}[{id_}].{'.'.join(field_path)}: {old!r} -> {new!r}")

fix_fasti_imagina(79, ['location', 'place'], 'Villa romana de Fuente Álaml', 'Villa romana de Fuente Álamo')

for f in data['fasti']:
    if f['id'] == 79 and f['title'] == 'Fvnvs immatvrvm':
        f['title'] = 'Fvnvs immaturvm'
        fixes.append("fasti[79].title: 'Fvnvs immatvrvm' -> 'Fvnvs immaturvm'")
for a in data['imagina']:
    if a['id'] == 79 and a['eventTitle'] == 'Fvnvs immatvrvm':
        a['eventTitle'] = 'Fvnvs immaturvm'
        fixes.append("imagina[79].eventTitle: 'Fvnvs immatvrvm' -> 'Fvnvs immaturvm'")

for a in data['imagina']:
    if a['id'] == 38 and a['location'].get('place') == 'Kalenda en Cordvba':
        a['location']['place'] = 'Kalendas in Cordvba'
        fixes.append("imagina[38].location.place: 'Kalenda en Cordvba' -> 'Kalendas in Cordvba'")
    if a['id'] == 62 and a['location'].get('place') == 'Calendas in Cordvba':
        a['location']['place'] = 'Kalendas in Cordvba'
        fixes.append("imagina[62].location.place: 'Calendas in Cordvba' -> 'Kalendas in Cordvba'")

for a in data['imagina']:
    if a['id'] == 63:
        old = "https://cdn.jsdelivr.net/gh/ibidemrecreacion/ibidemrecreacion.github.io@main/assets/img/Nvptiae_in_vicvs/Nvptiae_in _vicvs_portada.webp"
        new = "https://cdn.jsdelivr.net/gh/ibidemrecreacion/ibidemrecreacion.github.io@main/assets/img/Nvptiae_in_vicvs/Nvptiae_in%20_vicvs_portada.webp"
        if a.get('coverImage') == old:
            a['coverImage'] = new
            fixes.append("imagina[63].coverImage: espacio literal -> %20 explícito")

assert len(fixes) == 7, f"Se esperaban 7 correcciones, se aplicaron {len(fixes)}:\n" + "\n".join(fixes)

with open(datos_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"  ✓  {len(fixes)} erratas corregidas:")
for fx in fixes:
    print("    -", fx)
