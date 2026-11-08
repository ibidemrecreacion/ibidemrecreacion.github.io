#!/usr/bin/env python3
"""
add_cif_images_nocookie.py
1. Añade el CIF (G14974489) al Aviso Legal, a la Política de Privacidad
   y al schema.org/Organization estático (taxID).
2. Añade sección "Uso de imágenes y derechos de los interesados" a la
   Política de Privacidad, trasladando el texto del Anexo VI del
   Manual de Identidad (aprobado por Ibidem) — uso de planos generales,
   protección del menor, aviso de captación y derecho al olvido.
3. Cambia los dos embeds de YouTube a youtube-nocookie.com y actualiza
   la CSP (frame-src) acorde.
"""

import os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
PATH = os.path.normpath(PATH)

with open(PATH, encoding='utf-8') as f:
    html = f.read()

CIF = "G14974489"

# ─── 1a. CIF en Aviso Legal ───────────────────────────────────────────────────

old = "es titularidad de la Asociación Cultural IBIDEM, entidad sin ánimo de lucro con domicilio en Andalucía (España) y dirección electrónica de contacto: ibidemrecreacion@gmail.com."
assert html.count(old) == 1, f"CIF/legal no único ({html.count(old)})"
new = f"es titularidad de la Asociación Cultural IBIDEM (CIF {CIF}), entidad sin ánimo de lucro con domicilio en Andalucía (España) y dirección electrónica de contacto: ibidemrecreacion@gmail.com."
html = html.replace(old, new, 1)

# ─── 1b. CIF en Política de Privacidad (responsable del tratamiento) ─────────

old = "Asociación Cultural IBIDEM · ibidemrecreacion@gmail.com · Andalucía, España"
assert html.count(old) == 1, f"CIF/privacidad no único ({html.count(old)})"
new = f"Asociación Cultural IBIDEM (CIF {CIF}) · ibidemrecreacion@gmail.com · Andalucía, España"
html = html.replace(old, new, 1)

# ─── 1c. taxID en schema.org/Organization estático ───────────────────────────

old = '"email":"ibidemrecreacion@gmail.com","address":{"@type":"PostalAddress"'
assert html.count(old) == 1, f"taxID anchor no único ({html.count(old)})"
new = f'"email":"ibidemrecreacion@gmail.com","taxID":"{CIF}","address":{{"@type":"PostalAddress"'
html = html.replace(old, new, 1)

# ─── 2. Sección de imágenes en Política de Privacidad ─────────────────────────

old = """TUS DERECHOS

Puedes ejercer los derechos de acceso, rectificación, supresión, limitación, portabilidad y oposición dirigiéndote a ibidemrecreacion@gmail.com. También puedes presentar reclamación ante la Agencia Española de Protección de Datos (www.aepd.es).

MODIFICACIONES"""

assert html.count(old) == 1, f"bloque TUS DERECHOS no único ({html.count(old)})"

new = """USO DE IMÁGENES Y DERECHOS DE LOS INTERESADOS

IBIDEM realiza documentación gráfica de sus actividades de recreación histórica con fines divulgativos y de archivo, parte de la cual se publica en la sección Imagines de esta web.

Uso de imágenes generales: de acuerdo a la legislación vigente, priorizaremos planos generales donde la afluencia de público sea accesoria a la actividad. Se evitarán primeros planos de espectadores sin consentimiento expreso.

Protección del menor: es política inquebrantable de IBIDEM no publicar rostros reconocibles de menores. Cualquier fotografía de alto valor divulgativo que incluya a un niño será desenfocada antes de su difusión, salvo autorización escrita de los tutores legales.

Aviso de captación (texto también presente en la señalética física de nuestras actividades): «La asociación cultural Ibidem realiza documentación gráfica con fines divulgativos y de archivo. El acceso al área de respeto implica la aceptación de la posible aparición accesoria en dichos materiales. Si desea revocar este consentimiento, comuníquelo al personal técnico».

Derecho al olvido: cualquier persona podrá solicitar la retirada inmediata de su imagen de nuestros canales, incluida esta web, mediante comunicación formal a ibidemrecreacion@gmail.com.

TUS DERECHOS

Puedes ejercer los derechos de acceso, rectificación, supresión, limitación, portabilidad y oposición dirigiéndote a ibidemrecreacion@gmail.com. También puedes presentar reclamación ante la Agencia Española de Protección de Datos (www.aepd.es).

MODIFICACIONES"""

html = html.replace(old, new, 1)

# ─── 3a. YouTube → youtube-nocookie.com (dos lightboxes: Imagina y Officina) ──

old_yt = "src: `https://www.youtube.com/embed/${getYouTubeId(lbImg.src)}?autoplay=1&rel=0`,"
count_yt = html.count(old_yt)
assert count_yt == 2, f"se esperaban 2 iframes de YouTube, encontrados {count_yt}"
new_yt = "src: `https://www.youtube-nocookie.com/embed/${getYouTubeId(lbImg.src)}?autoplay=1&rel=0`,"
html = html.replace(old_yt, new_yt)

# ─── 3b. CSP: frame-src a youtube-nocookie.com ────────────────────────────────

old_csp = "frame-src https://www.youtube.com;"
assert html.count(old_csp) == 1, f"frame-src CSP no único ({html.count(old_csp)})"
new_csp = "frame-src https://www.youtube-nocookie.com;"
html = html.replace(old_csp, new_csp, 1)

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print("OK — CIF, política de imágenes y YouTube no-cookie aplicados.")
