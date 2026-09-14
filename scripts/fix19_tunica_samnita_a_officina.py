#!/usr/bin/env python3
"""
fix19_tunica_samnita_a_officina.py
"Arqueología experimental: la túnica samnita" (tabularium id 16) encaja
mejor como ficha de Officina que como artículo de archivo: describe un
proceso de reconstrucción textil, no un texto divulgativo cerrado. Se
elimina de tabularium y se crea una ficha de Officina condensando sus
tres apuntes originales (Actividades.txt, 4-5 agosto 2015), en la voz
de Pepe.
"""
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
datos_path = os.path.join(script_dir, '..', 'datos.json')

with open(datos_path, encoding='utf-8') as f:
    data = json.load(f)

before = len(data['tabularium'])
data['tabularium'] = [a for a in data['tabularium'] if a['id'] != 16]
assert len(data['tabularium']) == before - 1
print(f"  ✓  tabularium: {before} -> {len(data['tabularium'])} (eliminado id 16)")

next_officina_id = max(o['id'] for o in data['officina']) + 1  # 3
data['officina'].append({
    "id": next_officina_id,
    "title": "Túnica samnita",
    "categoria": "Textil",
    "desc": "Reconstruimos una túnica samnita de lino de los siglos III-II a. de C., coincidente con la segunda guerra púnica. El lino no llegó a Roma hasta que se importó desde Grecia, y su presencia está documentada en la Argólida desde el 2400 a. C. Para el patrón nos apoyamos en las cerámicas áticas griegas, las pinturas murales de la Magna Grecia y esculturas como el samnita de bronce del Louvre o el Marte de Todi: dos rectángulos de tela cosidos por los laterales y los hombros, muy cortos —al modo griego— para facilitar la carrera, y con dobles cintas o alfileres en el cuello para acortarlos aún más de cara al combate.",
    "coverImage": "https://cdn.jsdelivr.net/gh/ibidemrecreacion/ibidemrecreacion.github.io@main/assets/img/General/opus_in_fieri.svg",
    "images": [
        {
            "src": "https://cdn.jsdelivr.net/gh/ibidemrecreacion/ibidemrecreacion.github.io@main/assets/img/General/opus_in_fieri.svg",
            "caption": "Estamos trabajando en incorporar el reportaje gráfico de esta actividad."
        }
    ]
})
print(f"  ✓  officina[{next_officina_id}] 'Túnica samnita' creado (categoría Textil)")

with open(datos_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("  ✓  datos.json guardado")
