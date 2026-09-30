#!/usr/bin/env python3
"""
add_nap_partial.py
Añade un NAP parcial y responsable al schema.org/Organization estático
del <head>: solo localidad (Puente Genil), región y país. Sin
streetAddress ni telephone, por decisión explícita de la asociación
(sede es domicilio particular; no hay teléfono oficial, solo
personales de la directiva).
"""

import os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
PATH = os.path.normpath(PATH)

with open(PATH, encoding='utf-8') as f:
    html = f.read()

old = '{"@context":"https://schema.org","@type":"Organization","name":"Ibidem Recreación Histórica","url":"https://ibidemrecreacion.es/","email":"ibidemrecreacion@gmail.com","sameAs":["https://www.facebook.com/ibidem.ibidem/","https://www.instagram.com/ibidemrecreacion/"]}'

assert html.count(old) == 1, f"old no es único ({html.count(old)})"

new = '{"@context":"https://schema.org","@type":"Organization","name":"Ibidem Recreación Histórica","url":"https://ibidemrecreacion.es/","email":"ibidemrecreacion@gmail.com","address":{"@type":"PostalAddress","addressLocality":"Puente Genil","addressRegion":"Andalucía","addressCountry":"ES"},"areaServed":"Andalucía","sameAs":["https://www.facebook.com/ibidem.ibidem/","https://www.instagram.com/ibidemrecreacion/"]}'

html = html.replace(old, new, 1)

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print("OK — NAP parcial (localidad) insertado en Organization schema.")
