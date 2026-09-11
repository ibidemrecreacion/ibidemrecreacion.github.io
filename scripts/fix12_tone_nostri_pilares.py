#!/usr/bin/env python3
"""
fix12_tone_nostri_pilares.py
Reescribe nostri.mainText y los tres textos de home.pilares con un tono
menos artificial: tercera persona institucional, frases más concretas,
ritmo menos simétrico. Aprobado por el usuario tras revisar borrador.
"""
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
datos_path = os.path.join(script_dir, '..', 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

OLD_NOSTRI = "Nuestra historia no comienza en los libros, sino en la curiosidad por entender cómo se sentía, cómo se vestía y cómo se vivía el día a día en la Antigüedad Tardía. Ibidem nació como un grupo de entusiastas del rigor histórico que pronto comprendieron que la mejor forma de proteger el patrimonio es dándolo a conocer de una manera tangible y honesta. Nos alejamos del espectáculo bélico para centrar nuestro esfuerzo en la vida civil. Para nosotros, reconstruir un par de zapatos siguiendo un hallazgo arqueológico o recrear el rito de la mesa en una villa romana es un acto de respeto hacia quienes nos precedieron. No pretendemos ser actores que interpretan un papel; nos consideramos divulgadores en activo que utilizan la arqueología experimental como herramienta para conectar el presente con nuestro pasado común. A lo largo de los años, Ibidem ha evolucionado hasta convertirse en un interlocutor de confianza para museos e instituciones culturales. Sin embargo, en el corazón de nuestro proyecto sigue latiendo la misma pasión del primer día: la de habitar la historia para que esta no se olvide, cuidando cada detalle —desde la costura de una túnica hasta la composición de un pigmento— para que el espectador no solo vea el pasado, sino que lo sienta."

NEW_NOSTRI = "La historia de Ibidem no empieza en los libros, sino en la curiosidad por entender cómo se vestía, cómo se comía y cómo se vivía el día a día en la Antigüedad Tardía. La Asociación nació en 2014 de un grupo de personas interesadas en el rigor histórico, con la idea de que proteger el patrimonio pasa por darlo a conocer de forma honesta. Frente al espectáculo bélico habitual en otras propuestas de recreación, Ibidem se queda con la vida civil: el hogar, el taller, la mesa, el rito doméstico. Reconstruir un calzado a partir de un hallazgo arqueológico o representar una boda romana con su ritual completo no es un espectáculo, es una forma de respeto hacia quienes dejaron ese rastro. Con los años, la Asociación se ha convertido en colaboradora habitual de museos y yacimientos. Pero el objetivo sigue siendo el mismo que en 2014: que cada detalle —una costura, un pigmento— ayude a entender cómo era vivir hace mil setecientos años."

assert data['nostri']['mainText'] == OLD_NOSTRI, "nostri.mainText no coincide con lo esperado, revisar antes de sobrescribir"
data['nostri']['mainText'] = NEW_NOSTRI
print("  ✓  nostri.mainText actualizado")

PILARES_NEW = {
    "Rigor arqueológico": "Cada prenda que viste un recreador de Ibidem sale de una fuente concreta: un mosaico, una tumba excavada, una cerámica con restos textiles. La Asociación no reconstruye a ojo: documenta de dónde viene cada pieza.",
    "Historia habitada": "La mayoría de grupos de recreación se centran en la batalla. Ibidem no: le interesa la casa, el taller, la mesa, el funeral — los objetos y gestos de la gente corriente de la Antigüedad Tardía, no solo los de los ejércitos.",
    "Vocación didáctica": "Una recreación bien hecha explica algo que un texto no puede: cómo se ataba una fíbula, cuánto pesaba una toga mojada, qué costaba un tinte de púrpura. Ibidem trabaja con museos y yacimientos para que esa parte de la historia también se vea.",
}

updated = 0
for pilar in data['home']['pilares']:
    if pilar['title'] in PILARES_NEW:
        pilar['text'] = PILARES_NEW[pilar['title']]
        updated += 1
        print(f"  ✓  home.pilares[{pilar['title']!r}] actualizado")

assert updated == 3, f"Se esperaban 3 fichas actualizadas, se actualizaron {updated}"

with open(datos_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("  ✓  datos.json guardado")
