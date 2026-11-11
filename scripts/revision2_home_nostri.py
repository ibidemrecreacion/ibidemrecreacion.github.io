#!/usr/bin/env python3
"""
revision2_home_nostri.py
Segunda ronda de correcciones pedidas por Ibidem:
  Home:  cita de Pepe sin año; entradilla no limitada a la Antigüedad Tardía;
         pilar 1 sin ejemplos poco creíbles ni "a ojo"; pilar 2 pasa a
         "Intrahistoria" (sin limitarse a la Antigüedad Tardía); pilar 3 con
         "abrochaba" y sin la toga mojada.
  Nostri: historia propia de Ibidem (2014 en adelante); INTRO como grupo
          distinto, no como su origen.
  index.html: el FAQ usaba el título "Historia habitada" y una pregunta
          comparativa; se ajusta.
  llms.txt: deja de presentar a Ibidem como "evolución" de INTRO.
"""
import json, os

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
P_DATOS, P_HTML, P_LLMS = (os.path.join(BASE, n) for n in ('datos.json', 'index.html', 'llms.txt'))

# ─── datos.json ──────────────────────────────────────────────────────────────
d = json.load(open(P_DATOS, encoding='utf-8'))
h = d['home']

assert h['heroAuthor'] == 'José Montesinos Moreno, 2013'
h['heroAuthor'] = 'José Montesinos Moreno'

assert h['intro'].startswith('Ibidem es una asociación cultural')
h['intro'] = ('Ibidem es una asociación cultural de recreación histórica con sede en Puente Genil. '
              'Reconstruimos la vida cotidiana de la Antigüedad, con especial atención a la época romana y tardoantigua '
              '(bodas, funerales, nacimientos, banquetes, oficios), a partir de fuentes arqueológicas y textuales, '
              'y la presentamos en museos y yacimientos de Andalucía.')

p = {x['title']: x for x in h['pilares']}
assert set(p) == {'Rigor arqueológico', 'Historia habitada', 'Vocación didáctica'}, set(p)
p['Rigor arqueológico']['text'] = ('Nos basamos en fuentes primarias, tanto arqueológicas como textuales. '
                                   'Documentamos de dónde sale cada prenda y cada objeto que presentamos.')
p['Historia habitada']['title'] = 'Intrahistoria'
p['Historia habitada']['text'] = ('Nos interesa la intrahistoria: la casa, el taller, la mesa, el funeral, '
                                  'los objetos y gestos de la gente corriente de cada época.')
p['Vocación didáctica']['text'] = ('Una recreación explica lo que un texto no alcanza: cómo se abrochaba una fíbula, '
                                   'cómo se velaba a una novia. Trabajamos con museos y yacimientos de Andalucía '
                                   'para que esa parte de la historia también se vea.')

assert d['nostri']['mainText'].startswith('Nuestra historia empieza en 1992')
d['nostri']['mainText'] = '\n'.join([
    'Ibidem se fundó en 2014 y desde entonces ha ido construyendo su propia personalidad como grupo. '
    'Nació de la mano de José Montesinos Moreno, que ya había creado en los años noventa INTRO, otro grupo con su propia trayectoria. '
    'En ocasiones hemos trabajado juntos, pero Ibidem e INTRO no son lo mismo.',
    'Empezamos con talleres de tejidos y de eboraria (marfil, hueso, nácar y carey), y ese mismo año presentamos en la Villa romana '
    'de Fuente Álamo, en Puente Genil, las jornadas «Aspectos de la vida cotidiana en una villa romana de la Bética». '
    'Desde entonces hemos trabajado con museos y yacimientos de toda Andalucía y con otros grupos de recreación, '
    'como la Legio I Vernácula, la Legio VII Gemina y la Colección Museográfica de Gilena.',
    'Nuestro centro está en la vida cotidiana de la Antigüedad romana y tardoantigua: la casa, el taller, la mesa, el rito doméstico. '
    'Pero también hemos trabajado otras épocas: la Prehistoria, la Roma republicana y al-Ándalus.',
    'Ibidem es un grupo abierto a cualquier persona con curiosidad por cómo se vestía, se comía y se vivía en el pasado.',
])
open(P_DATOS, 'w', encoding='utf-8').write(json.dumps(d, indent=2, ensure_ascii=False))
json.load(open(P_DATOS, encoding='utf-8'))
print("  ✓ datos.json (Home + Nostri)")

# ─── index.html (FAQ) ────────────────────────────────────────────────────────
html = open(P_HTML, encoding='utf-8').read()
old = '{ q: "¿Qué diferencia a Ibidem de otros grupos de recreación histórica?", a: pilarText("Historia habitada") },'
assert html.count(old) == 1
html = html.replace(old, '{ q: "¿Qué aspectos de la historia trabaja Ibidem?", a: pilarText("Intrahistoria") },', 1)
open(P_HTML, 'w', encoding='utf-8').write(html)
print("  ✓ index.html (FAQ)")

# ─── llms.txt ────────────────────────────────────────────────────────────────
t = open(P_LLMS, encoding='utf-8').read()
def r(old, new):
    global t
    assert t.count(old) == 1, old[:50]
    t = t.replace(old, new, 1)
r('Ibidem nace en 2014 como evolución del grupo INTRO (fundado en 1992 en la Facultad de Bellas Artes de Sevilla), bajo la coordinación de José Montesinos Moreno (1969-2022), fundador y figura de referencia de la recreación histórica en Andalucía.',
  'Ibidem se fundó en 2014 de la mano de José Montesinos Moreno (1969-2022), referente de la recreación histórica en Andalucía, que años antes había creado el grupo INTRO (años 90). INTRO e Ibidem son grupos distintos, con trayectorias propias, que a veces han colaborado. Ibidem es un grupo abierto a cualquier persona.')
r('rigor arqueológico, historia habitada, vocación didáctica', 'rigor arqueológico, intrahistoria, vocación didáctica')
r('Historia de la asociación, de INTRO a Ibidem, y semblanza', 'Historia de la asociación desde 2014 y semblanza')
open(P_LLMS, 'w', encoding='utf-8').write(t)
print("  ✓ llms.txt")
