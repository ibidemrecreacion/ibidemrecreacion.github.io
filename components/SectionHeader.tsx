import React from 'react';

interface Props {
  title: string;
  subtitle?: string;
  className?: string;
}

export const SectionHeader: React.FC<Props> = ({ title, subtitle, className = "" }) => (
  <div className={`text-center mb-12 md:mb-16 pt-8 animate-fade-in ${className}`}>
    {subtitle && (
      <span className="block font-cinzel text-dorado-safe text-sm tracking-[0.3em] uppercase mb-3 font-bold">
        {subtitle}
      </span>
    )}
    <h2 className="font-cinzel text-3xl md:text-5xl font-bold text-pizarra leading-tight inline-block relative px-6">
      {title}
      <span className="absolute bottom-0 left-1/2 -translate-x-1/2 w-16 h-1 bg-pompeyano rounded mt-2"></span>
    </h2>
  </div>
);