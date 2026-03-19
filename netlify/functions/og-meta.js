// Netlify Function: og-meta.js
// Detecta bots de redes sociales y devuelve HTML con meta tags correctos
// para cada artículo del Tabularium.

const SITE_URL  = "https://ibidemrecreacion.netlify.app";
const SITE_NAME = "Ibidem Recreación Histórica";
const SITE_DESC = "Asociación dedicada a la reconstrucción minuciosa de la vida civil romana.";
const SITE_IMG  = "https://raw.githubusercontent.com/ibidemrecreacion/ibidemrecreacion.github.io/main/assets/img/General/Pepe_Larario.jpg";

const ARTICLES = {
  "5": {
    "title": "Llegas tarde a los idus de marzo",
    "summary": "Si planeas acudir al Foro el próximo 15 de marzo para conmemorar la muerte de César has de saber que llegarás tarde.",
    "img": "https://raw.githubusercontent.com/ibidemrecreacion/ibidemrecreacion.github.io/main/assets/img/Articulos/Idus_marzo/Idus_marzo.png"
  },
  "4": {
    "title": "¿Cuándo nació realmente la Navidad?",
    "summary": "Cada año, al encender las luces y adornar nuestros hogares en diciembre, se repite la misma historia: la Navidad no es más que una fiesta pagana reciclada, una ",
    "img": "https://www.walksinrome.com/uploads/2/5/1/0/25107996/adoration-of-the-three-magi-fresco-catacombs-of-priscilla-rome_orig.jpg"
  },
  "3": {
    "title": "Los Lares: guardianes del hogar romano",
    "summary": "Descubre cómo los romanos honraban diariamente a los espíritus protectores de su hogar a través de rituales que fortalecían los lazos familiares y aseguraban la",
    "img": "https://raw.githubusercontent.com/ibidemrecreacion/ibidemrecreacion.github.io/main/assets/img/tabularium/larario/Larario_Lararium.jpg"
  },
  "2": {
    "title": "La dieta de los gladiadores: 3 verdades sorprendentes que desafían el mito",
    "summary": "¿Héroes musculados o luchadores de sumo? Descubre la sorprendente realidad dietética de los gladiadores romanos: cebada, grasa y supervivencia.",
    "img": "https://placehold.co/1000x400/8B4513/F5EFE3?text=HOMBRES+DE+CEBADA"
  },
  "1": {
    "title": "El último viaje: el funus romano",
    "summary": "Para un romano, la muerte no era el final, sino la transición más crítica de su existencia. Descubre el ritual del funus.",
    "img": "https://placehold.co/1000x400/2A2A2A/F5EFE3?text=FUNUS+ROMANO"
  }
};

const BOT_AGENTS = [
  'facebookexternalhit','twitterbot','whatsapp','linkedinbot',
  'slackbot','telegrambot','discordbot','googlebot','bingbot','applebot',
];

const isBot = (ua = '') => {
  const lower = ua.toLowerCase();
  return BOT_AGENTS.some(b => lower.includes(b));
};

exports.handler = async (event) => {
  const ua   = (event.headers || {})['user-agent'] || '';
  const qs   = event.queryStringParameters || {};
  const hash = qs.hash || '';

  // Si no es bot, redirigir al sitio
  if (!isBot(ua)) {
    const dest = hash ? `/#${hash}` : '/';
    return { statusCode: 302, headers: { Location: dest }, body: '' };
  }

  let title = SITE_NAME;
  let desc  = SITE_DESC;
  let image = SITE_IMG;
  let url   = SITE_URL;

  const match = hash.match(/^article\?id=(\d+)/);
  if (match) {
    const art = ARTICLES[match[1]];
    if (art) {
      title = art.title + ' — ' + SITE_NAME;
      desc  = art.summary;
      image = art.img;
      url   = SITE_URL + '/#article?id=' + match[1];
    }
  }

  const esc = s => s.replace(/&/g,'&amp;').replace(/"/g,'&quot;');

  return {
    statusCode: 200,
    headers: { 'Content-Type': 'text/html; charset=utf-8' },
    body: `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>${esc(title)}</title>
  <meta name="description" content="${esc(desc)}">
  <meta property="og:type"         content="article">
  <meta property="og:url"          content="${url}">
  <meta property="og:title"        content="${esc(title)}">
  <meta property="og:description"  content="${esc(desc)}">
  <meta property="og:image"        content="${image}">
  <meta property="og:image:width"  content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name"    content="${SITE_NAME}">
  <meta property="twitter:card"        content="summary_large_image">
  <meta property="twitter:title"       content="${esc(title)}">
  <meta property="twitter:description" content="${esc(desc)}">
  <meta property="twitter:image"       content="${image}">
  <meta http-equiv="refresh" content="0; url=${url}">
</head>
<body><a href="${url}">${esc(title)}</a></body>
</html>`,
  };
};
