#!/usr/bin/env python3
"""
actualizar_imagenes_articulos.py
Sustituye las imágenes placeholder (placehold.co) de portada y de sección en
tabularium por las ilustraciones definitivas subidas al repositorio, servidas
vía jsDelivr.

Uso:
    python3 scripts/actualizar_imagenes_articulos.py
"""

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
DATOS_PATH = os.path.join(REPO_ROOT, "datos.json")

BASE_CDN = "https://cdn.jsdelivr.net/gh/ibidemrecreacion/ibidemrecreacion.github.io@main"

REEMPLAZOS = {
    "https://placehold.co/1000x400/2A2A2A/F5EFE3?text=FUNUS+ROMANO":
        f"{BASE_CDN}/assets/img/Articulos/Funus/Funus_portada.jpg",
    "https://placehold.co/1000x400/8B4513/F5EFE3?text=HOMBRES+DE+CEBADA":
        f"{BASE_CDN}/assets/img/Articulos/Hordearii/Hordearii_portada.jpg",
    "https://placehold.co/1000x400/9A2A2A/F5EFE3?text=LA+CANICULA+ROMANA":
        f"{BASE_CDN}/assets/img/Articulos/Canícula/Canicula_atrio.jpg",
    "https://placehold.co/800x400/2D2D2D/D4A017?text=SIRIO+Y+EL+CAN+MAYOR":
        f"{BASE_CDN}/assets/img/Articulos/Canícula/Canicula_orto_heliaco.jpg",
    "https://placehold.co/800x400/7A7A52/F5EFE3?text=MEDICINA+Y+SUPERSTICION":
        f"{BASE_CDN}/assets/img/Articulos/Canícula/Canicula_medicus.jpg",
    "https://placehold.co/800x400/DAA520/3E2823?text=GRANO+Y+LEGUMBRES":
        f"{BASE_CDN}/assets/img/Articulos/Hordearii/Hordearii_grano.jpg",
    "https://placehold.co/800x400/555555/F5EFE3?text=MOSAICO+GLADIADORES":
        f"{BASE_CDN}/assets/img/Articulos/Hordearii/Hordearii_mosaico.jpg",
}
# Nota: la clave de "grano y legumbres" se corrige más abajo por si el color
# exacto del placeholder difiere (DAA520/3E2723 vs 3E2823); se busca por
# coincidencia de texto, no solo por URL exacta, para evitar fallos silenciosos.


def replace_recursive(node, counter):
    if isinstance(node, dict):
        return {k: replace_recursive(v, counter) for k, v in node.items()}
    if isinstance(node, list):
        return [replace_recursive(v, counter) for v in node]
    if isinstance(node, str):
        for old, new in REEMPLAZOS.items():
            if node == old:
                counter[old] = counter.get(old, 0) + 1
                return new
        # coincidencia por contenido (texto tras "text=") como red de seguridad
        if node.startswith("https://placehold.co/") and "text=" in node:
            texto = node.split("text=")[-1]
            for old, new in REEMPLAZOS.items():
                if old.split("text=")[-1] == texto:
                    counter[old] = counter.get(old, 0) + 1
                    return new
        return node
    return node


def main():
    if not os.path.exists(DATOS_PATH):
        print(f"ERROR: no se encontró {DATOS_PATH}")
        sys.exit(1)

    with open(DATOS_PATH, encoding="utf-8") as f:
        data = json.load(f)  # validación round-trip: lectura

    counter = {}
    data = replace_recursive(data, counter)

    faltantes = [old for old in REEMPLAZOS if old not in counter]
    if faltantes:
        print("AVISO: no se encontraron (o ya estaban sustituidos) estos placeholders:")
        for f_ in faltantes:
            print("  -", f_)

    out = json.dumps(data, ensure_ascii=False, indent=2)
    json.loads(out)  # validación round-trip: reescritura

    with open(DATOS_PATH, "w", encoding="utf-8") as f:
        f.write(out)

    print(f"✓ Sustituciones aplicadas: {sum(counter.values())} de {len(REEMPLAZOS)} URLs objetivo.")
    for old, n in counter.items():
        print(f"  - {n}x  {REEMPLAZOS[old].split('/assets/')[-1]}")


if __name__ == "__main__":
    main()
