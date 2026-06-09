/* sw.js — Ibidem Recreación Histórica
   Estrategia:
   · Cache-first  → assets estáticos (fuentes, imágenes del repo, iconos PWA)
   · Network-first → index.html y datos.json (contenido que se actualiza)
   · Fallback     → index.html cacheado si no hay red
*/

const CACHE_VERSION = 'ibidem-v1';

const PRECACHE = [
  '/',
  '/datos.json',
  '/manifest.json',
  '/assets/pwa/icon-192.png',
  '/assets/pwa/icon-512.png'
];

const CACHE_FIRST_ORIGINS = [
  'fonts.googleapis.com',
  'fonts.gstatic.com',
  'cdn.tailwindcss.com',
  'unpkg.com',
  'raw.githubusercontent.com'
];

// ── Instalación: pre-cachear recursos críticos ────────────────────────────────
self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_VERSION).then(cache =>
      cache.addAll(PRECACHE).catch(() => {/* ignora si alguno falla en dev */})
    )
  );
});

// ── Activación: limpiar cachés de versiones anteriores ───────────────────────
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys
          .filter(k => k !== CACHE_VERSION)
          .map(k => caches.delete(k))
      )
    ).then(() => self.clients.claim())
  );
});

// ── Fetch: lógica por tipo de recurso ────────────────────────────────────────
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);

  // Solo interceptar GET
  if (request.method !== 'GET') return;

  // Assets externos (fuentes, CDN, imágenes del repo) → cache-first
  if (CACHE_FIRST_ORIGINS.some(origin => url.hostname.includes(origin))) {
    event.respondWith(cacheFirst(request));
    return;
  }

  // Mismo origen: index.html y datos.json → network-first con fallback
  if (url.origin === self.location.origin) {
    event.respondWith(networkFirstWithFallback(request));
    return;
  }
});

// ── Estrategias ───────────────────────────────────────────────────────────────
async function cacheFirst(request) {
  const cached = await caches.match(request);
  if (cached) return cached;
  try {
    const response = await fetch(request);
    if (response.ok) {
      const cache = await caches.open(CACHE_VERSION);
      cache.put(request, response.clone());
    }
    return response;
  } catch {
    return new Response('', { status: 503, statusText: 'Sin conexión' });
  }
}

async function networkFirstWithFallback(request) {
  try {
    const response = await fetch(request);
    if (response.ok) {
      const cache = await caches.open(CACHE_VERSION);
      cache.put(request, response.clone());
    }
    return response;
  } catch {
    const cached = await caches.match(request);
    if (cached) return cached;
    // Si piden cualquier ruta del SPA, servir index.html cacheado
    const fallback = await caches.match('/');
    return fallback || new Response('Sin conexión', { status: 503 });
  }
}
