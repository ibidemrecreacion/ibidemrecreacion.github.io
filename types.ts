export interface SocialLinks {
  email: string;
  facebook: string;
  instagram: string;
  logoUrl: string;
  heroImageHome: string;
}

export interface Pillar {
  title: string;
  text: string;
  linkTo: string;
}

export interface HomeData {
  heroTitle: string;
  intro: string;
  pilares: Pillar[];
}

export interface Founder {
  name: string;
  years: string;
  desc: string;
  image: string;
}

export interface NostriData {
  mainText: string;
  founder: Founder;
}

export interface Section {
  title: string;
  content: string;
  image?: string;
}

export interface Article {
  id: number;
  category: string;
  title: string;
  date: string;
  author: string;
  summary: string;
  img: string;
  intro: string;
  sections: Section[];
  bibliography: string[];
}

export interface Location {
  locality: string;
  place: string;
}

export interface EventItem {
  id: number;
  title: string;
  date: string;
  location: Location;
  desc: string;
  tags: string[];
  coverImage?: string;
  // Propiedad calculada para visualización
  displayImage?: string;
}

export interface AlbumImage {
  src: string;
  caption?: string;
}

export interface Album {
  id: number;
  eventTitle: string;
  date: string;
  location: Location;
  coverImage: string;
  images: AlbumImage[];
}

export interface GlossaryTerm {
  term: string;
  definition: string;
  category: 'Militar' | 'Civil' | 'Religioso' | 'General';
}

export interface AppData {
  general: SocialLinks;
  home: HomeData;
  nostri: NostriData;
  tabularium: Article[];
  fasti: {
    upcoming: EventItem[];
    past: EventItem[];
  };
  imagina: Album[];
  glossarium: GlossaryTerm[];
}