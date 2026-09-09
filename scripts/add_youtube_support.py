#!/usr/bin/env python3
import re, sys

path = "index.html"
with open(path, encoding="utf-8") as f:
    html = f.read()

def replace_once(old, new, html):
    n = html.count(old)
    assert n == 1, f"expected 1 occurrence, found {n}\n---\n{old[:120]}"
    return html.replace(old, new, 1)

def replace_n(old, new, n_expected, html):
    n = html.count(old)
    assert n == n_expected, f"expected {n_expected} occurrences, found {n}\n---\n{old[:120]}"
    return html.replace(old, new)

# 1. Add YouTube helper + update isVideoSrc
old_1 = """const VIDEO_EXTENSIONS = ['.mp4', '.webm', '.mov', '.m4v', '.ogg'];
const isVideoSrc = (src, item) => {
  if (item && item.type === 'video') return true;
  if (!src) return false;
  const clean = src.split('?')[0].split('#')[0].toLowerCase();
  return VIDEO_EXTENSIONS.some(ext => clean.endsWith(ext));
};"""
new_1 = """const VIDEO_EXTENSIONS = ['.mp4', '.webm', '.mov', '.m4v', '.ogg'];
const YOUTUBE_RE = /(?:youtube\\.com\\/(?:watch\\?v=|embed\\/|shorts\\/)|youtu\\.be\\/)([A-Za-z0-9_-]{11})/;
const getYouTubeId = src => {
  if (!src) return null;
  const m = src.match(YOUTUBE_RE);
  return m ? m[1] : null;
};
const isVideoSrc = (src, item) => {
  if (item && item.type === 'video') return true;
  if (!src) return false;
  if (getYouTubeId(src)) return true;
  const clean = src.split('?')[0].split('#')[0].toLowerCase();
  return VIDEO_EXTENSIONS.some(ext => clean.endsWith(ext));
};"""
html = replace_once(old_1, new_1, html)

# 2. Lightbox video/image block -> add YouTube iframe branch (appears twice: PageImagina + PageOfficina)
old_2 = """    }, isVideoSrc(lbImg.src, lbImg) ? React.createElement("video", {
      key: lbImg.src,
      src: lbImg.src,
      poster: lbImg.poster || undefined,
      controls: true,
      autoPlay: true,
      playsInline: true,
      style: {
        maxWidth: '100%',
        maxHeight: '100%',
        width: 'auto',
        height: 'auto',
        display: 'block',
        animation: 'lbFadeIn 0.22s ease-out'
      }
    }) : React.createElement("img", {
      key: lbImg.src,
      src: lbImg.src,
      alt: lbImg.caption || `Foto ${lightboxIndex + 1} de ${total}`,
      style: {
        maxWidth: '100%',
        maxHeight: '100%',
        width: 'auto',
        height: 'auto',
        objectFit: 'contain',
        display: 'block',
        animation: 'lbFadeIn 0.22s ease-out'
      }
    })), React.createElement("div", {"""
new_2 = """    }, getYouTubeId(lbImg.src) ? React.createElement("iframe", {
      key: lbImg.src,
      src: `https://www.youtube.com/embed/${getYouTubeId(lbImg.src)}?autoplay=1&rel=0`,
      title: lbImg.caption || 'V\\xEDdeo',
      allow: "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",
      allowFullScreen: true,
      style: {
        width: '90vw',
        maxWidth: '960px',
        aspectRatio: '16 / 9',
        border: 'none',
        display: 'block'
      }
    }) : isVideoSrc(lbImg.src, lbImg) ? React.createElement("video", {
      key: lbImg.src,
      src: lbImg.src,
      poster: lbImg.poster || undefined,
      controls: true,
      autoPlay: true,
      playsInline: true,
      style: {
        maxWidth: '100%',
        maxHeight: '100%',
        width: 'auto',
        height: 'auto',
        display: 'block',
        animation: 'lbFadeIn 0.22s ease-out'
      }
    }) : React.createElement("img", {
      key: lbImg.src,
      src: lbImg.src,
      alt: lbImg.caption || `Foto ${lightboxIndex + 1} de ${total}`,
      style: {
        maxWidth: '100%',
        maxHeight: '100%',
        width: 'auto',
        height: 'auto',
        objectFit: 'contain',
        display: 'block',
        animation: 'lbFadeIn 0.22s ease-out'
      }
    })), React.createElement("div", {"""
html = replace_n(old_2, new_2, 2, html)

# 3. Masonry thumbnail video/image block -> use YouTube thumbnail as poster image (appears twice)
old_3 = """      }, vid ? React.createElement(React.Fragment, null, React.createElement("video", {
        src: img.src,
        poster: img.poster || undefined,
        muted: true,
        playsInline: true,
        preload: "metadata"
      }), React.createElement(PlayGlyph, null)) : React.createElement("img", {
        src: img.src,
        loading: "lazy",
        alt: ""
      })));"""
new_3 = """      }, vid ? React.createElement(React.Fragment, null, getYouTubeId(img.src) ? React.createElement("img", {
        src: img.poster || `https://img.youtube.com/vi/${getYouTubeId(img.src)}/hqdefault.jpg`,
        loading: "lazy",
        alt: ""
      }) : React.createElement("video", {
        src: img.src,
        poster: img.poster || undefined,
        muted: true,
        playsInline: true,
        preload: "metadata"
      }), React.createElement(PlayGlyph, null)) : React.createElement("img", {
        src: img.src,
        loading: "lazy",
        alt: ""
      })));"""
html = replace_n(old_3, new_3, 2, html)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("OK: index.html patched")
