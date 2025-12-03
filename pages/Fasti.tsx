import React, { useMemo, useState } from 'react';
import { AppData, EventItem } from '../types';
import { getSortedEvents } from '../services/dataService';
import { SectionHeader } from '../components/SectionHeader';
import { Icons, DATA } from '../constants';
import { Link } from 'react-router-dom';
import { StoryView } from '../components/StoryView';

// Mini Footer for Mobile Views
const MobileFooter = () => (
    <div className="flex-none bg-pizarra text-pergamino py-3 border-t-2 border-dorado flex flex-col items-center justify-center z-20 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.1)]">
        <div className="flex gap-6 mb-1">
             <a href={DATA.general.facebook} target="_blank" rel="noreferrer"><Icons.Facebook className="w-5 h-5 text-pergamino" /></a>
             <a href={DATA.general.instagram} target="_blank" rel="noreferrer"><Icons.Instagram className="w-5 h-5 text-pergamino" /></a>
             <a href={`mailto:${DATA.general.email}`}><Icons.Mail className="w-5 h-5 text-pergamino" /></a>
        </div>
        <p className="font-cinzel text-[9px] text-gray-500 tracking-widest">&copy; {new Date().getFullYear()} IBIDEM</p>
    </div>
);

const EventCardDesktop: React.FC<{ event: EventItem; isFuture?: boolean }> = ({ event, isFuture }) => (
  <Link 
    to={`/imagina/${event.id}`} 
    className={`block bg-white rounded-lg overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 group h-full flex flex-col ${isFuture ? 'border-t-4 border-pompeyano transform hover:-translate-y-1' : 'border-l-4 border-dorado'}`}
  >
    <div className="h-48 overflow-hidden relative bg-gray-100">
      <img 
        src={event.displayImage || "https://placehold.co/600x400/9A2A2A/B8860B?text=SPQR"} 
        alt={event.title} 
        className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" 
        loading="lazy"
      />
      <div className="absolute inset-0 bg-pompeyano/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
        <span className="text-white font-cinzel font-bold tracking-widest text-sm border border-white px-3 py-1 rounded">VER DETALLE</span>
      </div>
    </div>
    <div className="p-5 flex-grow flex flex-col">
      <div className="flex items-center gap-2 mb-2">
        <span className={`text-[10px] font-bold px-2 py-0.5 rounded uppercase ${isFuture ? 'bg-pompeyano text-white' : 'bg-gray-200 text-gray-600'}`}>
          {isFuture ? 'PRÓXIMO' : event.date}
        </span>
      </div>
      <h3 className="font-cinzel text-xl font-bold text-pizarra mb-2 leading-tight group-hover:text-pompeyano transition-colors">{event.title}</h3>
      <div className="flex items-center text-gray-500 text-sm mb-3">
        <Icons.MapPin className="mr-1 text-dorado-safe w-4 h-4"/> {event.location.locality}
      </div>
      <p className="text-gray-700 text-sm leading-relaxed mb-4 line-clamp-3">{event.desc}</p>
    </div>
  </Link>
);

export const Fasti: React.FC<{ data: AppData }> = ({ data }) => {
  const { future, groupedPast, years } = useMemo(() => getSortedEvents(data), [data]);
  const [activeTab, setActiveTab] = useState<'future' | 'past'>('future');

  const mapToStory = (e: EventItem) => ({
    id: e.id,
    title: e.title,
    image: e.displayImage || "https://placehold.co/600x900/9A2A2A/F5EFE3?text=SPQR",
    subtitle: e.date,
    description: e.desc,
    linkTo: `/imagina/${e.id}`,
    footerInfo: e.location.locality
  });

  const futureStories = future.map(mapToStory);
  const pastStories = years.flatMap(y => groupedPast[y]).map(mapToStory);

  return (
    <>
        {/* MOBILE LAYOUT (Full Viewport Height, No Scroll) */}
        {/* Container height is Viewport - 7rem (Navbar padding). Starts exactly below Navbar. */}
        <div className="md:hidden flex flex-col h-[calc(100dvh-7rem)] w-full">
            
            {/* 1. Header Fijo (Título + Pestañas) */}
            <div className="flex-none px-4 pt-4 pb-3 bg-pergamino z-10 shadow-sm border-b border-dorado/20">
                <div className="flex justify-between items-center mb-3">
                    <h2 className="font-cinzel text-2xl font-bold text-pompeyano tracking-wider">FASTI</h2>
                    <span className="text-[10px] font-bold text-gray-500 uppercase tracking-widest bg-gray-100 px-2 py-1 rounded">
                        {activeTab === 'future' ? future.length : pastStories.length} EVENTOS
                    </span>
                </div>
                <div className="flex bg-gray-200 rounded-lg p-1">
                    <button 
                        onClick={() => setActiveTab('future')}
                        className={`flex-1 py-1.5 text-xs font-bold font-cinzel rounded-md transition-all ${activeTab === 'future' ? 'bg-white text-pompeyano shadow' : 'text-gray-500 hover:text-gray-700'}`}
                    >
                        PRÓXIMOS
                    </button>
                    <button 
                         onClick={() => setActiveTab('past')}
                         className={`flex-1 py-1.5 text-xs font-bold font-cinzel rounded-md transition-all ${activeTab === 'past' ? 'bg-white text-pompeyano shadow' : 'text-gray-500 hover:text-gray-700'}`}
                    >
                        ANTERIORES
                    </button>
                </div>
            </div>

            {/* 2. Contenido Flexible (Ocupa el resto del espacio) */}
            <div className="flex-grow overflow-hidden relative w-full bg-pizarra">
                {activeTab === 'future' ? (
                     <StoryView items={futureStories} />
                ) : (
                     <StoryView items={pastStories} />
                )}
            </div>

            {/* 3. Footer Fijo (Integrado) */}
            <MobileFooter />
        </div>

        {/* DESKTOP LAYOUT (Original) */}
        <div className="hidden md:block animate-fade-in pb-12 pt-8">
            <SectionHeader title="FASTI" subtitle="Calendario" />
            
            {/* Future */}
            {future.length > 0 && (
                <div className="max-w-6xl mx-auto px-4 mb-20">
                    <div className="flex items-center mb-8 border-b border-gray-300 pb-2">
                        <Icons.Calendar className="text-pompeyano w-6 h-6 mr-3"/>
                        <h3 className="font-cinzel text-2xl font-bold text-pompeyano">Proxima Eventa</h3>
                    </div>
                    <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                        {future.map(e => <EventCardDesktop key={e.id} event={e} isFuture={true} />)}
                    </div>
                </div>
            )}

            {/* Past */}
            <div className="max-w-5xl mx-auto px-4 relative mt-12">
                <div className="text-center mb-12">
                    <h3 className="font-cinzel text-2xl font-bold text-pizarra inline-block border-b-2 border-dorado pb-1">Acta Praeterita</h3>
                </div>
                <div className="absolute left-1/2 top-20 bottom-0 w-0.5 bg-gray-300 transform -translate-x-1/2"></div>
                <div className="space-y-16">
                    {years.map(year => (
                        <div key={year} className="relative">
                            <div className="flex justify-center mb-8 relative z-10">
                                <span className="bg-pizarra text-pergamino font-cinzel font-bold text-xl px-4 py-1 rounded shadow-lg border-2 border-dorado">{year}</span>
                            </div>
                            <div className="relative space-y-12">
                                {groupedPast[year].map((evt, idx) => (
                                    <div key={evt.id} className={`flex items-center justify-between w-full ${idx % 2 === 0 ? 'flex-row-reverse' : ''}`}>
                                        <div className="w-5/12"></div>
                                        <div className="absolute left-1/2 w-4 h-4 bg-pompeyano border-2 border-white rounded-full shadow transform -translate-x-1/2 z-10"></div>
                                        <div className="w-5/12 relative">
                                            <EventCardDesktop event={evt} isFuture={false} />
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    </>
  );
};