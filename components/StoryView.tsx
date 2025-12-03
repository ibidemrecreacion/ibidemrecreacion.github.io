import React from 'react';
import { Icons } from '../constants';
import { Link } from 'react-router-dom';

interface StoryItem {
  id: number;
  title: string;
  image: string;
  subtitle: string; // Date or Category
  description: string;
  linkTo: string;
  footerInfo?: string; // Location or Author
}

interface Props {
  items: StoryItem[];
}

export const StoryView: React.FC<Props> = ({ items }) => {
  const handleShare = async (e: React.MouseEvent, item: StoryItem) => {
    e.preventDefault();
    e.stopPropagation();
    if (navigator.share) {
      try {
        await navigator.share({
          title: item.title,
          text: item.description,
          url: window.location.href, // En una app real, esto sería la URL específica del item
        });
      } catch (err) {
        console.log('Error compartiendo', err);
      }
    } else {
      // Fallback simple: copiar al portapapeles
      navigator.clipboard.writeText(window.location.href);
      alert('Enlace copiado al portapapeles');
    }
  };

  if (items.length === 0) {
      return (
          <div className="flex items-center justify-center h-full w-full bg-pizarra/10 rounded-lg">
              <p className="font-cinzel text-gray-500">No hay contenido disponible</p>
          </div>
      )
  }

  return (
    /* h-full is critical here to fill the flex container from parent */
    <div className="flex overflow-x-auto snap-x snap-mandatory h-full w-full gap-0 no-scrollbar">
      {items.map((item) => (
        <div key={item.id} className="relative flex-shrink-0 w-full snap-center h-full bg-pizarra border-r border-white/10 overflow-hidden group">
          {/* Background Image */}
          <div className="absolute inset-0">
            <img 
                src={item.image} 
                alt={item.title} 
                className="w-full h-full object-cover opacity-80 transition-transform duration-[10s] ease-linear group-hover:scale-110"
                loading="lazy"
                onError={(e) => { e.currentTarget.src = "https://placehold.co/600x900/2A2A2A/F5EFE3?text=IBIDEM"; }}
            />
            {/* Gradient Overlay */}
            <div className="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
          </div>

          {/* Top Bar (Subtitle/Date + Share) */}
          <div className="absolute top-0 left-0 right-0 p-6 flex justify-between items-start pt-8">
             <span className="bg-pompeyano text-white text-xs font-bold px-4 py-1.5 rounded-full shadow-lg uppercase tracking-wider backdrop-blur-sm">
               {item.subtitle}
             </span>
             <button 
                onClick={(e) => handleShare(e, item)}
                className="bg-black/30 hover:bg-white/20 text-white p-2 rounded-full backdrop-blur-md transition-all active:scale-90"
                aria-label="Compartir"
             >
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/></svg>
             </button>
          </div>

          {/* Bottom Content */}
          <div className="absolute bottom-0 left-0 right-0 p-6 text-white pb-10 flex flex-col justify-end">
            <h3 className="font-cinzel text-2xl md:text-3xl font-bold mb-2 leading-tight drop-shadow-md text-pergamino">{item.title}</h3>
            
            {item.footerInfo && (
               <div className="flex items-center text-dorado-safe text-xs md:text-sm mb-3 font-bold">
                  <Icons.MapPin className="mr-1 w-4 h-4"/> <span className="uppercase tracking-wide">{item.footerInfo}</span>
               </div>
            )}

            <p className="text-gray-200 text-sm line-clamp-4 mb-5 leading-relaxed opacity-90 font-merriweather text-justify">
              {item.description}
            </p>

            <Link 
              to={item.linkTo} 
              className="inline-flex items-center justify-center w-full bg-dorado-safe/90 hover:bg-dorado text-white font-bold py-3.5 rounded-lg shadow-lg transition-colors uppercase tracking-widest text-xs backdrop-blur-sm border border-white/20 active:translate-y-0.5"
            >
              Ver Detalle
            </Link>
          </div>
        </div>
      ))}
    </div>
  );
};