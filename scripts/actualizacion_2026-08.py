#!/usr/bin/env python3
"""
actualizacion_2026-08.py
Aplica las novedades confirmadas del archivo Actividades.txt:

1. Añade fasti: "La fotografía en la recreación histórica" (24 sept 2017)
2. Renombra fasti id19 "Adelfopoiesis" -> "Fraternitas Iurata" (vinculado por tag)
3. Añade fasti: Sit tibi terra levis en Fuente Álamo (19 sept 2014)
   y en Castra Legionis (19 sept 2015)
4. Añade tabularium Legado: "Sit tibi terra levis: la obra teatral"
5. Añade tabularium Legado: "Arqueología experimental: la túnica samnita"
6. Añade fasti: Medinaceli (1-3 mayo 2015) y Bodas, guerra y muerte (17 mayo 2015)
7. Añade tabularium Legado: dos textos sobre el origen de la Navidad (2014 y 2016)
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATOS_PATH = os.path.join(SCRIPT_DIR, "..", "datos.json")

FALLBACK_IMG = (
    "https://cdn.jsdelivr.net/gh/ibidemrecreacion/ibidemrecreacion.github.io@main"
    "/assets/img/General/Pepe_Larario.jpg"
)

with open(DATOS_PATH, encoding="utf-8") as f:
    data = json.load(f)

fasti = data["fasti"]
tabularium = data["tabularium"]
imagina = data["imagina"]

fasti_ids = {e["id"] for e in fasti}
tab_ids = {a["id"] for a in tabularium}


def add_fasti(entry):
    assert entry["id"] not in fasti_ids, f"id de fasti duplicado: {entry['id']}"
    fasti_ids.add(entry["id"])
    fasti.append(entry)


def add_tabularium(entry):
    assert entry["id"] not in tab_ids, f"id de tabularium duplicado: {entry['id']}"
    tab_ids.add(entry["id"])
    tabularium.append(entry)


# ─── 1. La fotografía en la recreación histórica ────────────────────────────
add_fasti({
    "id": 62,
    "title": "La fotografía en la recreación histórica",
    "date": "24 de septiembre de 2017",
    "location": {"locality": "Gilena (Sevilla)", "place": "Castra Legionis"},
    "desc": "Conferencia sobre el papel de la fotografía en la recreación histórica, desarrollada bajo la dirección de José Montesinos Moreno.",
    "tags": ["Institucional"]
})

# ─── 2. Fraternitas Iurata (nombre original de Adelfopoiesis, id 19) ────────
for e in fasti:
    if e["id"] == 19:
        e["title"] = "Fraternitas Iurata"
        e["desc"] = (
            "Recreación del rito de hermandad o adopción ritual en un enclave "
            "de diálogo cultural. Nombre original de esta actividad, "
            "posteriormente rebautizada como Adelfopoiesis."
        )
        if "Adelfopoiesis" not in e["tags"]:
            e["tags"].append("Adelfopoiesis")
        break
else:
    raise RuntimeError("No se encontró fasti id 19")

for a in imagina:
    if a["id"] == 19:
        a["eventTitle"] = "Fraternitas Iurata"
        break
else:
    raise RuntimeError("No se encontró imagina id 19")

# ─── 3. Sit tibi terra levis — nuevas instancias ─────────────────────────────
add_fasti({
    "id": 63,
    "title": "Sit tibi terra levis",
    "date": "19 de septiembre de 2014",
    "location": {"locality": "Puente Genil (Córdoba)", "place": "Villa romana de Fuente Álamo"},
    "desc": "Estreno de la obra teatral Sit tibi terra levis, de José Montesinos Moreno, dentro de las jornadas «Aspectos de la vida cotidiana en una villa romana de la Bética».",
    "tags": ["Rito", "Funerario"]
})

add_fasti({
    "id": 64,
    "title": "Sit tibi terra levis",
    "date": "19 de septiembre de 2015",
    "location": {"locality": "Gilena (Sevilla)", "place": "Castra Legionis"},
    "desc": "Recreación teatralizada del culto a los antepasados y las imagines maiorum, con un coro de manes inspirado en un fragmento de Lucano.",
    "tags": ["Rito", "Funerario"]
})

# ─── 4. Legado: Sit tibi terra levis, la obra teatral ────────────────────────
add_tabularium({
    "id": 15,
    "category": "Legado",
    "title": "Sit tibi terra levis: la obra teatral",
    "antetitle": "Del archivo del fundador — textos originales de 2014 y 2016",
    "author": "José Montesinos Moreno",
    "date": "18 de octubre de 2014",
    "summary": "Recuperamos los textos originales del fundador de Ibidem sobre Sit tibi terra levis, la obra teatral que adapta libremente a Eurípides, Manilio, Lucano y Ovidio para sumergirnos en el mundo de la muerte tal y como lo entendían los romanos.",
    "img": FALLBACK_IMG,
    "caption": "",
    "intro": "Este artículo recupera textos escritos por José Montesinos Moreno, fundador de Ibidem, publicados originalmente en Facebook entre 2014 y 2016 con motivo de las distintas representaciones de Sit tibi terra levis. Se reproducen aquí como parte del archivo y la memoria de la Asociación, respetando su redacción original.",
    "sections": [
        {
            "title": "La obra",
            "content": "<p>Sit tibi terra levis nos sumerge en el mundo de la muerte como lo entendían en la Antigüedad.</p><p>Una obra de José Montesinos Moreno con adaptación libre de textos clásicos. Eurípides, Manilio, Lucano y Ovidio nos sumergen en el mundo de la muerte dónde el olvido, robarle la memoria a un ser humano era la peor de las condenas.</p><p>No os dejará indiferentes pues como en un espejo podremos ver lo frágil que resulta la materia y lo efímero que puede llegar a ser nuestro recuerdo.</p><p>«Un átomo de vida, un suspiro al aire no son nada si no están sometidos al tiempo que los debe provocar. Grabada a fuego la existencia con un sello imborrable»...</p>"
        },
        {
            "title": "El coro de manes: imagines maiorum",
            "content": "<p>Portan las máscaras y retratos funerarios de la familia. La deificación de los antepasados formaba parte imprescindible de la vida y el hogar en las casas romanas e Ibídem lo recuerda en su Sit tibi terra levis.</p><p>«No ha sido el oro de una urna, ni el incienso de la sepultura lo que nos ha hecho alcanzar el lugar donde habitamos. Somos seres de la vida inocente… a los cuales la fuerza del fuego celeste nos ha concedido gozar de la zona donde las almas son recogidas y recorren órbitas enteras. Desde allí, después de haber sido penetrados de luz, vemos la noche profunda que alumbra el día de aquí abajo y nos reímos del ultraje realizado a nuestros despojos mortales».</p><p>(Lucano) Fragmento del coro de manes de la obra Sit tibi terra levis.</p>"
        }
    ]
})

# ─── 5. Legado: Arqueología experimental — túnica samnita ───────────────────
add_tabularium({
    "id": 16,
    "category": "Legado",
    "title": "Arqueología experimental: la túnica samnita",
    "antetitle": "Del archivo del fundador — tres apuntes originales de agosto de 2015",
    "author": "José Montesinos Moreno",
    "date": "4 de agosto de 2015",
    "summary": "Tres apuntes del fundador de Ibidem sobre el proceso de reconstrucción de una túnica samnita de lino, desde el estudio de las fuentes iconográficas hasta la propia arqueología experimental.",
    "img": FALLBACK_IMG,
    "caption": "",
    "intro": "Este artículo reúne tres textos escritos por José Montesinos Moreno, fundador de Ibidem, publicados originalmente en Facebook el 4 y el 5 de agosto de 2015 sobre la reconstrucción experimental de una túnica samnita. Se reproducen aquí como parte del archivo y la memoria de la Asociación, respetando su redacción original.",
    "sections": [
        {
            "title": "Arqueología experimental: el lino y la influencia jónica",
            "content": "<p>Trabajo sobre restos conservados, cultura material y estudios comparativos en representaciones artísticas sobre una túnica samnita de lino.</p><p>Doy comienzo con la adquisición de varios metros de lino puro para la realización de una túnica de los siglos III-II a. de C., coincidente al periodo de la segunda guerra púnica.</p><p>La materia prima: el lino y la influencia jónica.</p><p>El lino ingresó en la civilización doria como un nuevo y raro artículo de lujo, cuyo consumo fue tempranamente limitado por Solón. También entraron en la civilización grecolatina por medio de los géneros más sutiles, las transparencias en el vestir, muy del gusto de las mujeres y recelo principal masculino.</p><p>Lino se ha encontrado en la Argólida, datado 2400-2000 a.C., importación de los colonos procedentes de Egipto y Asia Menor; en este último lugar su datación alcanza los 6000 años (Chatal Hüyük). En Grecia se aclimató sin dificultad en distintas regiones: Tracia, Macedonia, Acaya, y algunas islas como Creta, Chipre y Amorgos. Sin embargo, el centro productor más famoso fue Alejandría. También se ha encontrado una coraza de lino en una tumba de Etruria, pero el uso del lino no se difundió por Roma hasta que lo comenzaron a importar desde Grecia o, al menos, hasta que se conoció el método para obtener fibras de calidad una vez iniciado su cultivo en suelo itálico. Campania, Etruria y el valle del Po aceptaron la flor azul.</p><p>Sobre la difusión del lino en Roma nos da amplias noticias Toussaint-Samat. Su empleo no se limitaba a las prendas de vestir:</p><p>«Al margen del diáfano linón destinado a las mujeres elegantes con maridos tolerantes, el lino debía satisfacer las crecientes necesidades del ejército y la marina (velas y cuerdas), así como el mercado de ropa blanca para el hogar, según la moda egipcia: sábanas, manteles, servilletas, toallas, pañuelos... Con la gran expansión del Imperio, llegaron de la Grecia asiática y de Egipto los mejores tejedores de lino. Tras un período de captación se les enviaba a provincias (Arles, Lyon, Viena, Reims, Metz, Tournai, Tréveris) o a las colonias (España, Reino Unido) para que formaran a los linicultores y obreros de las fábricas imperiales, dirigidas por oficiales jubilados (...) En todas partes la industria del lino se resintió mucho con la caída del Imperio romano y las invasiones bárbaras».</p>"
        },
        {
            "title": "Las fuentes para la investigación sobre túnica samnita",
            "content": "<p>Los diseños con los cuales contamos nos los proporciona principalmente la pintura mural de la Magna Grecia, las cerámicas campanas y las esculturas republicanas y etruscas de la península itálica.</p><p>Tenemos que adentrarnos en sus referentes más directos como son las cerámicas áticas griegas, las cuales nos proporcionan muestras de los tejidos y sobre todo de sus grosores, dimensiones, etc., evidenciadas por las caídas, pliegues y ondulaciones.</p><p>A la hora de reproducir objetos, sobre todo prendas que se adaptan al cuerpo, los cuales aparecen principalmente en representaciones artísticas, debemos ser muy cautos, ya que dicha información está sometida no a una objetividad histórica sino más bien son el resultado de una construcción concreta del pensamiento y por tanto estarán sujetos a valores estéticos según la filosofía del momento en cuestión. Así obtendríamos información errónea para nuestro estudio objetivo si tomamos en cuenta el despliegue de soldados completamente desnudos o semidesnudos que aparecen en las fuentes artísticas.</p><p>Es por esta razón que la escultura nos proporcionará mayor objetividad, si cabe, que el resto de representaciones.</p><p>Haciendo esta observación hemos obtenido como resultado lógico que las túnicas samnitas, al igual que las griegas, suelen ser muy cortas para facilitar el movimiento y la carrera, máxime cuando se porta en el torso protecciones rígidas como los linothorax y/o pectorales de cuero o bronce.</p><p>Nuestro estudio recoge ejemplos significativos como pinturas murales en los sarcófagos de Capua o Paestum, así como cerámicas campanas y esculturas como el samnita de bronce del Museo del Louvre o el etrusco Marte de Todi.</p>"
        },
        {
            "title": "Arqueología experimental: túnica samnita II",
            "content": "<p>Mucho se habla sobre las dimensiones de las piezas de tela para la fabricación de las túnicas militares en general, máxime cuando existe documentación escrita concreta de un autor determinado, pero como todo en cualquier trabajo serio de investigación, es discutible.</p><p>El mundo samnita, al igual que todos los pueblos itálicos de su época, va a estar muy influenciado por el mundo griego. Hemos de recordar que Campania, sur de Italia y Sicilia conformarán la llamada Magna Grecia. Las formas de vestir, bien sean civiles o militares, se amoldarán a los cánones, tanto estéticos como funcionales, de la Hélade.</p><p>Centrándonos en la indumentaria militar y sobre todo en la túnica griega, sus formas y dimensiones principalmente, observamos que se fundamentarán en dos cuestiones básicas: la influencia jónica amante de la amplitud y los plisados y la funcionalidad de la misma atendiendo a la facilidad y comodidad para el movimiento. Esto se observa perfectamente en las pinturas de las cerámicas áticas, fuente de incalculable valor para comprender el tema que estamos tratando.</p><p>Se confeccionaban con dos rectángulos de tela cosidos por los laterales y los hombros dejando aberturas para cabeza y brazos. Piezas amplias que al ser ceñidas mediante cintas obtendrían los característicos plisados y ondulaciones típicas en este tipo de indumentaria. Dicha anchura y arrugas también facilitan el movimiento sobre todo para la carrera y flexura de rodillas a la hora de agacharse.</p><p>Túnicas cuya medida comenzaba en el cuello y en ocasiones bajaba hasta por debajo justo de la rodilla, pues se usarían no sólo para la batalla sino como indumentaria de diario. Es por esta razón que al ser utilizada para el campo de batalla había que incorporarle elementos para modificar su longitud y adaptarla para el combate.</p><p>En las cerámicas se ve en detalle las formas de fijación y modificación de la longitud mediante dobles cintas o pilladas, posiblemente con alfileres, en la parte del cuello, para subir precisamente las zonas correspondientes a los muslos. Esto avala la teoría de lo cortas que llegaron a ser dichas prendas. Del mismo modo y por las mismas razones los samnitas utilizarían la túnica muy corta al modo griego.</p><p>Sirvan de ejemplo las fotografías que presentamos.</p><p>«Arqueología experimental: la túnica samnita».</p>"
        }
    ]
})

# ─── 6. Medinaceli y Bodas, guerra y muerte en Roma ──────────────────────────
add_fasti({
    "id": 65,
    "title": "I Jornadas de Recreación Histórica de Medinaceli",
    "date": "1 al 3 de mayo de 2015",
    "location": {"locality": "Medinaceli (Soria)", "place": ""},
    "desc": "Recreación de feciales y salios, sacerdotes de la guerra, en colaboración con la Legio I Vernácula de Gilena.",
    "tags": ["Rito", "Religión"]
})

add_fasti({
    "id": 66,
    "title": "Bodas, guerra y muerte en Roma",
    "date": "17 de mayo de 2015",
    "location": {"locality": "Sevilla", "place": "Museo Arqueológico"},
    "desc": "Recorrido recreado por los grandes ritos de paso de la vida romana: el matrimonio, la guerra y la muerte.",
    "tags": ["Rito", "Vida cotidiana"]
})

# ─── 7. Legado: dos textos sobre el origen de la Navidad ─────────────────────
add_tabularium({
    "id": 17,
    "category": "Legado",
    "title": "Felices Pascuas: apuntes sobre el origen de la Navidad",
    "antetitle": "Del archivo del fundador — texto original de 2016",
    "author": "José Montesinos Moreno",
    "date": "23 de diciembre de 2016",
    "summary": "Un apunte del fundador de Ibidem sobre por qué el cristianismo primitivo no celebraba el nacimiento de Cristo y cómo se fue fijando, siglos después, la fecha del 25 de diciembre.",
    "img": FALLBACK_IMG,
    "caption": "",
    "intro": "Este artículo recupera un texto escrito por José Montesinos Moreno, fundador de Ibidem, publicado originalmente en Facebook el 23 de diciembre de 2016. Se reproduce aquí como parte del archivo y la memoria de la Asociación, respetando su redacción original.",
    "sections": [
        {
            "title": "Felices Pascuas",
            "content": "<p>Una de las primeras representaciones cristianas de Cristo y su madre.</p><p>En el cristianismo primitivo, aunque casi nadie hace referencia a ello, no se celebraba el nacimiento de Cristo hasta ya alcanzada la libertad de culto y sobre todo constituirse como religión oficial. Por otra parte las primeras referencias que hablan del nacimiento no lo sitúan ni en diciembre ni el día 25, estas son fechas que se imponen en la tardoantigüedad.</p><p>Hasta el siglo III no existen textos sobre la celebración del nacimiento de Jesús ni de la conmemoración de su onomástica, entre otras cosas porque los primeros cristianos no celebraban el nacimiento sino la muerte, que es el verdadero nacimiento a la vida eterna. El nacimiento carnal es la llegada a un mundo de tribulación y prueba.</p><p>Sexto Julio Africano el año 221 y el calendario litúrgico filocaliano del año 354 son los primeros que refieren tales fechas, pero aún así son simples reseñas que no habían calado en las ya extensas comunidades cristianas existentes a lo largo de las provincias occidentales y orientales. A partir del siglo IV los testimonios de este día como fecha del nacimiento de Cristo son comunes en la tradición occidental, mientras que en la oriental prevalece la fecha del 6 de enero.</p><p>Una explicación bastante difundida es que los cristianos optaron por ese día porque, a partir del año 274, el 25 de diciembre se celebraba en Roma el dies natalis Solis invicti, el día del nacimiento del Sol invicto, la victoria de la luz sobre la noche más larga del año. Y esta explicación surge simplemente del paralelismo entre el nacimiento de Jesucristo y expresiones bíblicas como «sol de justicia» (Ma 4,2) y «luz del mundo» (Jn 1,4ss.), textos evangélicos escritos 200 años antes de las fechas señaladas del sol invicto. Además es difícil imaginarse que los cristianos de aquel entonces quisieran adaptar fiestas paganas al calendario litúrgico, especialmente cuando acababan de experimentar la persecución además del rechazo implacable a todo lo que significase influencia religiosa pagana.</p><p>Otra explicación más plausible hace depender la fecha del nacimiento de Jesús de la fecha de su encarnación, que a su vez se relacionaba con la fecha de su muerte. En un tratado anónimo sobre solsticios y equinoccios se afirma que «nuestro Señor fue concebido el 8 de las kalendas de Abril en el mes de marzo (25 de marzo), que es el día de la pasión del Señor y de su concepción, pues fue concebido el mismo día que murió» (B. Botte, Les Origenes de la Noël et de l'Epiphanie, Louvain 1932, l. 230-33). En la tradición oriental, apoyándose en otro calendario, la pasión y la encarnación de Cristo se celebraban el 6 de abril, fecha que concuerda con la celebración de la Navidad el 6 de enero. Se trata de una concepción que también encuentra sus raíces en el judaísmo, donde creación y salvación se relacionaban con el mes de Nisán.</p><p>El arte cristiano ha reflejado esta misma idea a lo largo de la historia al pintar en la Anunciación de la Virgen al niño Jesús descendiendo del cielo con una cruz.</p><p>Así pues, es posible que los cristianos vincularan la redención obrada por Cristo con su concepción, y ésta determinara la fecha del nacimiento. No en vano a estas fechas tan señaladas se las denomina como Pascuas, y ya sabemos que la Pascua es de tradición puramente judía y celebra el paso de la esclavitud a la libertad del pueblo judío en Egipto y la muerte y resurrección de Cristo.</p>"
        }
    ]
})

add_tabularium({
    "id": 18,
    "category": "Legado",
    "title": "El solsticio de invierno y el nacimiento del Sol invicto",
    "antetitle": "Del archivo del fundador — texto original de 2014",
    "author": "José Montesinos Moreno",
    "date": "25 de diciembre de 2014",
    "summary": "Un recorrido del fundador de Ibidem por los mitos solares de la Antigüedad —Osiris, Mitra, Baco, Dioniso— y por el largo proceso que llevó a fijar el nacimiento de Cristo en la fecha del solsticio de invierno.",
    "img": FALLBACK_IMG,
    "caption": "",
    "intro": "Este artículo recupera un texto escrito por José Montesinos Moreno, fundador de Ibidem, publicado originalmente en Facebook el 25 de diciembre de 2014. Se reproduce aquí como parte del archivo y la memoria de la Asociación, respetando su redacción original.",
    "sections": [
        {
            "title": "El solsticio de invierno",
            "content": "<p>Durante el solsticio de invierno (22 de diciembre) el Sol alcanza su cénit en el punto más bajo y desde ese momento el día comienza a alargarse, progresivamente, en detrimento de sus noches, hasta llegar al solsticio de verano, en que invierte su curso. El término solsticio significa 'sol inmóvil', ya que en esos momentos el Sol cambia muy poco su declinación de un día a otro y parece permanecer en un lugar fijo del ecuador celeste.</p><p>El solsticio hiemal es el acontecimiento que vivifica la Naturaleza con su luz y su calor, razón por la cual, para todas las culturas antiguas, representaba el auténtico nacimiento del Sol y, con él, toda la Naturaleza comenzaba a despertar lentamente de su letargo invernal y los humanos veían renovadas sus esperanzas de supervivencia, gracias a la fertilidad de la tierra. En el solsticio de invierno, todos los pueblos antiguos celebraban el nacimiento del astro rey mediante grandes festejos, caracterizados por la alegría general y acompañados de ceremonias colectivas, centradas en cantos y danzas rituales y en la recogida de ciertas plantas mágicas, como el muérdago. Las grandes hogueras tenían la función de provocar el calor y la fuerza de los rayos de un sol recién nacido, que encaraba su curso hacia la primavera, inundando la tierra con su poder regenerador. Otro tanto sucedía durante el solsticio de verano, época adecuada para mostrarle, al divino sol, el agradecimiento de quienes habían sobrevivido un año más, gracias a su generosa intervención en el ciclo agrícola y ganadero. Con el desarrollo de las culturas urbanas, los rituales solsticiales agrarios no desaparecieron, sino que se adaptaron a las nuevas circunstancias y necesidades. Por eso, las fiestas paganas más importantes rebasaron el ámbito campesino y se convirtieron en ciudadanas, de forma que la fecundidad que en origen solicitaban para el campo y el ganado, pasó a comprenderse como prosperidad y riqueza para la ciudad.</p>"
        },
        {
            "title": "Los dioses jóvenes que nacen con el Sol",
            "content": "<p>Desde hace miles de años y para las culturas y sociedades más diversas, el solsticio de invierno ha representado el advenimiento del acontecimiento cósmico por excelencia. No es ninguna casualidad, por tanto, que el natalicio de los principales dioses relacionados con el Sol (como Osiris, Horus, Apolo, Mitra, Dioniso/Baco, etc.) fuese situado durante este período temporal.</p><p>En la antigua Grecia, el culto popular de Dioniso estaba repartido en cuatro grandes festividades: las dos primeras (las Dionisíacas de los campos y las Leneas) se celebraban alrededor del solsticio invernal, con carácter propiciatorio de la fertilidad/prosperidad y en medio de festejos, caracterizados por la gran alegría general. Las dos últimas tenían lugar en la primavera y festejaban la resurrección de la Naturaleza.</p><p>En Roma, la celebración de las Saturnalias (fiestas dedicadas a Saturno, padre de los dioses olímpicos y dios protector de la Naturaleza) duraba una semana. Después de la ceremonia religiosa, había grandes festejos y banquetes, se abolían temporalmente las clases sociales y, en los ágapes, los señores servían a sus esclavos; cesaba toda actividad pública (en tribunales, escuelas, comercios, operaciones militares, etc.) y no se permitía ejercer ningún arte ni oficio, salvo el de la cocina; se imponía el hacerse regalos unos a otros, los ricos convidaban a sus mesas, bien surtidas, a los pobres que llamaban a sus puertas, se practicaban juegos de azar, etc.</p><p>En los mitos solares de todas las culturas antiguas, ocupa un lugar central la presencia de un dios joven (Jesucristo en la religión cristiana), que cada año muere y resucita, encarnando en sí los ciclos de la vida de la Naturaleza.</p><p>Durante el solsticio de invierno, la imagen del dios egipcio Horus era sacada del santuario para ser expuesta a la adoración pública de las masas. Se le representaba como un niño recién nacido, recostado en un pesebre, con cabello dorado, con un dedo en la boca y el disco solar sobre su cabeza.</p><p>Mitra, uno de los principales dioses de la religión hindú, objeto de un culto aparecido unos mil años antes de Cristo, cargaba con los pecados y expiaba las iniquidades de la humanidad, era el principio mediador colocado entre el bien (el dios Ormuzd) y el mal (el dios Ahrimán), el dispensador de luz y bienes, mantenedor de la armonía en el mundo y guardián y protector de todas las criaturas, y era una especie de mesías que, según sus seguidores, debía volver al mundo como juez de los hombres. Era un dios que había nacido de madre virgen, en el solsticio de invierno, en una gruta o cueva, fue adorado por pastores y magos, obró milagros, fue perseguido, acabó siendo muerto y resucitó al tercer día.</p><p>Baco, otro dios solar romano, también estuvo destinado a cargar con las culpas de la humanidad, también fue asesinado y despedazado (como Osiris) y su madre también lo buscó (como Isis) y recogió todos sus pedazos y lo resucitó. Según la tradición, Baco moría despedazado en el equinoccio de primavera y resucitaba a los tres días.</p>"
        },
        {
            "title": "La fijación de una fecha",
            "content": "<p>En el siglo II de nuestra era, los cristianos sólo conmemoraban la Pascua de Resurrección, ya que consideraban irrelevante el momento del nacimiento de Jesús y, además, desconocían absolutamente cuándo pudo haber acontecido. Durante el siglo anterior, al comenzar a aflorar el deseo de celebrar el natalicio de Jesús de una forma clara y diferenciada, algunos teólogos, basándose en los textos de los Evangelios, propusieron datarlo en fechas tan distintas como el 6 y el 10 de enero, el 25 de marzo, el 15 y 20 de abril, etc. Pero el papa Fabián (236-250) decidió cortar por lo sano tanta especulación y calificó de sacrílegos a quienes intentaron determinar la fecha del nacimiento del nazareno.</p><p>A pesar de la disparidad de fechas apuntadas, todos coincidieron en pensar que el solsticio de invierno era la fecha menos probable, si se atendía a lo dicho por Lucas en su Evangelio: «Había en la región unos pastores que pernoctaban al raso y, de noche, se turnaban velando sobre el rebaño. Se les presentó un ángel del Señor y la gloria del Señor los envolvía con su luz…» (Lucas, 2, 8-14). Si los pastores dormían al raso, cuidando de sus rebaños, para que el relato de Lucas fuese cierto y/o coherente, debía de referirse a una noche de primavera, ya que a finales de diciembre, en la zona de Belén, el excesivo frío y las lluvias invernales impiden cualquier posibilidad de pernoctar al raso con el ganado.</p><p>Forzando la escena relatada por Lucas hasta el límite, otras Iglesias cristianas —ajenas a la católica, como la armenia— fijaron la conmemoración de la Natividad en el día 6 de enero, ya que, según su deducción, el relato de Lucas sí puede ser creíble, si se sitúa el nacimiento de Jesús un poco más tarde, en enero y en el Oriente Medio. Un tiempo y un lugar donde es muy probable la existencia de cielos nocturnos claros y sin borrascas, aunque todavía con mucho frío. Con el mismo argumento, otras Iglesias orientales, como la egipcia, griega y etíope, propusieron fijar el Natalicio el día 8 de enero.</p><p>Entrado ya el siglo VI, cuando ya se había concluido el proceso de trasvase de mitos desde los dioses solares jóvenes precristianos hacia la figura de Jesucristo, se decidió fijar una fecha concreta. Dado que a Jesús se le había adjudicado toda la carga legendaria que caracterizaba a su máximo competidor de esos días, el dios Mitra, lo lógico fue hacerle nacer el mismo día en el que se celebraba el advenimiento de ese joven dios. De esta forma, entre los años 354 y 360, durante el pontificado de Liberio (352-366), se tomó por fecha inmutable la de la noche del 24 al 25 de diciembre, fecha en la que los romanos celebraban el Natalus Solis Invicti, el «nacimiento del Sol Invencible», un culto muy popular y extendido al que los cristianos no habían podido vencer y, claro está, la misma fecha en la que todos los pueblos contemporáneos festejaban la llegada del solsticio de invierno. La fecha del 25 de diciembre fue fijada por el orbe católico como algo inamovible, aunque no fue aceptada por la Iglesia oriental que, aún hoy día, sigue celebrando el Natalicio de Jesús el 6 de enero.</p><p>Con la instauración de la Navidad, también se recuperó en Occidente la celebración de los cumpleaños, aunque las parroquias europeas no comenzaron a registrar las fechas de nacimiento de sus feligreses hasta el siglo XII.</p>"
        }
    ]
})

# ─── Guardar y validar ────────────────────────────────────────────────────────
with open(DATOS_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open(DATOS_PATH, encoding="utf-8") as f:
    check = json.load(f)

print("✓ JSON round-trip OK")
print(f"  fasti:      {len(check['fasti'])} (antes 61)")
print(f"  tabularium: {len(check['tabularium'])} (antes 14)")
print(f"  imagina:    {len(check['imagina'])} (sin cambios de tamaño)")
