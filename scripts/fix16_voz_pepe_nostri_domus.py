#!/usr/bin/env python3
"""
fix16_voz_pepe_nostri_domus.py
Reemplaza nostri.mainText y los tres textos de home.pilares por una
versión en primera persona del plural, con el tono real de José
Montesinos Moreno (Actividades.txt), según la regla editorial acordada:
la voz de Pepe prevalece siempre sobre el Manual de Identidad.
"""
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
datos_path = os.path.join(script_dir, '..', 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

OLD_NOSTRI = "La historia de Ibidem no empieza en los libros, sino en la curiosidad por entender cómo se vestía, cómo se comía y cómo se vivía el día a día en la Antigüedad Tardía. La Asociación nació en 2014 de un grupo de personas interesadas en el rigor histórico, con la idea de que proteger el patrimonio pasa por darlo a conocer de forma honesta. Frente al espectáculo bélico habitual en otras propuestas de recreación, Ibidem se queda con la vida civil: el hogar, el taller, la mesa, el rito doméstico. Reconstruir un calzado a partir de un hallazgo arqueológico o representar una boda romana con su ritual completo no es un espectáculo, es una forma de respeto hacia quienes dejaron ese rastro. Con los años, la Asociación se ha convertido en colaboradora habitual de museos y yacimientos. Pero el objetivo sigue siendo el mismo que en 2014: que cada detalle —una costura, un pigmento— ayude a entender cómo era vivir hace mil setecientos años."

NEW_NOSTRI = "Nuestra historia empieza en 1992, en la Facultad de Bellas Artes de Sevilla, antes incluso de que existiera Ibidem. De ahí salió INTRO, el grupo del que venimos, con la idea de experimentar con las artes plásticas y los sentidos. En 1997 nos plantamos en el yacimiento de Almedinilla y descubrimos que la mejor forma de explicar la Antigüedad no es contarla, sino vivirla: así nació el Convivium, con sus filósofos, sus plañideras y su banquete final. En 2014 fundamos Ibidem para centrarnos en la Antigüedad Tardía, dejando de lado el espectáculo bélico —a nosotros nos interesa la casa, el taller, la mesa, el rito doméstico, no la batalla. Reconstruir un calzado a partir de un hallazgo arqueológico o representar una boda romana entera, con su velatio y su pronuba, no es un espectáculo: es una forma de cuidar lo que otros dejaron. Con los años nos hemos convertido en colaboradores habituales de museos y yacimientos de toda Andalucía, pero seguimos siendo el mismo grupo de curiosos que empezó preguntándose cómo se vestía, cómo se comía y cómo se vivía el día a día hace mil setecientos años."

assert data['nostri']['mainText'] == OLD_NOSTRI, "nostri.mainText no coincide, revisar antes de sobrescribir"
data['nostri']['mainText'] = NEW_NOSTRI
print("  ✓  nostri.mainText actualizado (primera persona)")

PILARES_NEW = {
    "Rigor arqueológico": "Cada prenda que sacamos a la calle sale de una fuente concreta: un mosaico, una tumba excavada, una cerámica con restos textiles. No reconstruimos a ojo: documentamos de dónde sale cada pieza.",
    "Historia habitada": "La mayoría de grupos de recreación se quedan en la batalla. A nosotros nos interesa la casa, el taller, la mesa, el funeral — los objetos y gestos de la gente corriente de la Antigüedad Tardía, no solo los de los ejércitos.",
    "Vocación didáctica": "Una recreación bien hecha explica algo que un texto no puede: cómo se ataba una fíbula, cuánto pesaba una toga mojada, qué costaba un tinte de púrpura. Trabajamos con museos y yacimientos para que esa parte de la historia también se vea.",
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
