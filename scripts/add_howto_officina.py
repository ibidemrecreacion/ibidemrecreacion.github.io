#!/usr/bin/env python3
"""
add_howto_officina.py
Inserta JSON-LD en la ficha de detalle de Officina:
  - HowTo con los 5 pasos aprobados para "Túnica samnita" (id 3),
    extraídos literalmente del texto ya existente en datos.json,
    sin ninguna técnica no documentada.
  - CreativeWork genérico (título, descripción, imagen — todo ya
    existente) para el resto de talleres (Eborarium, Taller de
    tejidos), que son contexto histórico, no un procedimiento.
"""

import os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
PATH = os.path.normpath(PATH)

with open(PATH, encoding='utf-8') as f:
    html = f.read()

old = '''  }, [lightboxIndex, selected, albumId]);
  const closeLightbox = () => {
    setLightboxIndex(null);
    if (selected) window.history.replaceState({}, '', `/officina/${selected.id}`);
  };'''

assert html.count(old) == 1, f"old no es único ({html.count(old)})"

new = '''  }, [lightboxIndex, selected, albumId]);
  useEffect(() => {
    const existing = document.getElementById('schema-officina');
    if (existing) existing.remove();
    if (!selected) return;
    const url = `${window.location.origin}/officina/${selected.id}`;
    const cleanDesc = (selected.desc || '').replace(/[*_#]/g, '').slice(0, 300);
    let schema;
    if (selected.id === 3) {
      const steps = [
        { name: "Investigación de fuentes", text: "Se estudian las cerámicas áticas griegas, las pinturas murales de la Magna Grecia y esculturas como el samnita de bronce del Louvre o el Marte de Todi para documentar la forma de la prenda." },
        { name: "Selección de la materia prima", text: "Se emplea lino, tejido que no llegó a Roma hasta su importación desde Grecia; su presencia está documentada en la Argólida desde el 2400 a. C." },
        { name: "Patronaje", text: "El patrón se resuelve con dos rectángulos de tela." },
        { name: "Costura", text: "Los rectángulos se cosen por los laterales y por los hombros." },
        { name: "Ajuste de la longitud", text: "Se añaden dobles cintas o alfileres en el cuello para acortar la prenda al modo griego, muy corta, facilitando la carrera y el combate." }
      ];
      schema = {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": selected.title,
        "description": cleanDesc,
        "image": selected.coverImage,
        "inLanguage": "es",
        "step": steps.map((s, i) => ({
          "@type": "HowToStep",
          "position": i + 1,
          "name": s.name,
          "text": s.text
        })),
        "author": {
          "@type": "Organization",
          "name": "Ibidem Recreación Histórica",
          "url": "https://ibidemrecreacion.es"
        },
        "mainEntityOfPage": { "@type": "WebPage", "@id": url }
      };
    } else {
      schema = {
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "name": selected.title,
        "about": selected.categoria || "Arqueología experimental",
        "description": cleanDesc,
        "image": selected.coverImage,
        "inLanguage": "es",
        "author": {
          "@type": "Organization",
          "name": "Ibidem Recreación Histórica",
          "url": "https://ibidemrecreacion.es"
        },
        "mainEntityOfPage": { "@type": "WebPage", "@id": url }
      };
    }
    const tag = document.createElement('script');
    tag.id = 'schema-officina';
    tag.type = 'application/ld+json';
    tag.textContent = JSON.stringify(schema);
    document.head.appendChild(tag);
    return () => {
      const el = document.getElementById('schema-officina');
      if (el) el.remove();
    };
  }, [selected]);
  const closeLightbox = () => {
    setLightboxIndex(null);
    if (selected) window.history.replaceState({}, '', `/officina/${selected.id}`);
  };'''

html = html.replace(old, new, 1)

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print("OK — HowTo (túnica samnita) + CreativeWork (resto) insertados en Officina.")
