#!/usr/bin/env python3
"""
fix08_optimize_fallback_image.py
Sustituye las referencias a Pepe_Larario.jpg (2560x1920, 365 KB, sin optimizar)
por Pepe_Larario.webp (1920x1440, ~88 KB) en los usos de imagen "de escena"
(hero de portada, cabeceras de artículo). El og:image dedicado se gestiona
aparte en index.html / generate_og_pages.py (Pepe_Larario_og.jpg, 1200x630).

Requiere subir antes Pepe_Larario.webp y Pepe_Larario_og.jpg al repositorio
(assets/img/General/), entregados junto a este script.
"""
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
datos_path = os.path.join(script_dir, '..', 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

OLD = "https://cdn.jsdelivr.net/gh/ibidemrecreacion/ibidemrecreacion.github.io@main/assets/img/General/Pepe_Larario.jpg"
NEW = "https://cdn.jsdelivr.net/gh/ibidemrecreacion/ibidemrecreacion.github.io@main/assets/img/General/Pepe_Larario.webp"

count = 0

if data['general'].get('heroImageHome') == OLD:
    data['general']['heroImageHome'] = NEW
    count += 1

for art in data['tabularium']:
    if art.get('img') == OLD:
        art['img'] = NEW
        count += 1
    for sec in art.get('sections', []):
        img = sec.get('image')
        if isinstance(img, dict) and img.get('src') == OLD:
            img['src'] = NEW
            count += 1
        for sub in sec.get('subsections', []):
            simg = sub.get('image')
            if isinstance(simg, dict) and simg.get('src') == OLD:
                simg['src'] = NEW
                count += 1

assert count == 11, f"Se esperaban 11 sustituciones, se aplicaron {count}"

with open(datos_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"  ✓  {count} referencias actualizadas a Pepe_Larario.webp")
