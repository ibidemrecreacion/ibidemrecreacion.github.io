#!/usr/bin/env python3
"""
add_faq_schema.py
Convierte PageHome de función-flecha con retorno implícito a cuerpo
de bloque, e inserta un useEffect que genera JSON-LD schema.org/FAQPage
a partir de contenido YA EXISTENTE en datos.json (home.intro,
home.pilares, fasti.location.place, general.email) — sin inventar
ningún dato nuevo.
"""

import os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
PATH = os.path.normpath(PATH)

with open(PATH, encoding='utf-8') as f:
    html = f.read()

# ─── 1. Abrir el cuerpo de PageHome e insertar el useEffect ──────────────────

start_old = '''const PageHome = ({
  data
}) => React.createElement("div", {
  className: "fade-in"
}, React.createElement("section", {'''

assert html.count(start_old) == 1, f"start_old no es único ({html.count(start_old)})"

start_new = '''const PageHome = ({
  data
}) => {
  useEffect(() => {
    const existing = document.getElementById('schema-faq');
    if (existing) existing.remove();
    const pilarText = title => {
      const p = (data.home.pilares || []).find(x => x.title === title);
      return p ? p.text : '';
    };
    const allEvents = Array.isArray(data.fasti)
      ? data.fasti
      : [...((data.fasti && data.fasti.upcoming) || []), ...((data.fasti && data.fasti.past) || [])];
    const museos = Array.from(new Set(
      allEvents.map(e => e.location && e.location.place).filter(Boolean)
    )).slice(0, 8);
    const faqs = [
      { q: "¿Qué es Ibidem Recreación Histórica?", a: data.home.intro },
      { q: "¿Qué diferencia a Ibidem de otros grupos de recreación histórica?", a: pilarText("Historia habitada") },
      { q: "¿Cómo garantiza Ibidem el rigor histórico de sus recreaciones?", a: pilarText("Rigor arqueológico") },
      { q: "¿Qué tipo de actividades organiza Ibidem?", a: pilarText("Vocación didáctica") },
      {
        q: "¿Con qué museos o yacimientos ha colaborado Ibidem?",
        a: museos.length ? `Ibidem ha colaborado con instituciones como ${museos.join(', ')}, entre otras.` : ''
      },
      {
        q: "¿Cómo puedo contactar con Ibidem o proponer una colaboración?",
        a: data.general && data.general.email
          ? `Puede escribir a ${data.general.email} para proponer una colaboración institucional o solicitar una actividad.`
          : ''
      }
    ].filter(f => f.a);
    if (faqs.length) {
      const schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faqs.map(f => ({
          "@type": "Question",
          "name": f.q,
          "acceptedAnswer": { "@type": "Answer", "text": f.a }
        }))
      };
      const tag = document.createElement('script');
      tag.id = 'schema-faq';
      tag.type = 'application/ld+json';
      tag.textContent = JSON.stringify(schema);
      document.head.appendChild(tag);
    }
    return () => {
      const el = document.getElementById('schema-faq');
      if (el) el.remove();
    };
  }, [data]);
  return React.createElement("div", {
  className: "fade-in"
}, React.createElement("section", {'''

html = html.replace(start_old, start_new, 1)

# ─── 2. Cerrar el cuerpo de bloque al final de PageHome ───────────────────────

end_old = '''}, "Leer m\\xE1s")))));
const PageNostri = ({'''

assert html.count(end_old) == 1, f"end_old no es único ({html.count(end_old)})"

end_new = '''}, "Leer m\\xE1s")))));
};
const PageNostri = ({'''

html = html.replace(end_old, end_new, 1)

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print("OK — FAQPage schema insertado en PageHome.")
