#!/usr/bin/env python3
"""
add_legado_tabularium_2026-08.py
Da de alta en tabularium los 9 textos divulgativos recuperados del archivo
histórico de Facebook, todos de autoría de José Montesinos Moreno.
Transcripción fiel: se respeta la redacción original, solo se corrigen
erratas tipográficas objetivas (p. ej. "obre"->"obra", "eclessiae"->"ecclesiae").
No se inventan títulos de sección: cuando el texto original no tenía
subtítulos propios, se usa como único encabezado de sección el mismo título
con el que José publicó el texto.

IDs 9-17 (no colisionan con los existentes 1-8).

PENDIENTE: todos usan de momento la imagen genérica Pepe_Larario.jpg como
placeholder. Sustituir por una imagen real de cada tema antes de publicar.

Uso: colocar en scripts/ en la raíz del repo y ejecutar:
    python3 scripts/add_legado_tabularium_2026-08.py
"""

import json
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
datos_path = os.path.join(repo_root, 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

existing_ids = {e['id'] for e in data['tabularium']}

PLACEHOLDER_IMG = ("https://cdn.jsdelivr.net/gh/ibidemrecreacion/ibidemrecreacion.github.io@main"
                    "/assets/img/General/Pepe_Larario.jpg")

NUEVOS = [
    {
        "id": 9,
        "category": "Legado",
        "title": "El janitor: el guardián olvidado de la domus",
        "antetitle": "Del archivo del fundador — texto original de 2019",
        "author": "José Montesinos Moreno",
        "date": "14 de octubre de 2019",
        "summary": "Recuperamos un texto de nuestro fundador sobre el janitor u ostiario, el esclavo guardián de la puerta que, con el paso del tiempo, llegó a ocupar un lugar de confianza en la domus romana y, más tarde, en las comunidades cristianas primitivas.",
        "img": PLACEHOLDER_IMG,
        "caption": "",
        "intro": "Este artículo recupera un texto escrito por José Montesinos Moreno, fundador de Ibidem, publicado originalmente en Facebook el 14 de octubre de 2019. Se reproduce aquí como parte del archivo y la memoria de la Asociación, respetando su redacción original salvo la corrección de erratas evidentes.",
        "sections": [
            {
                "title": "El janitor",
                "content": "Hoy presentamos a un personaje muy olvidado o que pasa desapercibido pero que su importancia fue creciendo a medida que avanzaba el Imperio Romano llegando al máximo grado durante los comienzos del Bajo Imperio extendiéndose hasta la segunda mitad del siglo XX. Este personaje era el \u201cjanitor\u201d o portero que debe su nombre a Jano, divinidad protectora de las puertas puesto que es el guardián de la puerta de la casa, sobre todo en las viviendas aristocráticas.\n\nEn los primeros tiempos de Roma el janitor era un esclavo que se encontraba encadenado al cuidado de la entrada de la casa pero que fue adquiriendo con el tiempo un papel de relevancia dentro del hogar y puesto que se encargaba tanto de la custodia y guardia de los habitantes de la casa así como de los bienes que las mismas atesoraban, por tanto era el protector de sus moradores y su hacienda. Pero todavía llegaba a ser mucho más importante puesto que también custodiaba la honra de las doncellas de la familia frente a pretendientes y extraños.\n\nEran los que portaban las llaves ya que estaba muy mal visto que los señores las llevaran consigo. Se encargaban de cerrar y abrir los portones y de anunciar a los que llegasen de la calle y poseía el derecho de admisión.\n\nSolían ser personas fuertes, de aspecto serio e imponente pues debían infundir respeto. Junto a él siempre lo acompañaban sus armas más efectivas: los perros y una vara o bastón que le ayudaba tanto a ahuyentar a los no deseados como a dar leñazos en más de una ocasión a ladrones, miserables y niños imprudentes.\n\nA estos janitores se les comenzó a llamar también \u201costiarios\u201d (nombre que procede de ostium o puerta, recordemos el puerto de Ostia llamado así por ser la puerta del comercio marítimo de la ciudad) y que solían habitar en la \u201ccella ostiaria\u201d o estancia anexa a la entrada de la casa y el vestíbulo. Es por ello que en las fauces de algunas casas aparezcan mosaicos con el famoso \u201ccave canem\u201d o lo que es lo mismo \u201ccuidado con el perro\u201d que dejan evidencias de la importancia de estos animales y de sus guardianes.\n\nFue creciendo tanto su importancia en la familia que llegaron a alcanzar un puesto de confianza dentro de la vida doméstica hasta el punto que a finales del siglo III d. de C los obispos cristianos los incluyeron dentro del ministerio puesto que cuidaban de la \u201cdomus ecclesiae\u201d (Casas de reunión cristianas) y los bienes de las comunidades cristianas. Eran ordenados bajo el rito de la entrega de las llaves."
            }
        ]
    },
    {
        "id": 10,
        "category": "Legado",
        "title": "Mujeres dedicadas a la medicina durante la Antigüedad y la Edad Media",
        "antetitle": "Del archivo del fundador — texto sin fecha registrada (h. 2017)",
        "author": "José Montesinos Moreno",
        "date": "Sin fecha",
        "summary": "Un recorrido por las medicae de la Antigüedad: desde la comadrona descrita por Sorano de Éfeso hasta las trescientas setenta y tres autoras griegas y romanas que cita Plinio el Viejo, pasando por Trótula de Salerno.",
        "img": PLACEHOLDER_IMG,
        "caption": "",
        "intro": "Este artículo recupera un texto escrito por José Montesinos Moreno, fundador de Ibidem, sin fecha de publicación registrada en el archivo recuperado. Se reproduce aquí como parte del archivo y la memoria de la Asociación, respetando su redacción original salvo la corrección de erratas evidentes. Fecha por confirmar.",
        "sections": [
            {
                "title": "Mujeres dedicadas a la medicina durante la Antigüedad y la Edad Media",
                "content": "Comencemos a mirar la Historia desde otra perspectiva diferente y abramos los alcanforados arcones de la memoria.\n\nMuchas fueron las mujeres dedicadas a la medicina, las llamadas \"medicae\" y que se encargaban principalmente de los males de las féminas.\n\nNos ha llegado el tratado más antiguo sobre obstetricia datado sobre el siglo II d. de C cuyo autor fue Sorano de Éfeso y su obra \"Gynaikeia\" y que en el siglo VI fue traducido al latín, ejemplar que se conserva y ha llegado hasta nuestros días.\n\nNos habla de la partera o comadrona, mujer culta, preparada y maestra: \u201c(\u2026) debe ser robusta y de fuertes brazos, tener largos y finos dedos con cortas uñas en sus extremos\u2026 debe ser culta, tener una buena memoria, ser capaz de impartir información y ser respetable (\u2026)\u201d.\n\nPero fueron muchos los nombres de mujeres que aparecen a lo largo de la Historia como Agnócide de Atenas, considerada también ginecóloga. Y si buscamos referencias en la Historia de otras mujeres médico encontramos las que hace Plinio el Viejo en su \u201cHistoria Natural\u201d a ¡trescientas veintisiete autoras griegas y cuarenta y seis romanas!, entre ellas las comadronas Olympia de Tebas y Salpe, además de Sótira, Elefantis y Lais, famosas estas dos últimas por curar la malaria utilizando\u2026 ¡sangre menstrual! Galeno menciona a Origenia, Eugerasia y Antioquia. El primer tratado de ginecología escrito por una mujer es de Metrodora y no debemos olvidarnos tampoco de Aspasia, Trótula de Salerno en el siglo XI e incluso Fabiola y Santa Nicerata, representantes de las mujeres que practicaron la medicina con fines caritativos en esos primeros siglos del cristianismo."
            }
        ]
    },
    {
        "id": 11,
        "category": "Legado",
        "title": "Domus Ecclesiae: las primeras casas de culto cristiano",
        "antetitle": "Del archivo del fundador — texto original de 2017",
        "author": "José Montesinos Moreno",
        "date": "23 de enero de 2017",
        "summary": "Antes de que el cristianismo dispusiera de templos propios, las comunidades primitivas se reunían en casas particulares. Un recorrido por las domus ecclesiae, con los ejemplos conservados de Dura Europos y el Celio romano.",
        "img": PLACEHOLDER_IMG,
        "caption": "",
        "intro": "Este artículo recupera un texto escrito por José Montesinos Moreno, fundador de Ibidem, publicado originalmente en Facebook el 23 de enero de 2017. Se reproduce aquí como parte del archivo y la memoria de la Asociación, respetando su redacción original salvo la corrección de erratas evidentes.",
        "sections": [
            {
                "title": "Domus Ecclesiae",
                "content": "El cristianismo nace como una secta del judaísmo durante el siglo primero y a raíz de las enseñanzas de una figura cumbre en la Historia de la Humanidad tanto en cuanto ha sido germen de una de las grandes religiones del mundo.\n\nLas comunidades tanto judeocristianas (comunidades formadas por judíos que adoptan la variante cristiana) como cristianas (nacidas tras el primer Concilio con la adhesión de los paganos) vivieron tiempos de clandestinidad hasta ya entrado el siglo IV y la libertad de culto en el Imperio romano.\n\nEstas comunidades no usaron de templos propiciadas fundamentalmente por las formas de vida y aspectos culturales y cultuales heredados de los primeros fundadores de la nueva religión en la cual, como nos apunta el apóstol Esteban \"el templo es el cuerpo no realizado en piedra ni por manos humanas\" y por tanto no se acota un espacio de oración y culto específico a modo de templo sino a semejanza del cenáculo descrito en los Evangelios recordando las palabras del fundador \"haced esto en recuerdo mío\" puesto que tampoco él consideraba otro templo que no fuese el de Jerusalén. Es por esto que los primeros cristianos adoptan las propias casas de los \"hermanos\" (mayormente por los que tenían medios para ello) para la realización principalmente de la oración comunitaria, la eucaristía y los ágapes. Con posterioridad se irán incluyendo espacios como la piscina bautismal (anteriormente se usaban los ríos o corrientes de agua limpia) y espacios destinados para los catecúmenos o aspirantes al bautismo.\n\nEstas casas, también llamadas Tituli, acogían a las comunidades cristianas hasta que el culto se trasladó a los grandes templos llamados \"iglesias\", nombre que se adopta no por el edificio en sí sino por el hecho de acoger a la asamblea de fieles. Domus ecclesiae es esto precisamente casa de reunión de fieles o casa de la asamblea. Para ello se aprovecharon las casas de las clases pudientes y dos ejemplos hasta ahora conservados se localizan en Siria y Roma. La Domus Ecclesiae (Tituli) de Dura Europos es la única que conserva la sala bautismal, si no ha llegado a ser destruida en la actualidad, claro."
            }
        ]
    },
    {
        "id": 12,
        "category": "Legado",
        "title": "El Opus Sectile de Ostia",
        "antetitle": "Del archivo del fundador — texto original de 2017",
        "author": "José Montesinos Moreno",
        "date": "12 de enero de 2017",
        "summary": "Un análisis del edificio con Opus Sectile de Ostia, hoy conservado en el Museo dell'Alto Medioevo de Roma, como referencia para imaginar el aspecto de los comedores de las grandes villas romanas de la Baetica.",
        "img": PLACEHOLDER_IMG,
        "caption": "",
        "intro": "Este artículo recupera un texto escrito por José Montesinos Moreno, fundador de Ibidem, publicado originalmente en Facebook el 12 de enero de 2017. Se reproduce aquí como parte del archivo y la memoria de la Asociación, respetando su redacción original salvo la corrección de erratas evidentes.",
        "sections": [
            {
                "title": "El Opus Sectile de Ostia",
                "content": "Comenzamos el año con la muestra de una de las maravillas del siglo IV conservadas en el Museo del Alto Medioevo de la ciudad de Roma. Podríamos hacernos una ligera idea del aspecto que ofrecerían los comedores de las grandes villas romanas de la Baetica. Estos espacios ilustran el paisaje arquitectónico en el cual se desarrollarían algunas actividades que realiza nuestro grupo Ibídem Recreación Histórica.\n\nEl edificio con Opus Sectile fue construido a 100 metros de Porta Marina, detrás de la antigua playa en la ciudad portuaria de Ostia. Fue parcialmente excavado en los años 1938-1942, pero gran parte, y especialmente su famosa decoración de muros de mármol (opus sectile), fue desenterrado en los años 1959-1961 (Calza y Gismondi detuvieron su excavación después de descubrir el opus sectile). El edificio fue publicado en detalle por Giovanni Becatti en 1969.\n\nDe 83 monedas se deduce que la construcción se inició en los años 385-388 dC (opus vittatum), pero todavía se puede ver alguna albañilería (opus mixtum). El edificio inacabado fue destruido en 393 dC aproximadamente. No se encontraron restos de fuego y la causa más probable pudo haber sido un terremoto (observemos que en los años 393-394 AD la celda del Templo de Hércules fue restaurada). Después el trabajo no continuó y el edificio nunca fue usado.\n\nSe entra al complejo a través de un vestíbulo con un pórtico (A) al final del Decumanus Maximus. En la entrada hay un umbral con agujeros de pivote para puertas. El vestíbulo conduce a la esquina noreste de un patio de columnas (B), que en su mayor parte fue destruido por el mar y está cubierto por la carretera moderna. Se encontraron restos de un dique que corre hacia el oeste y de un topo perpendicular al dique, tal vez construido en el siglo I dC. El dique fue abandonado durante la construcción de finales de antigüedad. Al este del patio hay una fila de habitaciones, incluyendo una exedra (C), con dos columnas en la entrada y con un suelo de mármol. Otras habitaciones fueron halladas al norte del patio, incluyendo una gran escalera hacia el oeste y la sala D, donde se encontró el opus sectile que dio nombre al edificio. Por alguna razón el nivel en esta parte del edificio fue bajado 1,5 m. En la entrada de la sala D hay dos columnas, descansando sobre el dique abandonado. La parte trasera de la habitación es una alcoba o exedra. Hay una puerta en la pared este.\n\nEl opus sectile fue encontrado en el suelo y la restauración duró muchos años. En 2006 fue trasladado del museo de Ostia al Museo dell'Alto Medioevo en Roma (EUR). Solamente la parte superior de la decoración de mármol de las paredes había sido terminada cuando el edificio fue destruido, de 2,50 a casi 8 metros del suelo. El trabajo en la parte inferior aún no había comenzado. En la parte delantera de la sala hay tres registros en las paredes laterales. En la pared del este se encontraban representaciones de animales y personas: dos leones (amarillos) que atacan a un ciervo (gris azulado), una representación de Cristo con nimbo y barba, y otra de un hombre joven. En la pared oeste había un tigre atacando un ciervo y representaciones de arquitectura y de una ventana.\n\nEl lado sur de las paredes laterales de la parte posterior de la sala estaba decorado con pilastras en opus sectile, con representaciones de zarcillos de vid, pájaros, caracoles, mariposas y gusanos. En las paredes de la parte posterior el mármol imita opus mixtum y ventanas, e incluso sombras. La imitación del ladrillo y tufo de opus mixtum es sorprendente: es un material inferior al mármol, y esa combinación particular no se había utilizado durante siglos en Ostia (aunque algún opus mixtum de época adrianea todavía era visible en este edificio). En la parte inferior de la pared hay un patrón de tablero de ajedrez, tal vez un tapiz.\n\nEl techo parece haber sido decorado con mosaicos sobre fondo azul. No hay paralelos para esta decoración musiva de techos, invención de finales del siglo IV, como podemos leer en una carta escrita por Symmachus (Epist. VIII, 42). Por encima de la entrada a la exedra aparece un arquitrabe con representaciones de muebles y otros objetos. No se encontró pavimento, pero en el edificio ya había varias planchas de mármol destinadas a su decoración."
            }
        ]
    },
    {
        "id": 13,
        "category": "Legado",
        "title": "La dinamización y difusión como recurso de empleo",
        "antetitle": "Del archivo del fundador — texto original de 2013, previo a la fundación de Ibidem",
        "author": "José Montesinos Moreno",
        "date": "10 de mayo de 2013",
        "summary": "Resucitar las humanidades como motor de desarrollo: un ensayo del fundador sobre el papel de la difusión y la dinamización del patrimonio como recurso económico, social y, sobre todo, educativo.",
        "img": PLACEHOLDER_IMG,
        "caption": "",
        "intro": "Este artículo recupera un texto escrito por José Montesinos Moreno, publicado el 10 de mayo de 2013, un año antes de la fundación de Ibidem. Se reproduce aquí como parte del archivo y la memoria de la Asociación, respetando su redacción original salvo la corrección de erratas evidentes.",
        "sections": [
            {
                "title": "La dinamización y difusión como recurso de empleo. Resucitar las humanidades como motor de desarrollo",
                "content": "La experiencia, como mejor consejera y compañera de los profesionales en cualquier materia y oficio, va observando, analizando y cribando. Ciertamente es subjetiva como también lo es la realidad en la que el ser humano se mueve y se desenvuelve pero esta subjetividad, siempre que no sea destructiva, no paraliza a las sociedades, más bien las construye y enriquece. Hemos aprendido de los errores y seguiremos aprendiendo de ellos, eliminando todo lo que nos entorpece en pos del conocimiento serio de las cosas. Este devenir te hace recapacitar y ser crítico en un mundo cada vez más pluralizado y, por qué no decirlo, más complejo por su diversidad.\n\nHemos vivido de la difusión y la dinamización histórica entendida como estudio y práctica, también como recurso económico, político y social, pero por encima de todo como motor de educación y aprendizaje. La democratización de la Cultura, al igual que el velo desgarrado que impedía la contemplación del Sancta Sanctorum, ha abierto las puertas de lo oculto presentando la esencia al servicio de todos, porque todos somos los dueños de lo nuestro y los custodios destinados a dejarlo en herencia. Pero también es cierto, y nunca deberíamos olvidarlo, que el Patrimonio y la Cultura tienen profesionales específicamente preparados para orientar, organizar y presentar, que luchan por la dinamización y la difusión de un pasado aparentemente muerto. Es por esto que las propuestas que deberían exponerse a la hora de abordar recursos concretos de dinamización parten de la necesidad de crear actividades que, si no son tan diferentes al resto de las realizadas en las diversas localidades, yacimientos y museos arqueológicos, sí que aporten algo que las diferencie del resto en pos de una mayor ampliación de conocimientos y experiencias. Algunas de ellas, sobre todo las que presenten oficios concretos, irían enfocadas no solo a la difusión del bien mismo hacia el público al cual van dirigidas, sino que también debieran afectar a sectores que, desgraciadamente y en la actualidad, van perdiendo protagonismo, engrosando las largas listas de profesionales en constante desempleo, tales como escritores, actores, músicos, compositores, poetas, bailarines y artistas, por poner algunos ejemplos. Del mismo modo, deberían buscar estimular la participación ciudadana mediante el asociacionismo, tan en boga en la actualidad y a la vez tan necesario.\n\nEs significativo que en la sociedad actual, heredera directa del pasado que nos ha creado y alumbrado, se dejen al margen profesiones que tan directamente fueron partícipes protagonistas en la creación de los restos que nos han llegado. Conservamos, difundimos y restauramos piedras sin alma en la medida en que estos hallazgos tan solo sirven para ser únicamente contemplados y/o estudiados. Pero estos restos han sido el contenedor de un alma que todavía permanece viva, el alma de los que la hicieron ser, de aquellos que decoraron las paredes y los suelos, del eco de los sonidos de la música y el canto, de las historias que nos han llegado gracias a la poesía y a la literatura, de los actores y el teatro; y precisamente, en las villae romanas, existen ejemplos claros de ello: Baco es el dios de los escenarios, \u201cLas Tres Gracias\u201d de la sabiduría, etc.\n\nLas villas romanas deberían ser un referente, no solo de estudios arqueológicos, científicos, históricos y de conservación y restauración, sino de arqueología experimental de las artes, y estas enfocadas principalmente a las filosofías, al mundo de las ideas y por ende a las formas de entender y vivir la vida en la tardoantigüedad. Un laboratorio de culturas y Cultura, de Libertades y Pensamiento.\n\nOtra cuestión de vital importancia es la implicación de la sociedad donde se encuentran localizados los restos arqueológicos. Una comunidad es consciente del valor del Patrimonio en la medida que lo asume como suyo y lo siente como propio, si lo vive y es partícipe del mismo. Reconocer nuestra historia y nuestro pasado no es tan solo mirarlo en las vitrinas, es fundamentalmente grabarlo en el inconsciente por medio de los sentidos, es llegar a experimentar la simbiosis con el ayer. Pero para que esto suceda hay que cimentar las bases mediante el aprendizaje y la sensibilización y, por tanto, crear y utilizar un buen programa de difusión y dinamización que nos fusione con lo nuestro. El hombre es consustancial a sus acciones, obteniendo como resultado la Historia. Si en el presente somos herederos directos de este legado, nos hacemos un todo y un uno para afrontar el futuro en sociedad. Porque conocer la Historia no es tan solo leerla y aprender fechas, cifras y/o personajes concretos, es sentirla y sumergirse en las almas de aquellos que la hicieron, volver a re-crear momentos, situaciones, y siempre desde sus formas particulares de ver su espacio y su tiempo, porque el hombre como concepto es uno desde ayer hasta mañana y por siempre. Conocer la Historia es eliminar barreras y tabúes manipuladores de conciencias individualistas y partidistas, es no ver amigos ni enemigos, buenos y malos, pues los hombres, con nuestras acciones, somos una ópera coral en constante batalla a merced de cada tiempo y de la suma de todos los tiempos.\n\nTan solo hay una peligrosa enemiga a la que hay que atajar y que es la piedra de tropiezo para avanzar y evolucionar en igualdad, libertad y tolerancia: esa es la ignorancia, resultado de la manipulación de la conciencia del ser humano hacia el mismo ser humano, que incapacita al \u201cyo\u201d como individuo, lo limita y lo somete a las cadenas de la incultura.\n\nReconocer nuestro pasado es asumir la responsabilidad que como seres sociales tenemos frente a las generaciones futuras y, como responsables de las acciones pasadas, nos esforzamos por un mundo mejorado, ya no solo para poder vivir nuestro presente de la mejor manera posible, sino también y sobre todo para construir un futuro que nos supere. Abonar una tierra virgen para los que han de venir. Precisamente bajo este punto de vista es cuando el aprendizaje de la Historia no solo es un derecho sino que se convierte en una obligación tanto para la sociedad como para el Estado. Una obligación que nos construye como sociedad responsable y justa y que nos defiende de las verdades absolutas impuestas por la oligarquía de la sinrazón."
            }
        ]
    },
    {
        "id": 14,
        "category": "Legado",
        "title": "Los tejidos coptos y la iconografía de los pantomimos",
        "antetitle": "Del archivo del fundador — texto original de 2016",
        "author": "José Montesinos Moreno",
        "date": "5 de septiembre de 2016",
        "summary": "Cuando las fuentes escritas escasean, los tejidos coptos de los siglos IV y V se convierten en una fuente primaria de primer orden para reconstruir el vestuario de los actores pantomimos de la Antigüedad Tardía.",
        "img": PLACEHOLDER_IMG,
        "caption": "",
        "intro": "Este artículo recupera un texto escrito y firmado por José Montesinos Moreno (Conservador-Restaurador de Bienes Culturales, Licenciado en Bellas Artes, Coordinador de grupos de Recreación Histórica), publicado originalmente en Facebook el 5 de septiembre de 2016. Se reproduce aquí como parte del archivo y la memoria de la Asociación, respetando su redacción original salvo la corrección de erratas evidentes.",
        "sections": [
            {
                "title": "Vestuario del Bajo Imperio: los actores pantomimos",
                "content": "En multitud de casos las fuentes escritas son muy escasas, aunque siempre nos encontramos con referencias que nos hacen indagar en otras fuentes primarias como las representaciones sobre soportes materiales conservados. En el caso concreto de la indumentaria hay que tener en cuenta que los materiales son de naturaleza principalmente orgánica, sometidos al paso del tiempo y la descomposición.\n\nHoy traemos ejemplos de estudio de vestuario del Bajo Imperio romano y concretamente sobre el aspecto que podrían ofrecer los actores pantomimos.\n\nLa pantomima latina ofrecía espectáculos que versaban sobre los mitos y sus dioses, representándose en teatros, calles, plazas y/o villas. En contra del mimo, eminentemente cómico, las pantomimas solían ser historias trágicas que rápidamente pasaron a la cultura cristiana encarnando a mártires y sus aleccionadoras historias.\n\nRecogemos información extraída de las representaciones mitológicas que aparecen en los tejidos coptos de los siglos IV y V d. de C."
            }
        ]
    },
    {
        "id": 15,
        "category": "Legado",
        "title": "Indumentaria de las aristócratas del Bajo Imperio según las fuentes escritas",
        "antetitle": "Del archivo del fundador — texto original de 2016",
        "author": "José Montesinos Moreno",
        "date": "15 de agosto de 2016",
        "summary": "Las cartas de San Jerónimo, entre otras fuentes del siglo IV, describen con detalle el lujo cromático y ornamental de las aristócratas del Bajo Imperio: seda, albayalde, perlas del mar Rojo y esmeraldas.",
        "img": PLACEHOLDER_IMG,
        "caption": "",
        "intro": "Este artículo recupera un texto escrito por José Montesinos Moreno, fundador de Ibidem, publicado originalmente en Facebook el 15 de agosto de 2016. Se reproduce aquí como parte del archivo y la memoria de la Asociación, respetando su redacción original salvo la corrección de erratas evidentes.",
        "sections": [
            {
                "title": "Indumentaria de las aristócratas del Bajo Imperio",
                "content": "\"Acostumbran a andar con la cara pintada de arrebol y albayalde, lucen vestidos de seda, resplandecen con piedras preciosas, llevan collares de oro, se cuelgan de las orejas horadadas las perlas más preciosas del mar Rojo y despiden fragancia de musgo.\"\n\n\"Que exija todavía algún otro detalle, ora sea embellecerlo en su altiva frente coronada de engastadas amatistas, ora ceñir su cándido cuello de collares fulgurantes, ora colgar a sus cargadas orejas pendientes de verdes esmeraldas. En sus cabellos, relucientes de perfumes, prende la blanca perla de las conchas marinas y con cadenitas de oro quedan sujetos los bucles de su cabellera.\"\n\nDe las cartas de San Jerónimo, siglo IV d. de C."
            }
        ]
    },
    {
        "id": 16,
        "category": "Legado",
        "title": "Oriente en el Bajo Imperio",
        "antetitle": "Del archivo del fundador — texto original de 2016",
        "author": "José Montesinos Moreno",
        "date": "7 de mayo de 2016",
        "summary": "Las influencias estéticas orientales que llegaron a la Bética tardorromana, con la comunidad procedente de Palmira como probable origen del culto a Adonis en el sur de la península ibérica.",
        "img": PLACEHOLDER_IMG,
        "caption": "",
        "intro": "Este artículo recupera un texto escrito por José Montesinos Moreno, fundador de Ibidem, publicado originalmente en Facebook el 7 de mayo de 2016. Se reproduce aquí como parte del archivo y la memoria de la Asociación, respetando su redacción original salvo la corrección de erratas evidentes.",
        "sections": [
            {
                "title": "Oriente en el Bajo Imperio",
                "content": "Nuestra propuesta va más allá de Occidente para entrar de lleno en el oriente del Bajo Imperio, puesto que las influencias estéticas posteriores a la caída de Roma como capital se van a ir imponiendo hasta alcanzar la Alta Edad Media europea.\n\nRepresentamos a un aristócrata de la ciudad siria de Palmira. Es conocido que en la Bética tardorromana existía una comunidad procedente de esta parte de Oriente Próximo que probablemente introdujese el culto a Adonis en el sur de la península ibérica."
            }
        ]
    },
    {
        "id": 17,
        "category": "Legado",
        "title": "Peinado femenino del siglo IV",
        "antetitle": "Del archivo del fundador — texto original de 2016",
        "author": "José Montesinos Moreno",
        "date": "7 de mayo de 2016",
        "summary": "Los sarcófagos paleocristianos de la basílica de San Sebastián en Roma y las monedas del Bajo Imperio como fuentes para reconstruir el peinado femenino del siglo IV.",
        "img": PLACEHOLDER_IMG,
        "caption": "",
        "intro": "Este artículo recupera un texto escrito por José Montesinos Moreno, fundador de Ibidem, publicado originalmente en Facebook el 7 de mayo de 2016. Se reproduce aquí como parte del archivo y la memoria de la Asociación, respetando su redacción original salvo la corrección de erratas evidentes.",
        "sections": [
            {
                "title": "Peinado femenino del siglo IV",
                "content": "Investigando sobre caracterizaciones del siglo IV recogemos ejemplos de los sarcófagos paleocristianos. En este caso concreto, de los existentes en la basílica de San Sebastián en Roma y en monedas del Bajo Imperio.\n\nPeinado realizado por nuestra compañera de Ibídem Eva Torres Castillo."
            }
        ]
    },
]

conflicts = existing_ids & {e['id'] for e in NUEVOS}
if conflicts:
    print(f"  ERROR: los ids {conflicts} ya existen en tabularium. Abortando.")
    sys.exit(1)

data['tabularium'].extend(NUEVOS)

# --- Validación round-trip ---
serialized = json.dumps(data, ensure_ascii=False, indent=2)
reparsed = json.loads(serialized)
assert reparsed == data, "El JSON no sobrevive al round-trip"

# --- Comprobación: todos los títulos y el autor están presentes ---
for e in NUEVOS:
    assert e['title'] in serialized, f"Falta el título '{e['title']}' tras la serialización"
    assert 'José Montesinos Moreno' in json.dumps(e, ensure_ascii=False), f"Falta la autoría en '{e['title']}'"

with open(datos_path, 'w', encoding='utf-8') as f:
    f.write(serialized + '\n')

print(f"  \u2713 {len(NUEVOS)} artículos del Legado añadidos a tabularium (ids {NUEVOS[0]['id']}-{NUEVOS[-1]['id']})")
print("  \u2713 Round-trip JSON validado")
print("  \u2713 Comprobación de títulos y autoría: OK")
print("  PENDIENTE: sustituir PLACEHOLDER_IMG por una imagen real en cada artículo.")
print("  PENDIENTE: confirmar fecha de 'Mujeres dedicadas a la medicina...' (id 10).")
print("  Recuerda ejecutar generate_og_pages.py o dejar que lo haga el Action tras el push.")
