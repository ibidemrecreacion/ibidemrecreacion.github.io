import { DATA } from '../constants';
import { AppData, EventItem, Album } from '../types';

// Función robusta para parsear fechas en español
const parseDate = (dateStr: string): Date => {
  if (!dateStr) return new Date(0);
  try {
    const months: { [key: string]: number } = { "enero": 0, "febrero": 1, "marzo": 2, "abril": 3, "mayo": 4, "junio": 5, "julio": 6, "agosto": 7, "septiembre": 8, "octubre": 9, "noviembre": 10, "diciembre": 11 };
    
    // Limpieza agresiva: elimina 'de', comas y divide por cualquier cantidad de espacios en blanco
    const clean = dateStr.toLowerCase()
      .replace(/de /g, '')
      .replace(/,/g, '')
      .trim()
      .split(/\s+/); // Regex \s+ maneja múltiples espacios

    let m = -1, d = 1, y = new Date().getFullYear();

    clean.forEach(part => {
      if (months[part] !== undefined) {
        m = months[part];
      } else if (!isNaN(Number(part)) && part !== '') {
        const num = parseInt(part, 10);
        if (num > 31) y = num;
        else d = num;
      }
    });

    // Si falló el mes, devolvemos fecha época para que se vaya al final (o principio según sort)
    return m === -1 ? new Date(0) : new Date(y, m, d);
  } catch (e) {
    return new Date(0);
  }
};

export const getAppData = (): Promise<AppData> => {
  return new Promise((resolve) => {
    setTimeout(() => resolve(DATA), 100);
  });
};

export const getSortedEvents = (data: AppData) => {
  const allEvents = [...(data.fasti.upcoming || []), ...(data.fasti.past || [])];
  
  // Enriquecer eventos con imagen de portada si existe en álbumes
  const enriched = allEvents.map(evt => {
    const album = data.imagina ? data.imagina.find(a => a.id === evt.id) : null;
    let img = evt.coverImage;
    if (!img && album) img = album.coverImage || (album.images?.[0]?.src);
    return { ...evt, displayImage: img };
  });

  const now = new Date();
  now.setHours(0, 0, 0, 0);

  const future: EventItem[] = [];
  const past: EventItem[] = [];

  enriched.forEach(e => {
    const d = parseDate(e.date);
    // Comparación segura
    if (d.getTime() >= now.getTime()) future.push(e);
    else past.push(e);
  });

  // Ordenar Futuros: Ascendente (El más cercano a hoy primero)
  future.sort((a, b) => parseDate(a.date).getTime() - parseDate(b.date).getTime());
  
  // Ordenar Pasados: Descendente (El más reciente primero)
  past.sort((a, b) => parseDate(b.date).getTime() - parseDate(a.date).getTime());

  // Agrupar pasados por año
  const groupedPast: { [key: string]: EventItem[] } = {};
  past.forEach(e => {
    const d = parseDate(e.date);
    // Si la fecha es inválida (año 1970/1900), agrupar en "Antiguo" o el año que tenga
    const y = d.getFullYear() <= 1970 ? "Antiguo" : d.getFullYear().toString();
    
    if (!groupedPast[y]) groupedPast[y] = [];
    groupedPast[y].push(e);
  });

  return { future, groupedPast, years: Object.keys(groupedPast).sort((a, b) => Number(b) - Number(a)) };
};

export const getArticleById = (id: number) => {
  return DATA.tabularium.find(a => a.id === id);
};

export const getAlbumById = (id: number) => {
  return DATA.imagina.find(a => a.id === id);
};