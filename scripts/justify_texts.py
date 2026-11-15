#!/usr/bin/env python3
"""
justify_texts.py
Texto corrido justificado con partición silábica (hyphens:auto, <html lang="es">):
  - CSS común para .text-reading, .text-justify y la nueva .justify-text,
    con hyphenate-limit-chars para evitar particiones feas.
  - Se añade .justify-text a los párrafos que estaban centrados o alineados
    a la izquierda: entradilla de la Home, fichas de pilares, descripciones
    de tarjetas de actividad, textos de Officina, Contactus y textos legales.
Quedan fuera (por diseño): títulos, rótulos, pies de foto, la cita del hero,
mensajes de una línea (estados vacíos, 404).
"""
import os

PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html'))
html = open(PATH, encoding='utf-8').read()

def rep(old, new, label):
    global html
    n = html.count(old)
    assert n == 1, f"{label}: {n} coincidencias"
    html = html.replace(old, new, 1)
    print("  ✓", label)

# ─── CSS ─────────────────────────────────────────────────────────────────────
rep('''        /* Home: hero sin degradados + fichas de pieza''', '''        /* Texto corrido: justificado con partición silábica (html lang="es") */
        .text-reading, .text-reading p, .text-justify, .justify-text, .ficha-texto {
            text-align: justify;
            hyphens: auto;
            -webkit-hyphens: auto;
            hyphenate-limit-chars: 6 3 3;
            overflow-wrap: break-word;
        }

        /* Home: hero sin degradados + fichas de pieza''', 'CSS justificado')

# ─── Clases en los párrafos ──────────────────────────────────────────────────
def add_class(old_cls, label):
    rep(f'className: "{old_cls}"', f'className: "{old_cls} justify-text"', label)

add_class('text-xl md:text-2xl text-texto leading-relaxed font-merriweather font-light', 'Home: entradilla')
add_class('font-merriweather text-sm text-gray-700 leading-relaxed mb-6 line-clamp-4 flex-grow', 'Tarjetas de actividad')
add_class('max-w-2xl mx-auto text-center font-merriweather text-sm text-gray-600 italic -mt-6 mb-10 px-4', 'Officina: descripción')
add_class('max-w-2xl mx-auto text-center font-merriweather text-base text-gray-700 leading-relaxed mb-10 px-2', 'Officina: introducción')
add_class('font-merriweather text-base text-gray-700 leading-relaxed max-w-xl mx-auto', 'Contactus')
add_class('font-merriweather text-sm text-texto leading-relaxed whitespace-pre-line', 'Textos legales')

open(PATH, 'w', encoding='utf-8').write(html)
print("OK — justificado aplicado.")
