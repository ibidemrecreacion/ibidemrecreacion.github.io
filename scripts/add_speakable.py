#!/usr/bin/env python3
"""
add_speakable.py
Añade schema.org SpeakableSpecification al Article JSON-LD, apuntando
a selectores CSS estables (clases marcador sin efecto visual) sobre
el titular y la entradilla del artículo — el contenido que un
asistente de voz / motor de respuesta debería leer primero.
"""

import os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
PATH = os.path.normpath(PATH)

with open(PATH, encoding='utf-8') as f:
    html = f.read()

# ─── 1. Marcar el H1 del artículo con una clase estable, sin tocar estilos ───

old_h1 = '''    className: "font-cinzel text-3xl md:text-5xl font-bold text-texto mb-6 leading-tight"'''
assert html.count(old_h1) == 1, f"old_h1 no es único ({html.count(old_h1)})"
new_h1 = '''    className: "article-headline font-cinzel text-3xl md:text-5xl font-bold text-texto mb-6 leading-tight"'''
html = html.replace(old_h1, new_h1, 1)

# ─── 2. Marcar la entradilla (intro) con una clase estable ───────────────────

old_intro = '''    className: "text-xl md:text-2xl font-light italic leading-relaxed mb-10 pl-6 border-l-4 border-pompeyano text-gray-700"'''
assert html.count(old_intro) == 1, f"old_intro no es único ({html.count(old_intro)})"
new_intro = '''    className: "article-intro text-xl md:text-2xl font-light italic leading-relaxed mb-10 pl-6 border-l-4 border-pompeyano text-gray-700"'''
html = html.replace(old_intro, new_intro, 1)

# ─── 3. Añadir "speakable" al schema Article ─────────────────────────────────

old_schema = '''      if (wordCount) schema.wordCount = wordCount;'''
assert html.count(old_schema) == 1, f"old_schema no es único ({html.count(old_schema)})"
new_schema = '''      if (wordCount) schema.wordCount = wordCount;
      schema.speakable = {
        "@type": "SpeakableSpecification",
        "cssSelector": [".article-headline", ".article-intro"]
      };'''
html = html.replace(old_schema, new_schema, 1)

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print("OK — speakable insertado (clases marcador + schema).")
