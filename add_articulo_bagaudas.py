#!/usr/bin/env python3
"""
add_articulo_bagaudas.py
Inserta el artículo "Los bagaudas" en datos.json (tabularium), recuperado
de una publicación original del fundador (José Montesinos Moreno, 2013).

Uso:
    python3 add_articulo_bagaudas.py

Requisitos cumplidos:
- No se edita datos.json a mano.
- El nuevo id es mayor que el máximo existente.
- Se inserta en la posición correcta del array (orden descendente por id,
  igual que el resto del archivo).
- Validación round-trip JSON antes y después de escribir.
"""

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)  # scripts/ vive un nivel por debajo de la raíz
DATOS_PATH = os.path.join(REPO_ROOT, "datos.json")

NUEVO_ARTICULO = {
    "id": 8,
    "category": "Legado",
    "title": "Los bagaudas: la rebelión campesina que desafió a Roma",
    "antetitle": "Del archivo del fundador — texto original de 2013",
    "author": "José Montesinos Moreno",
    "date": "27 de abril de 2013",
    "summary": "Entre los siglos III y V, campesinos, colonos y esclavos de las regiones menos romanizadas de la Galia e Hispania se alzaron contra el poder de Roma. Recuperamos un texto de nuestro fundador sobre el movimiento bagáudico, sus protagonistas y el debate historiográfico que aún genera.",
    "img": "https://placehold.co/1000x400/9A2A2A/F5EFE3?text=LOS+BAGAUDAS",
    "caption": "",
    "intro": "Este artículo recupera un texto escrito por José Montesinos Moreno, fundador de Ibidem, publicado originalmente en 2013. Se reproduce aquí como parte del archivo y la memoria de la Asociación, con una ligera revisión de forma que no altera su contenido ni sus conclusiones. Aborda uno de los episodios menos conocidos del Bajo Imperio romano: el movimiento bagáudico, una rebelión campesina que, entre los siglos III y V, puso en jaque el orden social y fiscal de Roma en las regiones periféricas de la Galia e Hispania.",
    "sections": [
        {
            "title": "El contexto: la crisis del Bajo Imperio (siglos III-IV)",
            "content": "Desde el año 235 d. C. se abre en Roma un largo período de «anarquía militar». Las luchas de los caudillos militares por el poder rompen el equilibrio inestable de la *pax romana* instaurada por Augusto: entre el expansionismo y la resistencia al empuje de los pueblos «bárbaros», entre el gasto militar y los recursos del Estado, entre la producción y el consumo, entre el campo y la ciudad, y entre las pervivencias republicanas del Senado y las tendencias monárquicas de emperadores como Diocleciano (284-305) y Constantino (306-337).\n\nComo señaló el historiador Walbank, el reforzamiento del autoritarismo estatal no respondió a un plan preconcebido, sino a los problemas estructurales del fin del modelo esclavista. El profesor Teja, refiriéndose al caso de Hispania, sitúa el origen de la crisis no tanto en cambios cuantitativos (mano de obra, producción) como en **cambios cualitativos** en la estructura socioeconómica, que tienden a una simplificación y polarización de la sociedad. Estos cambios pueden resumirse en tres puntos:\n\n1. **Cambio en la distribución de la propiedad.** Los *honestiores* (la clase terrateniente) concentran progresivamente la tierra, donde predomina el trabajo de arrendatarios y colonos. El colono busca el amparo del señor rural frente a la presión fiscal y los peligros exteriores mediante la fórmula del *patrocinio*, sustituyendo así al esclavo como mano de obra principal.\n2. **Nuevas relaciones entre campo y ciudad.** Si el Alto Imperio había significado el florecimiento del comercio y la vida urbana, el Bajo Imperio trae consigo la «ruralización» de la sociedad. Los *curiales* —la aristocracia municipal encargada de cobrar impuestos— desaparecen, empobrecidos por la presión fiscal, lo que acaba con la inversión en infraestructuras urbanas.\n3. **Polarización social.** Por un lado, los *honestiores*: grandes senadores, la jerarquía eclesiástica (desde el Edicto de Milán, 313) y los jefes bárbaros asentados como grandes propietarios. Por otro, los *humiliores*: campesinos y artesanos libres o semilibres, entre los que destacan los colonos."
        },
        {
            "title": "Precedentes: de Espartaco a Bulla",
            "content": "La crisis bajoimperial agudizó las luchas sociales, aunque —como advierte D. Plácido— la «lucha de clases» en la Antigüedad no implica necesariamente un conflicto físico y violento. Bajo el aparente equilibrio de la *pax romana* existieron ya precedentes del fenómeno bagáudico, desde la revuelta de esclavos de Espartaco (73-71 a. C.) hasta la «revolución de los desertores» de Materno (186 d. C.) y la de Bulla a comienzos del siglo III, ambas aplastadas sin piedad por Septimio Severo en la península itálica.\n\nSegún E. A. Thompson, Materno no dejó de ser un «Robin Hood» que aspiraba a convertirse en «emperador de los pobres y los ladrones»; Bulla, en cambio, practicó una forma temprana de *bandolerismo social*, más cercana ya al fenómeno bagáudico. A este cuadro cabe sumar movimientos heréticos con fuerte componente social, como los *circumcelliones* del norte de África (segunda mitad del siglo IV) o el priscilianismo hispano (siglos IV-V)."
        },
        {
            "title": "El movimiento bagáudico: cronología de una rebelión",
            "content": "Tradicionalmente se distinguen dos fases del movimiento bagáudico, sin que exista consenso sobre si se trata de un mismo fenómeno continuado o de dos episodios independientes. Geográficamente, ambas se desarrollan en regiones periféricas y menos romanizadas de la Galia e Hispania —la Armórica (actual Bretaña) y la Vasconia (actual País Vasco)—, lo que para Sánchez León constituye su rasgo más característico.",
            "subsections": [
                {
                    "subtitle": "Primer movimiento bagáudico (siglo III)",
                    "content": "Las primeras noticias sobre los bagaudas datan del año 284, coincidiendo con el acceso al trono de Diocleciano, y su radio de acción se circunscribió a las Galias. Aprovechando la inestabilidad política y las invasiones de alamanes y francos, un ejército campesino al mando de Eliano y Amando se alzó contra Roma. La amenaza fue tomada tan en serio que el emperador nombró César a Maximiano y lo envió a sofocar la rebelión. De esta campaña surgió la tradición de la «legión tebana»: el grupo de soldados al mando del futuro san Mauricio que, al negarse a combatir contra otros cristianos, fue ejecutado junto a sus hombres, convertidos en mártires junto a los propios caudillos bagaudas."
                },
                {
                    "subtitle": "Segundo movimiento bagáudico (siglo V)",
                    "content": "El episodio más documentado e importante comenzó hacia el 409 en la rebelde Armórica, precedido de disturbios sociales en los Alpes. Tras el impacto del saco de Roma por Alarico (408-410), el emperador Honorio envió un fuerte ejército que reprimió con dureza la región, sin lograr sofocar la inestabilidad de fondo: entre el 435 y el 437, Tibatón lideró un nuevo ejército de campesinos y esclavos, aplastado con ayuda de la caballería huna; en el 445 se repitió el episodio con apoyo de los alanos —lo que, unido a la intervención del obispo Germán, alimentó la posterior leyenda de unos bagaudas «soldados cristianos»—; y tres años más tarde, el médico Eudoxio, vinculado a la corte de Atila, levantó de nuevo el estandarte de la lucha social con idéntico resultado. Pese a la represión constante, los armoricanos lograron finalmente el estatuto de *federados* de Roma, obteniendo de facto su independencia.\n\nEn Hispania, donde la principal fuente es la *Crónica* de Hidacio, los bagaudas de la Tarraconense occidental atacaron grandes villas y tierras episcopales en un contexto de descomposición política: desde el 409, vándalos, suevos y alanos recorrían la Península, mientras el trigo hispano seguía siendo indispensable para Roma. Frente a esta doble amenaza —bárbara y bagáudica— se organizaron cuerpos militares como los *comitatenses* y los *limitanei*, reforzados por los ejércitos privados de los grandes terratenientes. El episodio más conocido es el de Basilio, que en el 449 asoló el valle del Ebro y dio muerte al obispo de Tarazona. Los bagaudas hispanos llegaron incluso a pactar con reyes bárbaros, como el suevo Requiario a mediados del siglo V, aunque fue finalmente un pueblo bárbaro —el visigodo, el más romanizado de todos— quien los exterminó definitivamente: en el 454, Frederico, hermano del rey Teodorico, acabó con las últimas partidas bagáudicas."
                }
            ]
        },
        {
            "title": "¿Quiénes eran los bagaudas?",
            "content": "Antes de responder a esta pregunta conviene una advertencia metodológica: la cultura dominante tiende a imponer una lectura simplista e individualista de la historia que excluye la complejidad del conflicto social, y en el terreno de la Historia Antigua el problema se agrava aún más. D. Plácido advierte del riesgo de emplear sin matices el concepto de «lucha de clases»: la ortodoxia marxista exige conciencia del propio conflicto para hablar de lucha de clases, pero la explotación puede existir sin esa conciencia, en lo que E. P. Thompson llamó «lucha de clases sin clases».\n\nLas causas del levantamiento bagáudico presentan una doble vertiente: coyuntural (la dureza fiscal, la corrupción administrativa) y estructural (la concentración de la propiedad y el creciente autoritarismo imperial). Mientras E. A. Thompson defendió una lectura «revolucionaria» del fenómeno, Sánchez León prefiere hablar de un *bandolerismo complejo*, a medio camino entre el separatismo social —la aspiración a una «sociedad bagáudica libre»— y el separatismo nacional. Se trataría, en la terminología de Hobsbawm, de un *bandolerismo social*: una protesta endémica del campesinado contra la opresión y la pobreza, con ambiciones limitadas —un mundo tradicional restaurado, no un mundo nuevo.\n\nPara G. Bravo, el movimiento fue esencialmente campesino, compuesto por libres, colonos, libertos y esclavos frente a grandes terratenientes respaldados por los ejércitos imperiales, con posibles vínculos con corrientes heréticas rigoristas. Sánchez León va más allá y niega que exista un «tipo social» bagauda unívoco: coexisten estatus jurídico-económicos distintos (libres, semilibres, esclavos), culturales (vascones, celtas, romanos) y sociales (pequeños propietarios arruinados, braceros, bandoleros, desertores, colonos, esclavos e incluso elementos urbanos de extracción alta).\n\nEl único testimonio literario sobre la vida cotidiana en territorio bagáudico es el *Querolus*, obra anónima que describe una sociedad armoricana del siglo V regida por «leyes del bosque» ajenas a la autoridad romana. Frente a la imagen de anarquismo bagáudico defendida por Mazzarino, las fuentes romanas hablan más bien de una sociedad que «restituyó las leyes, restauró las libertades y no permitió que los propietarios fueran esclavos de sus propios esclavos», lo que sugiere episodios de expropiación de tierras y cierto igualitarismo. E. A. Thompson llegó a hablar de un rudimentario Estado bagauda con una justicia más equitativa, una lectura en la que —como recuerda el hispanista Gabriel Jackson— «el deseo ha impulsado el conocimiento» más de una vez.\n\nMilitarmente, sus ejércitos combinaban una infantería campesina con una caballería formada por pastores, bajo el mando de caudillos —probablemente los más romanizados y de mayor extracción social del grupo— y recurrían sobre todo a la guerrilla, con escasas referencias a grandes batallas campales (como la de Aracelli, cerca de Pamplona, en el 443). Se ha querido ver también en el movimiento un antecedente de las luchas identitarias de bretones y vascones, aunque parece más plausible que respondiera a la falta de integración de las zonas menos romanizadas y a su rechazo de un orden fiscal y social percibido como opresivo."
        },
        {
            "title": "El problema de las fuentes y la historiografía",
            "content": "Como en tantos episodios de la Historia Antigua, el estudio de los bagaudas se enfrenta a la escasez y fragmentación de las fuentes. Para el siglo III, la referencia principal son las crónicas de Mamertino sobre la campaña de Maximiano; para el siglo V son algo más abundantes, con Zósimo, Rutilio Namanciano, el ya citado *Querolus*, Salviano e Hidacio —esta última imprescindible para el caso hispano—.\n\nEl debate historiográfico ha estado marcado por el clima político de las décadas centrales del siglo XX. E. A. Thompson abrió la discusión académica en la revista *Past and Present* en 1952, seguido por autores del bloque comunista. En los años sesenta se enfrentaron dentro del marxismo las tesis de Kovaliov, partidario de la idea de «revolución social», y las de Staerman, que entendía el conflicto como la pugna entre el sistema esclavista y el feudal; en España, A. Barbero y M. Vigil publicaron en esa línea entre 1963 y 1965. La década de los ochenta trajo una revisión más atenta a las fuentes, con la obra de P. Dockés sobre el «bosque» bagauda, y en España destacaron los trabajos de N. Santos y J. J. Sayas en la revista *Hispania*. La obra de referencia en castellano sigue siendo la de Sánchez León, publicada por la Universidad de Jaén en 1996.\n\nDe todo ello pueden extraerse tres grandes lecturas del fenómeno bagáudico:\n\n- La **teoría social**, mayoritariamente de raíz marxista.\n- La **teoría nacional**, que subraya el papel de los elementos indígenas —bretones y vascones— como precedente de un incipiente «nacionalismo».\n- La **teoría funcional**, la más actual, que pone el acento en el carácter interclasista del movimiento y en la cooperación, más que el enfrentamiento sistemático, entre campesinos y propietarios."
        }
    ]
}


def main():
    if not os.path.exists(DATOS_PATH):
        print(f"ERROR: no se encontró {DATOS_PATH}")
        sys.exit(1)

    with open(DATOS_PATH, encoding="utf-8") as f:
        raw = f.read()
    data = json.loads(raw)  # validación round-trip: lectura

    existing_ids = [a["id"] for a in data["tabularium"]]
    if NUEVO_ARTICULO["id"] in existing_ids:
        print(f"ERROR: el id {NUEVO_ARTICULO['id']} ya existe en tabularium.")
        sys.exit(1)
    if NUEVO_ARTICULO["id"] <= max(existing_ids):
        print(f"ERROR: el id {NUEVO_ARTICULO['id']} debe ser mayor que {max(existing_ids)}.")
        sys.exit(1)

    # El array de tabularium sigue un orden descendente por fecha de publicación
    # (no por id). Este artículo es, con diferencia, el más antiguo (2013),
    # así que se añade al final para mantener ese orden cronológico.
    data["tabularium"].append(NUEVO_ARTICULO)

    out = json.dumps(data, ensure_ascii=False, indent=2)
    json.loads(out)  # validación round-trip: reescritura

    with open(DATOS_PATH, "w", encoding="utf-8") as f:
        f.write(out)

    print(f"✓ Artículo id={NUEVO_ARTICULO['id']} «{NUEVO_ARTICULO['title']}» insertado correctamente.")
    print(f"✓ Total artículos en tabularium: {len(data['tabularium'])}")


if __name__ == "__main__":
    main()
