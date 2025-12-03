import React, { useState, useEffect } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { Icons } from '../constants';
import { SocialLinks } from '../types';

interface Props {
  social: SocialLinks;
}

export const Navbar: React.FC<Props> = ({ social }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const location = useLocation();

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  useEffect(() => {
    setIsOpen(false);
  }, [location]);

  const navClass = ({ isActive }: { isActive: boolean }) => 
    `font-cinzel font-bold tracking-widest transition-colors duration-300 ${
      isActive ? 'text-pompeyano border-b-2 border-pompeyano' : 'text-pizarra hover:text-pompeyano'
    }`;

  const mobileNavClass = ({ isActive }: { isActive: boolean }) => 
    `text-white font-cinzel text-3xl font-bold tracking-widest hover:text-dorado transition ${
      isActive ? 'text-dorado' : ''
    }`;

  return (
    // Fixed height header h-28 (7rem) to match App padding. z-50 ensures it's on top.
    <header className={`fixed top-0 w-full z-50 transition-all duration-300 h-28 flex items-center ${scrolled ? 'bg-pergamino/95 shadow-md backdrop-blur-sm' : 'bg-pergamino border-b border-dorado/20'}`}>
      <div className="container mx-auto px-4 flex justify-between items-center w-full">
        <NavLink to="/" className="block relative z-50">
          {/* LOGOTIPO: Fixed height ensures consistent layout spacing */}
          <img 
            src={social.logoUrl} 
            alt="Ibidem Logo" 
            className={`w-auto object-contain transition-all duration-300 ${scrolled ? 'h-16' : 'h-20'}`} 
          />
        </NavLink>

        {/* Desktop Nav */}
        <nav className="hidden md:flex space-x-6 items-center text-sm lg:text-base">
          <NavLink to="/" className={navClass}>DOMUS</NavLink>
          <NavLink to="/nostri" className={navClass}>NOSTRI</NavLink>
          <NavLink to="/fasti" className={navClass}>FASTI</NavLink>
          <NavLink to="/imagina" className={navClass}>IMAGINA</NavLink>
          <NavLink to="/tabularium" className={navClass}>TABULARIUM</NavLink>
          <NavLink to="/glossarium" className={navClass}>GLOSSARIUM</NavLink>
        </nav>

        {/* Mobile Toggle */}
        <button 
          className="md:hidden text-pompeyano p-2 relative z-50 focus:outline-none" 
          onClick={() => setIsOpen(!isOpen)}
          aria-label="Toggle Menu"
        >
          {isOpen ? <Icons.X className="text-white w-8 h-8" /> : <Icons.Menu className="w-8 h-8" />}
        </button>

        {/* Mobile Menu Overlay */}
        <div className={`fixed inset-0 bg-pompeyano flex flex-col items-center justify-center space-y-8 transition-transform duration-500 transform ${isOpen ? 'translate-x-0' : 'translate-x-full'} md:hidden z-40`}>
           {/* LOGOTIPO MÓVIL */}
           <img src={social.logoUrl} alt="Logo" className="h-32 w-auto mb-6 brightness-0 invert opacity-90" />
           <NavLink to="/" className={mobileNavClass}>DOMUS</NavLink>
           <NavLink to="/nostri" className={mobileNavClass}>NOSTRI</NavLink>
           <NavLink to="/fasti" className={mobileNavClass}>FASTI</NavLink>
           <NavLink to="/imagina" className={mobileNavClass}>IMAGINA</NavLink>
           <NavLink to="/tabularium" className={mobileNavClass}>TABULARIUM</NavLink>
           <NavLink to="/glossarium" className={mobileNavClass}>GLOSSARIUM</NavLink>
        </div>
      </div>
    </header>
  );
};