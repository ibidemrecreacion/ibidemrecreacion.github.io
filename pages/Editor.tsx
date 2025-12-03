import React, { useState } from 'react';
import { SectionHeader } from '../components/SectionHeader';

export const Editor: React.FC = () => {
  const [type, setType] = useState<'event' | 'article'>('event');
  
  // Form States
  const [title, setTitle] = useState('');
  const [date, setDate] = useState('');
  const [desc, setDesc] = useState('');
  const [locality, setLocality] = useState('');
  const [image, setImage] = useState('');
  const [generatedJson, setGeneratedJson] = useState('');

  const generate = () => {
    let obj: any = {};
    const id = Math.floor(Math.random() * 10000);

    if (type === 'event') {
      obj = {
        id,
        title,
        date, // User should input "1 de noviembre, 2025"
        location: { locality, place: "Lugar del evento" },
        desc,
        tags: ["Nuevo"],
        coverImage: image
      };
    } else {
      obj = {
        id,
        category: "Vida Cotidiana",
        title,
        date,
        author: "Ibidem",
        summary: desc,
        img: image,
        intro: desc,
        sections: [{ title: "Sección 1", content: "Contenido..." }],
        bibliography: []
      };
    }

    setGeneratedJson(JSON.stringify(obj, null, 2));
  };

  return (
    <div className="max-w-3xl mx-auto px-4 animate-fade-in">
      <SectionHeader title="EDITOR" subtitle="Gestor de Contenido" />
      
      <div className="bg-white p-6 rounded-lg shadow-lg mb-8">
        <p className="text-sm text-gray-500 mb-4 italic">
          Nota: Al ser una web estática, este editor genera el código que debes copiar y pegar en el archivo <strong>constants.tsx</strong> o enviarlo al desarrollador.
        </p>

        <div className="flex gap-4 mb-6">
          <button 
            onClick={() => setType('event')} 
            className={`px-4 py-2 rounded font-bold ${type === 'event' ? 'bg-pompeyano text-white' : 'bg-gray-200'}`}
          >
            Nuevo Evento
          </button>
          <button 
            onClick={() => setType('article')} 
            className={`px-4 py-2 rounded font-bold ${type === 'article' ? 'bg-pompeyano text-white' : 'bg-gray-200'}`}
          >
            Nuevo Artículo
          </button>
        </div>

        <div className="space-y-4">
          <div>
            <label className="block text-sm font-bold mb-1">Título</label>
            <input className="w-full border p-2 rounded" value={title} onChange={e => setTitle(e.target.value)} placeholder="Ej. Fvnvs: El último viaje" />
          </div>
          <div>
            <label className="block text-sm font-bold mb-1">Fecha (Texto)</label>
            <input className="w-full border p-2 rounded" value={date} onChange={e => setDate(e.target.value)} placeholder="Ej. 1 de noviembre, 2025" />
          </div>
          <div>
            <label className="block text-sm font-bold mb-1">Localidad / Categoría</label>
            <input className="w-full border p-2 rounded" value={locality} onChange={e => setLocality(e.target.value)} placeholder={type === 'event' ? "Ej. Mérida (Badajoz)" : "Ej. Ritos"} />
          </div>
          <div>
            <label className="block text-sm font-bold mb-1">URL Imagen</label>
            <input className="w-full border p-2 rounded" value={image} onChange={e => setImage(e.target.value)} placeholder="https://..." />
          </div>
          <div>
            <label className="block text-sm font-bold mb-1">Descripción / Resumen</label>
            <textarea className="w-full border p-2 rounded h-24" value={desc} onChange={e => setDesc(e.target.value)} placeholder="Descripción del contenido..." />
          </div>

          <button onClick={generate} className="w-full bg-dorado-safe text-white font-cinzel font-bold py-3 rounded hover:bg-dorado transition">
            GENERAR CÓDIGO JSON
          </button>
        </div>
      </div>

      {generatedJson && (
        <div className="bg-pizarra text-green-400 p-6 rounded-lg shadow-inner overflow-x-auto relative">
          <h3 className="text-white font-bold mb-2">Copia este código:</h3>
          <pre className="text-xs">{generatedJson}</pre>
          <button 
            onClick={() => navigator.clipboard.writeText(generatedJson)} 
            className="absolute top-4 right-4 bg-white/20 hover:bg-white/40 text-white text-xs px-2 py-1 rounded"
          >
            COPIAR
          </button>
        </div>
      )}
    </div>
  );
};