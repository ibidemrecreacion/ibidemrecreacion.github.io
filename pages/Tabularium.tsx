import React, { useState } from 'react';
import { DATA } from '../constants';
import { SectionHeader } from '../components/SectionHeader';
import { Icons } from '../constants';
import { StoryView } from '../components/StoryView';
import { Link } from 'react-router-dom';

// Mini Footer for Mobile Views (Reused)
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

export const Tabularium: React.FC = () => {
    const [filter, setFilter] = useState('TODOS');
    const filtered = DATA.tabularium.filter(a => filter === 'TODOS' || a.category === filter);
    const cats = ['TODOS', ...Array.from(new Set(DATA.tabularium.map(a => a.category)))];

    const storyItems = filtered.map(a => ({
        id: a.id,
        title: a.title,
        image: a.img,
        subtitle: a.category,
        description: a.summary,
        linkTo: `/tabularium/${a.id}`,
        footerInfo: a.author
    }));

    return (
        <>
            {/* MOBILE LAYOUT (Full Viewport Height, No Scroll) */}
            {/* Height calculation matches App padding (7rem) */}
            <div className="md:hidden flex flex-col h-[calc(100dvh-7rem)] w-full">
                 {/* 1. Header & Filters Fijos */}
                 <div className="flex-none px-4 pt-4 pb-2 bg-pergamino z-10 shadow-sm border-b border-dorado/20">
                    <div className="flex justify-between items-center mb-3">
                        <h2 className="font-cinzel text-2xl font-bold text-pompeyano tracking-wider">TABULARIUM</h2>
                        <span className="text-[10px] font-bold text-gray-500 uppercase tracking-widest bg-gray-100 px-2 py-1 rounded">
                            {filtered.length} ARTÍCULOS
                        </span>
                    </div>
                    {/* Horizontal scrollable filters */}
                    <div className="flex overflow-x-auto gap-2 pb-2 no-scrollbar">
                        {cats.map(c => (
                            <button 
                                key={c} 
                                onClick={() => setFilter(c)} 
                                className={`flex-shrink-0 px-3 py-1.5 rounded-full font-cinzel text-[10px] font-bold tracking-wider border transition whitespace-nowrap ${filter===c ? 'bg-pompeyano text-white border-pompeyano shadow' : 'bg-white text-gray-500 border-gray-300'}`}
                            >
                                {c.toUpperCase()}
                            </button>
                        ))}
                    </div>
                 </div>

                 {/* 2. Content Flexible */}
                 <div className="flex-grow overflow-hidden relative w-full bg-pizarra">
                     <StoryView items={storyItems} />
                 </div>

                 {/* 3. Footer Fijo */}
                 <MobileFooter />
            </div>

            {/* DESKTOP LAYOUT */}
            <div className="hidden md:block animate-fade-in px-4 pt-8 pb-12">
                <SectionHeader title="TABULARIUM" subtitle="Archivo" />
                <div className="flex justify-center flex-wrap gap-2 mb-10">
                    {cats.map(c => (
                        <button key={c} onClick={() => setFilter(c)} className={`px-4 py-1 rounded-full font-cinzel text-xs font-bold tracking-wider border transition ${filter===c ? 'bg-pompeyano text-white border-pompeyano' : 'bg-white text-gray-500 border-gray-300 hover:border-pompeyano'}`}>
                            {c.toUpperCase()}
                        </button>
                    ))}
                </div>
                <div className="grid md:grid-cols-2 gap-8 max-w-6xl mx-auto">
                    {filtered.map(art => (
                        <div key={art.id} className="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-2xl transition flex flex-col group">
                            <div className="h-48 overflow-hidden"><img src={art.img} className="w-full h-full object-cover group-hover:scale-105 transition duration-700" loading="lazy" onError={(e) => { e.currentTarget.src="https://placehold.co/600x400/2A2A2A/F5EFE3?text=IMAGEN+NO+DISPONIBLE"; }}/></div>
                            <div className="p-6 flex flex-col flex-grow">
                                <span className="text-xs font-cinzel text-dorado-safe uppercase mb-2">{art.category}</span>
                                <h3 className="font-cinzel text-xl font-bold mb-3">{art.title}</h3>
                                <p className="text-gray-600 text-sm mb-4 line-clamp-3 flex-grow">{art.summary}</p>
                                <Link to={`/tabularium/${art.id}`} className="text-pompeyano font-bold text-sm hover:text-dorado-safe flex items-center mt-auto self-start">
                                    Leer más <Icons.ChevronRight className="w-4 h-4 ml-1"/>
                                </Link>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </>
    );
};