/**
 * Netlify Edge Function — OG meta tags dinámicos por artículo
 *
 * Cómo funciona:
 *  1. Solo actúa cuando el User-Agent pertenece a un crawler de redes sociales.
 *  2. Extrae el id del artículo de la URL (/article/:id).
 *  3. Obtiene datos.json desde el propio origen.
 *  4. Devuelve un HTML mínimo con los meta tags correctos + refresh al SPA.
 *  5. Cualquier otro visitante pasa directamente al SPA sin modificación.
 */

const CRAWLER_RE =
  /facebookexternalhit|facebot|twitterbot|linkedinbot|whatsapp|telegrambot|slackbot|discordbot|applebot|googlebot|bingbot/i;

export default async (request, context) => {
  // ── 1. ¿Es un bot de red social? ────────────────────────────────────────
  const ua = request.headers.get("user-agent") || "";
  if (!CRAWLER_RE.test(ua)) return context.next();

  // ── 2. ¿Es una URL de artículo? ──────────────────────────────────────────
  const url = new URL(request.url);
  const match = url.pathname.match(/^\/article\/(\d+)\/?$/);
  if (!match) return context.next();

  const articleId = parseInt(match[1], 10);

  // ── 3. Leer datos.json ───────────────────────────────────────────────────
  let article;
  try {
    const res = await fetch(`${url.origin}/datos.json`);
    if (!res.ok) return context.next();
    const data = await res.json();
    article = data.tabularium.find((a) => a.id === articleId);
  } catch {
    return context.next();
  }

  if (!article) return context.next();

  // ── 4. Construir meta tags ────────────────────────────────────────────────
  const siteUrl   = "https://ibidemrecreacion.netlify.app";
  const canonical = `${siteUrl}/article/${articleId}`;
  const title     = `${article.title} — Ibidem Recreación Histórica`;
  const desc      = (article.summary || article.intro || "")
    .replace(/<[^>]*>/g, "")   // quitar HTML del intro si lo hubiera
    .substring(0, 200)
    .replace(/"/g, "&quot;");
  const image     = article.img || `${siteUrl}/assets/img/General/Pepe_Larario.jpg`;
  const safeTitle = title.replace(/"/g, "&quot;");

  // ── 5. Devolver HTML mínimo con OG + refresh al SPA ──────────────────────
  const html = `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>${safeTitle}</title>
  <meta name="description" content="${desc}">

  <!-- Open Graph -->
  <meta property="og:type"        content="article">
  <meta property="og:url"         content="${canonical}">
  <meta property="og:title"       content="${safeTitle}">
  <meta property="og:description" content="${desc}">
  <meta property="og:image"       content="${image}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height"content="630">
  <meta property="og:site_name"   content="Ibidem Recreación Histórica">

  <!-- Twitter / X -->
  <meta name="twitter:card"        content="summary_large_image">
  <meta name="twitter:url"         content="${canonical}">
  <meta name="twitter:title"       content="${safeTitle}">
  <meta name="twitter:description" content="${desc}">
  <meta name="twitter:image"       content="${image}">

  <!-- Redirige al SPA para usuarios reales que lleguen sin JS -->
  <meta http-equiv="refresh" content="0; url=${canonical}">
  <link rel="canonical" href="${canonical}">
</head>
<body></body>
</html>`;

  return new Response(html, {
    status: 200,
    headers: { "content-type": "text/html; charset=utf-8" },
  });
};

// Declara la ruta que activa esta función
export const config = { path: "/article/*" };
