#!/usr/bin/env python3
path = "cvrator-app.html"
with open(path, encoding="utf-8") as f:
    html = f.read()

def replace_once(old, new, html):
    n = html.count(old)
    assert n == 1, f"expected 1 occurrence, found {n}\n---\n{old[:150]}"
    return html.replace(old, new, 1)

def replace_n(old, new, n_expected, html):
    n = html.count(old)
    assert n == n_expected, f"expected {n_expected} occurrences, found {n}\n---\n{old[:150]}"
    return html.replace(old, new)

# 1. Add YOUTUBE_RE + youTubeThumb helper near BASE_CDN constant
old_1 = """  var BASE_CDN = 'https://cdn.jsdelivr.net/gh/ibidemrecreacion/ibidemrecreacion.github.io@main/assets/img/';"""
new_1 = """  var BASE_CDN = 'https://cdn.jsdelivr.net/gh/ibidemrecreacion/ibidemrecreacion.github.io@main/assets/img/';
  var YOUTUBE_RE = /(?:youtube\\.com\\/(?:watch\\?v=|embed\\/|shorts\\/)|youtu\\.be\\/)([A-Za-z0-9_-]{11})/;
  function youTubeThumb(src){
    var m = (src || '').match(YOUTUBE_RE);
    return m ? 'https://img.youtube.com/vi/' + m[1] + '/hqdefault.jpg' : null;
  }
  function isYouTube(src){ return !!(src || '').match(YOUTUBE_RE); }"""
html = replace_once(old_1, new_1, html)

# 2. thumbHtml: use YouTube thumbnail as preview image when applicable
old_2 = """  function thumbHtml(src, iconOnBroken){
    var safe = escapeHtml(src||'');
    return '<img src="'+safe+'" alt="" loading="lazy" onerror="this.style.display=\\'none\\';this.nextElementSibling.style.display=\\'flex\\';">' +
      '<div class="broken" style="display:none; align-items:center; justify-content:center; flex-direction:column;">' +
      (iconOnBroken ? ICON.image : 'Sin vista previa') + '</div>';
  }"""
new_2 = """  function thumbHtml(src, iconOnBroken){
    var yt = youTubeThumb(src);
    var safe = escapeHtml(yt || src || '');
    return '<img src="'+safe+'" alt="" loading="lazy" onerror="this.style.display=\\'none\\';this.nextElementSibling.style.display=\\'flex\\';">' +
      '<div class="broken" style="display:none; align-items:center; justify-content:center; flex-direction:column;">' +
      (iconOnBroken ? ICON.image : 'Sin vista previa') + '</div>';
  }"""
html = replace_once(old_2, new_2, html)

# 3. Image src input hints (gallery + officina) -> mention YouTube support
old_3a = """        '<span class="field-label">Ruta en assets/img/</span>' +
        '<input type="text" class="img-src" value="'+escapeHtml(toDisplayPath(img.src))+'" placeholder="Pugno/Herrera/2026/foto01.jpg">' +
        '<div style="height:8px;"></div>' +
        '<span class="field-label">Descripción</span>'"""
new_3a = """        '<span class="field-label">Ruta en assets/img/ o enlace de YouTube</span>' +
        '<input type="text" class="img-src" value="'+escapeHtml(isYouTube(img.src) ? img.src : toDisplayPath(img.src))+'" placeholder="Pugno/Herrera/2026/foto01.jpg o https://youtu.be/XXXXXXXXXXX">' +
        '<span class="field-hint">Pega un enlace completo de YouTube para insertarlo como vídeo.</span>' +
        '<div style="height:8px;"></div>' +
        '<span class="field-label">Descripción</span>'"""
html = replace_once(old_3a, new_3a, html)

old_3b = """        '<span class="field-label">Ruta en assets/img/</span>' +
        '<input type="text" class="img-src" value="'+escapeHtml(toDisplayPath(img.src))+'" placeholder="Officina/Textil/foto01.jpg">' +
        '<div style="height:8px;"></div>' +
        '<span class="field-label">Descripción</span>'"""
new_3b = """        '<span class="field-label">Ruta en assets/img/ o enlace de YouTube</span>' +
        '<input type="text" class="img-src" value="'+escapeHtml(isYouTube(img.src) ? img.src : toDisplayPath(img.src))+'" placeholder="Officina/Textil/foto01.jpg o https://youtu.be/XXXXXXXXXXX">' +
        '<span class="field-hint">Pega un enlace completo de YouTube para insertarlo como vídeo.</span>' +
        '<div style="height:8px;"></div>' +
        '<span class="field-label">Descripción</span>'"""
html = replace_once(old_3b, new_3b, html)

# 4. img-src input change handler: don't force-prefix YouTube links with BASE_CDN (toStoredUrl already
#    passes through http(s):// links untouched, but keep display consistent when re-rendering)
old_4 = """      card.querySelector('.img-src').addEventListener('input', function(e){
        img.src = toStoredUrl(e.target.value);
        card.querySelector('.thumb').innerHTML = thumbHtml(img.src,true);
        scheduleSave();
      });"""
new_4 = """      card.querySelector('.img-src').addEventListener('input', function(e){
        var v = e.target.value.trim();
        img.src = isYouTube(v) ? v : toStoredUrl(v);
        card.querySelector('.thumb').innerHTML = thumbHtml(img.src,true);
        scheduleSave();
      });"""
html = replace_n(old_4, new_4, 2, html)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("OK: cvrator-app.html patched")
