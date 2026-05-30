#!/usr/bin/env python3
"""
precompile.py
Convierte el código JSX de index.html a JavaScript estándar,
eliminando la necesidad de que el navegador descargue Babel (~900 KB).

Uso: python3 precompile.py
Requiere: Node.js y @babel/standalone instalado (lo instala el Action de GitHub)
"""

import re, json, subprocess, os, sys

script_dir = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(script_dir, 'index.html')

with open(index_path, encoding='utf-8') as f:
    html = f.read()

# Si ya está compilado, no hacer nada
if 'text/babel' not in html:
    print("  index.html ya está compilado — sin cambios.")
    sys.exit(0)

# Extraer el bloque JSX
m = re.search(r'<script type="text/babel">(.*?)</script>', html, re.DOTALL)
if not m:
    print("ERROR: no se encontró el bloque JSX en index.html")
    sys.exit(1)

jsx = m.group(1)
print(f"  Compilando {len(jsx):,} caracteres de JSX...")

# Compilar con Babel (Node.js)
r = subprocess.run(
    ['node', '-e', f'''
const babel = require('@babel/standalone');
const result = babel.transform({json.dumps(jsx)}, {{
    presets: ['react'],
    filename: 'app.jsx',
    comments: false,
}});
process.stdout.write(result.code);
'''],
    capture_output=True, text=True
)

if r.returncode != 0:
    print("ERROR durante la compilación:", r.stderr[:400])
    sys.exit(1)

compiled = r.stdout

# Aplicar cambios al HTML:
# 1. Eliminar la etiqueta que carga Babel desde internet
html = re.sub(
    r'\s*<script src="https://unpkg\.com/@babel/standalone@[^"]+"></script>',
    '',
    html
)
# 2. Sustituir el bloque JSX por el JavaScript compilado
html = html.replace(
    f'<script type="text/babel">{jsx}</script>',
    f'<script>{compiled}</script>'
)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"  ✓  index.html compilado — {len(html.encode()) / 1024:.0f} KB")
