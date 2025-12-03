import React from 'react';
import { HomeData } from '../types';
import { SectionHeader } from '../components/SectionHeader';
import { Link } from 'react-router-dom';
import { Icons } from '../constants';

interface Props {
  data: HomeData;
  heroImage: string;
}

export const Home: React.FC<Props> = ({ data, heroImage }) => {
  return (
    <div className="animate-fade-in-up">
      {/* Hero Section */}
      <section className="relative h-[60vh] md:h-[70vh] w-full bg-cover bg-center rounded-xl overflow-hidden shadow-2xl mb-16 group mx-auto max-w-7xl" style={{ backgroundImage: `url(${heroImage})` }}>
        <div className="absolute inset-0 bg-gradient-to-t from-pizarra/90 via-transparent to-transparent"></div>
        <div className="absolute bottom-6 left-6 md:bottom-16 md:left-16 max-w-3xl">
          <h1 className="font-merriweather text-xl md:text-3xl italic text-pergamino leading-relaxed border-l-4 border-dorado pl-6 shadow-black drop-shadow-lg">
            {data.heroTitle}
          </h1>
        </div>
      </section>
      
      {/* Intro */}
      <section className="max-w-4xl mx-auto text-center mb-20 px-4">
        <p className="text-lg md:text-2xl text-pizarra leading-relaxed font-light font-merriweather">{data.intro}</p>
      </section>
      
      {/* Pillars */}
      <SectionHeader title="NOSTRA FUNDAMENTA" subtitle="Nuestros Pilares" />
      <div className="grid md:grid-cols-3 gap-8 mb-20 px-4 max-w-7xl mx-auto">
        {data.pilares.map((pilar, index) => (
          <article key={index} className="bg-white p-8 rounded-lg shadow-lg border-t-4 border-dorado hover:-translate-y-2 transition-transform duration-300 flex flex-col">
            <h3 className="font-cinzel text-xl font-bold text-pompeyano mb-4">{pilar.title}</h3>
            <p className="text-gray-700 mb-6 flex-grow leading-relaxed">{pilar.text}</p>
            <Link to={`/${pilar.linkTo}`} className="text-dorado-safe font-bold text-xs uppercase tracking-widest hover:text-pompeyano flex items-center gap-2 group">
              Saber más <Icons.ChevronRight className="w-4 h-4 transition-transform group-hover:translate-x-1" />
            </Link>
          </article>
        ))}
      </div>
    </div>
  );
};