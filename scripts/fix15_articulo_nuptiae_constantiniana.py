#!/usr/bin/env python3
"""
fix15_articulo_nuptiae_constantiniana.py
Añade un cuarto artículo Legado, esta vez con imagen real (no placeholder):
recupera los apuntes de José Montesinos Moreno sobre el ritual nupcial
cristiano recreado en el Circo Máximo de Roma (Natale di Roma 2016).
"""
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
datos_path = os.path.join(script_dir, '..', 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

existing_ids = {a['id'] for a in data['tabularium']}
assert existing_ids == set(range(1, 22)), f"IDs inesperados: {sorted(existing_ids)}"

alb19 = next(a for a in data['imagina'] if a['id'] == 19)
assert alb19['eventTitle'] == 'Nvptiae Constantiniana'
HEADER_IMG = alb19['coverImage']

NEW_ARTICLE = {
    "id": 22,
    "category": "Legado",
    "title": "Nvptiae Constantiniana: el rito nupcial bajo Constantino",
    "antetitle": "Del archivo del fundador — varios apuntes originales de mayo de 2016",
    "author": "José Montesinos Moreno",
    "date": "1 y 2 de mayo de 2016",
    "summary": "Cinco apuntes del fundador de Ibidem sobre la recreación de una boda cristiana del siglo IV en el Circo Máximo de Roma: el sacerdote que sustituye al auspex pagano, la velatio de la novia, el papel de la pronuba y dos notas de vestuario sobre la aristocracia constantiniana.",
    "img": HEADER_IMG,
    "caption": "Nvptiae Constantiniana, recreada en el Circo Máximo de Roma con motivo del Natale di Roma 2016.",
    "intro": "Este artículo recupera varios apuntes escritos por José Montesinos Moreno, fundador de Ibidem, publicados originalmente en Facebook el 1 y el 2 de mayo de 2016, con motivo de la actividad Nvptiae Constantiniana, recreada en el Circo Máximo de Roma junto a la Legio I Vernácula por el Natale di Roma. Se reproducen aquí como parte del archivo y la memoria de la Asociación, respetando su redacción original. Las fotografías de la actividad fueron realizadas por Isa EM, corresponsal en Málaga que cubrió buena parte de las actividades del grupo durante aquellos años.",
    "sections": [
        {
            "title": "El sacerdote sustituye al auspex",
            "content": "En términos generales podemos afirmar que los cristianos del siglo IV contraían matrimonio todavía de la misma forma que sus contemporáneos paganos, e incluso adaptándose a las costumbres de otras religiones dependiendo de la provincia a la que pertenecían. Era una celebración litúrgica ante la Iglesia y en el pórtico del templo, presidida por el sacerdote, quien otorgaba finalmente su bendición a los recién casados. Sin embargo, no existía ninguna ley eclesiástica que obligara a los cristianos a casarse mediante una ceremonia religiosa: el simple intercambio del consentimiento era suficiente. En realidad, el rito religioso no llegó a ser obligatorio en Oriente hasta finales del siglo IX, y en Occidente hasta el Concilio de Trento en el siglo XVI.\n\nEl rito no difiere del común romano, al cual se le sustituyen los sacrificios animales por la eucaristía posterior y la oración. El auspex desaparece para dar paso al sacerdote como mediador entre la víctima —que es Cristo— y los que van a contraer matrimonio, así como el pan que da nombre a la «conferreatio» queda sustituido por el de la eucaristía."
        },
        {
            "title": "La velatio de la novia",
            "content": "La madre, junto a la pronuba o paraninpha (madrina), cubrían a la novia con el «flammeum» o velo, calzando sus pies con zapatos del mismo color. De aquí viene el nombre de nupcias, pues el velo cubre a la novia como una nube. El color del velo hacía alusión al fuego fecundador y, como tal, era símbolo de fertilidad. Las mujeres que entraban a formar parte de la vida consagrada en las primeras comunidades cristianas también hacían uso de este velo y de su color, precisamente por sus desposorios místicos."
        },
        {
            "title": "La pronuba",
            "content": "La pronuba o paraninpha era la madrina que asistía a la novia: una mujer casada una sola vez y experimentada como gran matrona en su propio matrimonio. Ella acompañaba a la novia desde que era vestida para la boda hasta el tálamo nupcial.\n\nEn nuestra recreación, ataviada según modelos encontrados en Antinoópolis (Egipto), la pronuba fue nuestra compañera Lola, de la Legio I Vernácula."
        },
        {
            "title": "Aristócrata viuda del siglo IV",
            "content": "Iconografía extraída de las imágenes catacumbarias y de las cartas de San Jerónimo. En el Natale di Roma 2016, nuestra compañera Fany dio vida a esta aristócrata viuda."
        },
        {
            "title": "La velatio con pallium",
            "content": "Las referencias al enlazado de manos con estola y a la velatio de los nuevos esposos con el pallium las hacen autores como Isidoro de Sevilla, y son costumbres heredadas de diversos pueblos y culturas del extenso Imperio romano. Así se recreó en la actividad realizada en Roma: Nvptiae bajo el dominio constantiniano."
        }
    ],
    "bibliography": []
}

data['tabularium'].append(NEW_ARTICLE)

with open(datos_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"  ✓  tabularium[22] añadido: {NEW_ARTICLE['title']!r}")
print(f"  ✓  imagen de cabecera real: {HEADER_IMG}")
print(f"  ✓  tabularium ahora tiene {len(data['tabularium'])} artículos")
