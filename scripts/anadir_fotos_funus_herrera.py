#!/usr/bin/env python3
"""
anadir_fotos_funus_herrera.py
Añade las fotos nuevas del reportaje "Fvnvs: El último viaje" (Herrera, 2025)
a su álbum en imagina (id 43), que hasta ahora solo tenía el cartel.

Uso:
    python3 scripts/anadir_fotos_funus_herrera.py
"""

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
DATOS_PATH = os.path.join(REPO_ROOT, "datos.json")

BASE_CDN = "https://cdn.jsdelivr.net/gh/ibidemrecreacion/ibidemrecreacion.github.io@main"
CARPETA = f"{BASE_CDN}/assets/img/Funus/Herrera/2025"

ALBUM_ID = 43

NUEVAS_FOTOS = [
    {"src": f"{CARPETA}/Funus_Herrera_25_01.webp", "caption": ""},
    {"src": f"{CARPETA}/Funus_Herrera_25_02.webp", "caption": ""},
    {"src": f"{CARPETA}/Funus_Herrera_25_03.webp", "caption": ""},
    {"src": f"{CARPETA}/Funus_Herrera_25_04.webp", "caption": ""},
    {"src": f"{CARPETA}/Funus_Herrera_25_05.webp", "caption": ""},
]


def main():
    if not os.path.exists(DATOS_PATH):
        print(f"ERROR: no se encontró {DATOS_PATH}")
        sys.exit(1)

    with open(DATOS_PATH, encoding="utf-8") as f:
        data = json.load(f)  # validación round-trip: lectura

    album = next((a for a in data.get("imagina", []) if a["id"] == ALBUM_ID), None)
    if album is None:
        print(f"ERROR: no se encontró el álbum id={ALBUM_ID} en imagina.")
        sys.exit(1)

    existentes = {img["src"] for img in album["images"]}
    añadidas = 0
    for foto in NUEVAS_FOTOS:
        if foto["src"] in existentes:
            continue
        album["images"].append(foto)
        añadidas += 1

    out = json.dumps(data, ensure_ascii=False, indent=2)
    json.loads(out)  # validación round-trip: reescritura

    with open(DATOS_PATH, "w", encoding="utf-8") as f:
        f.write(out)

    print(f"✓ Álbum id={ALBUM_ID} «{album['eventTitle']}»: {añadidas} fotos añadidas.")
    print(f"✓ Total de imágenes en el álbum ahora: {len(album['images'])}")


if __name__ == "__main__":
    main()
