#!/usr/bin/env python3
"""
fix03_dedupe_placeholder_svg.py
Sustituye las 72 copias idénticas del placeholder SVG "OPVS IN FIERI"
(inline data-URI, ~1.5 KB cada una) por una única referencia al archivo
real alojado en el CDN: assets/img/General/opus_in_fieri.svg

Requiere subir antes ese archivo al repositorio (se entrega junto a este
script). Reduce datos.json en ~105 KB sin cambiar el comportamiento visual.
"""
import json
import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
datos_path = os.path.join(script_dir, '..', 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    raw = f.read()

OLD_PLACEHOLDER_RE = re.compile(r'data:image/svg\+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww\.w3\.org%2F2000%2Fsvg%27[^"]*?%3C%2Fsvg%3E')
NEW_URL = "https://cdn.jsdelivr.net/gh/ibidemrecreacion/ibidemrecreacion.github.io@main/assets/img/General/opus_in_fieri.svg"

count = len(OLD_PLACEHOLDER_RE.findall(raw))
assert count == 72, f"Se esperaban 72 ocurrencias, se encontraron {count}"

raw = OLD_PLACEHOLDER_RE.sub(NEW_URL, raw)

# Round-trip para verificar que el JSON sigue siendo válido
data = json.loads(raw)

with open(datos_path, 'w', encoding='utf-8') as f:
    f.write(raw)

print(f"  ✓  {count} placeholders sustituidos por referencia CDN")
print(f"  ✓  datos.json válido tras la sustitución ({len(raw):,} bytes)")
