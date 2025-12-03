import React, { useState } from 'react';
import { DATA } from '../constants';
import { SectionHeader } from '../components/SectionHeader';
import { Icons } from '../constants';

export const Glossarium: React.FC = () => {
  const [search, setSearch] = useState('');
  const [filter, setFilter] = useState('TODOS');

  const terms = DATA.glossarium.filter(t => {
    const matchesSearch = t.term.toLowerCase().includes(search.toLowerCase()) || t.definition.toLowerCase().includes(search.toLowerCase());
    const matchesFilter = filter === 'TODOS' || t.category === filter;
    return matchesSearch && matchesFilter;
  });

  const categories = ['TODOS', ...Array.from(new Set(DATA.glossarium.map(t => t.category)))];

  // Ordenar alfabéticamente
  terms.sort((a, b) => a.term.localeCompare(b.term));

  return (
    <div className="max-w-4xl mx-auto px-4 animate-fade-in pt-8 pb-20">
      <SectionHeader title="GLOSSARIUM" subtitle="Diccionario" />

      {/* Search & Filter Bar */}
      <div className="bg-white p-4 rounded-lg shadow-lg mb-10 sticky top-32 z-30 border border-dorado/20">
        <div className="flex flex-col md:flex-row gap-4">
          <div className="relative flex-grow">
            <input 
              type="text" 
              placeholder="Buscar término..." 
              className="w-full pl-10 pr-4 py-2 border rounded-full focus:outline-none focus:ring-2 focus:ring-pompeyano bg-gray-50"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />
            <Icons.Search className="absolute left-3 top-2.5 text-gray-400 w-5 h-5"/>
          </div>
          <div className="flex overflow-x-auto gap-2 no-scrollbar md:flex-wrap">
            {categories.map(cat => (
              <button 
                key={cat}
                onClick={() => setFilter(cat)}
                className={`px-4 py-2 rounded-full text-xs font-bold font-cinzel transition whitespace-nowrap ${filter === cat ? 'bg-pompeyano text-white shadow-md' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'}`}
              >
                {cat.toUpperCase()}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Terms List */}
      <div className="grid gap-6">
        {terms.length > 0 ? (
          terms.map((item, idx) => (
            <div key={idx} className="bg-white p-6 rounded-lg shadow border-l-4 border-dorado hover:shadow-lg transition duration-300">
              <div className="flex justify-between items-start mb-2">
                <h3 className="font-cinzel text-2xl font-bold text-pompeyano">{item.term}</h3>
                <span className="text-[10px] uppercase tracking-widest bg-gray-100 text-gray-500 px-2 py-1 rounded border">
                  {item.category}
                </span>
              </div>
              <p className="text-gray-700 font-merriweather leading-relaxed text-justify">
                {item.definition}
              </p>
            </div>
          ))
        ) : (
          <div className="text-center py-10 opacity-60">
            <Icons.Book className="w-16 h-16 mx-auto mb-4 text-gray-300"/>
            <p className="font-cinzel text-xl text-gray-500">No se encontraron términos.</p>
          </div>
        )}
      </div>
    </div>
  );
};