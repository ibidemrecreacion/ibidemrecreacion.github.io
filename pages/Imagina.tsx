import React, { useState, useMemo, useEffect } from 'react';
import { AppData, Album } from '../types';
import { SectionHeader } from '../components/SectionHeader';
import { Icons } from '../constants';
import { useParams, Link } from 'react-router-dom';

const AlbumDetail: React.FC<{ album: Album }> = ({ album }) => (
  <div className="animate-fade-in px-4">
    <Link to="/imagina" className="flex items-center text-pompeyano font-bold mb-6 hover:text-dorado-safe transition-colors w-fit">
      <Icons.ArrowLeft className="mr-2 w-5 h-5"/> Volver a Galerías
    </Link>
    <SectionHeader title={album.eventTitle} subtitle={album.date} />
    <div className="columns-1 md:columns-2 lg:columns-3 gap-4 space-y-4 max-w-7xl mx-auto pb-12">
      {album.images.map((img, i) => (
        <div key={i} className="break-inside-avoid rounded-lg overflow-hidden shadow-md hover:shadow-xl transition duration-300 bg-white">
          <img 
            src={img.src} 
            alt={img.caption || "Foto del evento"} 
            className="w-full h-auto" 
            loading="lazy" 
            onError={(e) => { e.currentTarget.src="https://placehold.co/400x300/F5EFE3/9A2A2A?text=ERROR"; }}
          />
          {img.caption && (
            <div className="p-3 bg-white text-xs text-center italic text-gray-600 border-t border-gray-100 font-merriweather">
              {img.caption}
            </div>
          )}
        </div>
      ))}
    </div>
  </div>
);

export const Imagina: React.FC<{ data: AppData }> = ({ data }) => {
  const { id } = useParams();
  
  // Merge explicit albums with events that have images but no explicit album entry
  const albums = useMemo(() => {
    const combined = [...(data.imagina || [])];
    const events = [...(data.fasti.upcoming || []), ...(data.fasti.past || [])];
    
    events.forEach(e => {
      // If event has images/cover but isn't already in albums list
      if (!combined.find(a => a.id === e.id) && (e.coverImage)) {
        combined.push({ 
          id: e.id, 
          eventTitle: e.title, 
          date: e.date, 
          location: e.location,
          coverImage: e.coverImage!, 
          images: e.coverImage ? [{ src: e.coverImage }] : [] 
        });
      }
    });
    // Simple date parse for sorting
    const parse = (d: string) => { try { return new Date(d) } catch { return new Date(0) } };
    return combined; // Assuming they are roughly sorted or relying on source order
  }, [data]);

  const selectedAlbum = id ? albums.find(a => a.id === Number(id)) : null;

  if (selectedAlbum) {
    return <AlbumDetail album={selectedAlbum} />;
  }

  return (
    <div className="animate-fade-in px-4 pb-12">
      <SectionHeader title="IMAGINA" subtitle="Galería" />
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-7xl mx-auto">
        {albums.map(alb => (
          <Link key={alb.id} to={`/imagina/${alb.id}`} className="block group bg-white rounded-lg overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1">
            <div className="h-64 overflow-hidden relative">
              <img 
                src={alb.coverImage} 
                className="w-full h-full object-cover transition duration-700 group-hover:scale-110" 
                alt={`Portada de ${alb.eventTitle}`} 
                loading="lazy"
                onError={(e) => { e.currentTarget.src="https://placehold.co/600x400/9A2A2A/B8860B?text=EVENTO"; }}
              />
              <div className="absolute inset-0 bg-pompeyano/40 opacity-0 group-hover:opacity-100 transition duration-300 flex items-center justify-center backdrop-blur-[2px]">
                <span className="text-white font-cinzel font-bold tracking-widest border-2 border-white px-4 py-2">VER FOTOS</span>
              </div>
            </div>
            <div className="p-5 text-center relative bg-white">
              <h3 className="font-cinzel text-lg font-bold text-pompeyano truncate px-2">{alb.eventTitle}</h3>
              <p className="text-xs text-gray-500 mt-2 font-merriweather italic">{alb.date} • {alb.images?.length || 0} Fotos</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};