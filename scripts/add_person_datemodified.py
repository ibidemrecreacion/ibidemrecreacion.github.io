#!/usr/bin/env python3
"""
add_person_datemodified.py
Enriquece el JSON-LD de PageArticle (schema-article):
  - author: Organization (con sameAs a Facebook/Instagram) cuando el
    autor es "Ibidem"; Person (con datos reales de nostri.founder
    cuando aplica, p. ej. José Montesinos Moreno) en caso contrario.
  - dateModified (= datePublished como fallback honesto, ya que el
    dataset no rastrea ediciones posteriores).
  - inLanguage: "es".
  - wordCount calculado del texto real del artículo (intro + secciones
    + subsecciones), no inventado.
"""

import os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
PATH = os.path.normpath(PATH)

with open(PATH, encoding='utf-8') as f:
    html = f.read()

old = """    if (art) {
      const schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": art.title,
        "description": art.summary || art.intro?.substring(0, 160),
        "image": art.img,
        "author": {
          "@type": "Person",
          "name": art.author
        },
        "publisher": {
          "@type": "Organization",
          "name": "Ibidem Recreación Histórica",
          "url": "https://ibidemrecreacion.es"
        },
        "datePublished": art.date,
        "mainEntityOfPage": {
          "@type": "WebPage",
          "@id": `${window.location.origin}/article/${art.id}`
        }
      };"""

assert html.count(old) == 1, f"old no es único (encontrado {html.count(old)} veces)"

new = """    if (art) {
      const buildAuthorEntity = authorName => {
        if (!authorName || authorName === "Ibidem") {
          return {
            "@type": "Organization",
            "name": "Ibidem Recreación Histórica",
            "url": "https://ibidemrecreacion.es",
            "sameAs": [data.general?.facebook, data.general?.instagram].filter(Boolean)
          };
        }
        const person = { "@type": "Person", "name": authorName };
        const founder = data.nostri && data.nostri.founder;
        if (founder && founder.name === authorName) {
          person.description = `Fundador y coordinador de Ibidem Recreación Histórica (${founder.years}).`;
          if (founder.image) person.image = founder.image;
        }
        return person;
      };
      const articleText = [
        art.intro || '',
        ...(art.sections || []).map(s => [s.content || '', ...((s.subsections || []).map(ss => ss.content || ''))].join(' '))
      ].join(' ').trim();
      const wordCount = articleText ? articleText.split(/\\s+/).length : undefined;
      const schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": art.title,
        "description": art.summary || art.intro?.substring(0, 160),
        "image": art.img,
        "inLanguage": "es",
        "author": buildAuthorEntity(art.author),
        "publisher": {
          "@type": "Organization",
          "name": "Ibidem Recreación Histórica",
          "url": "https://ibidemrecreacion.es"
        },
        "datePublished": art.date,
        "dateModified": art.date,
        "mainEntityOfPage": {
          "@type": "WebPage",
          "@id": `${window.location.origin}/article/${art.id}`
        }
      };
      if (wordCount) schema.wordCount = wordCount;"""

html = html.replace(old, new, 1)

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print("OK — Person/Organization schema y dateModified insertados.")
