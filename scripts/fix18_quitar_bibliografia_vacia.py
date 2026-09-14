#!/usr/bin/env python3
"""
fix18_quitar_bibliografia_vacia.py
`art.bibliography && ...` en index.html trata un array vacío [] como
verdadero (JS), así que renderiza el bloque "Fontes (Bibliografía)" vacío.
Se elimina la clave por completo en los artículos donde no hay fuentes,
igual que en el resto de artículos Legado que nunca la tuvieron.
"""
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
datos_path = os.path.join(script_dir, '..', 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

removed = []
for art in data['tabularium']:
    if art.get('bibliography') == []:
        del art['bibliography']
        removed.append(art['id'])

assert removed == [9, 10, 11, 19, 20, 21, 22], f"Lista inesperada: {removed}"

with open(datos_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"  ✓  bibliography vacía eliminada en tabularium: {removed}")
