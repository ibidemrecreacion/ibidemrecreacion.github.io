#!/usr/bin/env python3
"""
add_event_schema.py
Inserta JSON-LD schema.org/Event dinámico en:
  1. PageActivityDetail (ficha de actividad) — un Event por cada
     ocurrencia histórica/futura de la actividad.
  2. PageFasti (listado Eventa) — un ItemList de Event solo para las
     próximas convocatorias.
"""

import re, subprocess, sys, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
PATH = os.path.normpath(PATH)

with open(PATH, encoding='utf-8') as f:
    html = f.read()

# ─── 1. PageActivityDetail: schema-event por ficha de actividad ──────────────

old_1 = """  const relatedArticles = useMemo(() => {
    if (!data.tabularium) return [];
    const keywords = decodedTitle.split(/[:\\s]+/).filter(w => w.length > 3).map(normalizeLatin);
    return data.tabularium.filter(art => keywords.some(k => normalizeLatin(art.title).includes(k))).slice(0, 2);
  }, [data, decodedTitle]);
  if (activityData.length === 0) {"""

assert html.count(old_1) == 1, f"old_1 no es único (encontrado {html.count(old_1)} veces)"

new_1 = """  const relatedArticles = useMemo(() => {
    if (!data.tabularium) return [];
    const keywords = decodedTitle.split(/[:\\s]+/).filter(w => w.length > 3).map(normalizeLatin);
    return data.tabularium.filter(art => keywords.some(k => normalizeLatin(art.title).includes(k))).slice(0, 2);
  }, [data, decodedTitle]);
  useEffect(() => {
    const existing = document.getElementById('schema-event');
    if (existing) existing.remove();
    if (activityData.length > 0) {
      const toISODate = d => {
        const dt = parseDate(d);
        if (!dt || dt.getTime() === 0) return undefined;
        const y = dt.getFullYear();
        const m = String(dt.getMonth() + 1).padStart(2, '0');
        const day = String(dt.getDate()).padStart(2, '0');
        return `${y}-${m}-${day}`;
      };
      const baseDesc = (EXTENDED_DESCRIPTIONS[decodedTitle] || activityData[0].desc || decodedTitle).replace(/[*_#]/g, '').slice(0, 300);
      const events = activityData.map(evt => {
        const iso = toISODate(evt.date);
        if (!iso) return null;
        const loc = evt.location || {};
        const album = data.imagina ? data.imagina.find(a => a.id === evt.id) : null;
        const ev = {
          "@type": "Event",
          "name": evt.title || evt.eventTitle || decodedTitle,
          "startDate": iso,
          "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
          "eventStatus": "https://schema.org/EventScheduled",
          "location": {
            "@type": "Place",
            "name": loc.place || loc.locality || "Andalucía",
            "address": {
              "@type": "PostalAddress",
              "addressLocality": loc.locality || "",
              "addressCountry": "ES"
            }
          },
          "description": ((evt.desc || baseDesc || '').replace(/[*_#]/g, '') || decodedTitle).slice(0, 300),
          "organizer": {
            "@type": "Organization",
            "name": "Ibidem Recreación Histórica",
            "url": "https://ibidemrecreacion.es"
          },
          "url": `${window.location.origin}/activity/${encodeURIComponent(decodedTitle)}`
        };
        if (album && album.coverImage) ev.image = album.coverImage;
        return ev;
      }).filter(Boolean);
      if (events.length) {
        const schema = events.length === 1
          ? Object.assign({ "@context": "https://schema.org" }, events[0])
          : { "@context": "https://schema.org", "@graph": events };
        const tag = document.createElement('script');
        tag.id = 'schema-event';
        tag.type = 'application/ld+json';
        tag.textContent = JSON.stringify(schema);
        document.head.appendChild(tag);
      }
    }
    return () => {
      const el = document.getElementById('schema-event');
      if (el) el.remove();
    };
  }, [activityData, decodedTitle, data]);
  if (activityData.length === 0) {"""

html = html.replace(old_1, new_1, 1)

# ─── 2. PageFasti: ItemList de próximas convocatorias ─────────────────────────

old_2 = """  }, [data]);
  const tagOptions = TEMATICA_OPTIONS;
  const formatOptions = FORMATO_OPTIONS;"""

assert html.count(old_2) == 1, f"old_2 no es único (encontrado {html.count(old_2)} veces)"

new_2 = """  }, [data]);
  useEffect(() => {
    const existing = document.getElementById('schema-events-list');
    if (existing) existing.remove();
    if (upcoming.length > 0) {
      const toISODate = d => {
        const dt = parseDate(d);
        if (!dt || dt.getTime() === 0) return undefined;
        const y = dt.getFullYear();
        const m = String(dt.getMonth() + 1).padStart(2, '0');
        const day = String(dt.getDate()).padStart(2, '0');
        return `${y}-${m}-${day}`;
      };
      const items = upcoming.map((g, i) => {
        const iso = toISODate(g.lastEvent && g.lastEvent.date);
        if (!iso) return null;
        const loc = (g.lastEvent && g.lastEvent.location) || {};
        return {
          "@type": "ListItem",
          "position": i + 1,
          "item": {
            "@type": "Event",
            "name": g.titulo,
            "startDate": iso,
            "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
            "eventStatus": "https://schema.org/EventScheduled",
            "location": {
              "@type": "Place",
              "name": loc.place || loc.locality || "Andalucía",
              "address": {
                "@type": "PostalAddress",
                "addressLocality": loc.locality || "",
                "addressCountry": "ES"
              }
            },
            "description": (g.descripcion || g.titulo || '').replace(/[*_#]/g, '').slice(0, 300),
            "organizer": {
              "@type": "Organization",
              "name": "Ibidem Recreación Histórica",
              "url": "https://ibidemrecreacion.es"
            },
            "url": `${window.location.origin}/activity/${encodeURIComponent(g.titulo)}`
          }
        };
      }).filter(Boolean);
      if (items.length) {
        const schema = {
          "@context": "https://schema.org",
          "@type": "ItemList",
          "itemListElement": items
        };
        const tag = document.createElement('script');
        tag.id = 'schema-events-list';
        tag.type = 'application/ld+json';
        tag.textContent = JSON.stringify(schema);
        document.head.appendChild(tag);
      }
    }
    return () => {
      const el = document.getElementById('schema-events-list');
      if (el) el.remove();
    };
  }, [upcoming]);
  const tagOptions = TEMATICA_OPTIONS;
  const formatOptions = FORMATO_OPTIONS;"""

html = html.replace(old_2, new_2, 1)

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print("OK — schema Event insertado en PageActivityDetail y PageFasti.")
