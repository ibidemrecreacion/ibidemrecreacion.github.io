#!/usr/bin/env python3
"""
generate_og_pages.py
Genera article/N/index.html para cada artículo del tabularium
y actualiza sitemap.xml con todas las URLs del sitio.

Uso:
    python3 generate_og_pages.py
    python3 generate_og_pages.py --base-url https://ibidemrecreacion.github.io
"""

import json
import os
import re
import sys
from datetime import datetime

BASE_URL  = "https://ibidemrecreacion.github.io"
SITE_NAME = "Ibidem Recreación Histórica"
DEFAULT_IMAGE = (
    "https://raw.githubusercontent.com/ibidemrecreacion/ibidemrecreacion.github.io"
    "/main/assets/img/General/Pepe_Larario.jpg"
)

for i, arg in enumerate(sys.argv[1:]):
    if arg == "--base-url" and i + 2 < len(sys.argv):
        BASE_URL = sys.argv[i + 2]

MONTHS = {
    'enero':'01','febrero':'02','marzo':'03','abril':'04',
    'mayo':'05','junio':'06','julio':'07','agosto':'08',
    'septiembre':'09','octubre':'10','noviembre':'11','diciembre':'12'
}

# ─── Utilidades ──────────────────────────────────────────────────────────────

def html_esc(s):
    return s.replace('&','&amp;').replace('"','&quot;').replace('<','&lt;').replace('>','&gt;')

def truncate(text, max_len=160):
    if not text: return ""
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\*+', '', text).strip()
    return text if len(text) <= max_len else text[:max_len-1].rstrip() + "…"

def parse_date(s):
    if not s: return None
    s = s.lower().replace('de ','').strip()
    parts = s.split()
    day, month, year = None, None, None
    for p in parts:
        if p in MONTHS:               month = MONTHS[p]
        elif len(p)==4 and p.isdigit(): year  = p
        elif p.isdigit() and int(p)<=31: day  = p.zfill(2)
    if year and month and day:  return f"{year}-{month}-{day}"
    if year and month:          return f"{year}-{month}-01"
    return None

# ─── Generación de páginas OG ────────────────────────────────────────────────

def replace_og_tags(html, article):
    art_id  = article["id"]
    title   = f'{article["title"]} — {SITE_NAME}'
    desc    = truncate(article.get("summary") or article.get("intro") or "")
    image   = article.get("img") or DEFAULT_IMAGE
    url     = f"{BASE_URL}/article/{art_id}"

    subs = {
        r'<title>.*?</title>':
            f'<title>{html_esc(title)}</title>',
        r'<meta name="description"[^>]*>':
            f'<meta name="description" content="{html_esc(desc)}">',
        r'<link rel="canonical"[^>]*>':
            f'<link rel="canonical" href="{url}">',
        r'<meta property="og:type"[^>]*>':
            '<meta property="og:type" content="article">',
        r'<meta property="og:url"[^>]*>':
            f'<meta property="og:url" content="{url}">',
        r'<meta property="og:title"[^>]*>':
            f'<meta property="og:title" content="{html_esc(title)}">',
        r'<meta property="og:description"[^>]*>':
            f'<meta property="og:description" content="{html_esc(desc)}">',
        r'<meta property="og:image"[^>]*>':
            f'<meta property="og:image" content="{image}">',
        r'<meta property="twitter:url"[^>]*>':
            f'<meta property="twitter:url" content="{url}">',
        r'<meta property="twitter:title"[^>]*>':
            f'<meta property="twitter:title" content="{html_esc(title)}">',
        r'<meta property="twitter:description"[^>]*>':
            f'<meta property="twitter:description" content="{html_esc(desc)}">',
        r'<meta property="twitter:image"[^>]*>':
            f'<meta property="twitter:image" content="{image}">',
    }
    for pattern, replacement in subs.items():
        html = re.sub(pattern, replacement, html)
    return html

def generate_article_pages(data, base_html, script_dir):
    articles = data.get("tabularium", [])
    for art in articles:
        art_id   = art["id"]
        out_dir  = os.path.join(script_dir, "article", str(art_id))
        out_path = os.path.join(out_dir, "index.html")
        os.makedirs(out_dir, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(replace_og_tags(base_html, art))
        print(f"  ✓  article/{art_id}/index.html  —  {art['title'][:55]}")
    print(f"\n  {len(articles)} páginas de artículo generadas.")

# ─── Generación del sitemap.xml ──────────────────────────────────────────────

def generate_sitemap(data, script_dir):
    today  = datetime.now().strftime('%Y-%m-%d')

    static = [
        ('/',           '0.8', today),
        ('/nostri',     '0.6', today),
        ('/fasti',      '0.7', today),
        ('/imagina',    '0.7', today),
        ('/tabularium', '0.8', today),
        ('/civitas',    '0.5', today),
    ]

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path, priority, lastmod in static:
        lines += [
            '  <url>',
            f'    <loc>{BASE_URL}{path}</loc>',
            f'    <lastmod>{lastmod}</lastmod>',
            '    <changefreq>monthly</changefreq>',
            f'    <priority>{priority}</priority>',
            '  </url>',
        ]
    for art in sorted(data.get('tabularium', []), key=lambda a: a['id']):
        lastmod = parse_date(art.get('date')) or today
        lines += [
            '  <url>',
            f'    <loc>{BASE_URL}/article/{art["id"]}</loc>',
            f'    <lastmod>{lastmod}</lastmod>',
            '    <changefreq>monthly</changefreq>',
            '    <priority>0.9</priority>',
            '  </url>',
        ]
    lines.append('</urlset>')

    out_path = os.path.join(script_dir, 'sitemap.xml')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    n = len(data.get('tabularium', []))
    print(f"  ✓  sitemap.xml  ({len(static)} páginas estáticas + {n} artículos)")

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(script_dir, "index.html")
    datos_path = os.path.join(script_dir, "datos.json")

    for path in (index_path, datos_path):
        if not os.path.exists(path):
            print(f"ERROR: no se encontró {path}")
            sys.exit(1)

    with open(index_path, encoding="utf-8") as f:
        base_html = f.read()
    with open(datos_path, encoding="utf-8") as f:
        data = json.load(f)

    print("Generando páginas OG...")
    generate_article_pages(data, base_html, script_dir)

    print("\nGenerando sitemap.xml...")
    generate_sitemap(data, script_dir)

    print("\n¡Listo!")

if __name__ == "__main__":
    main()
