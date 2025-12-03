import React, { useEffect, useState } from 'react';
import { HashRouter, Routes, Route, Navigate, useLocation, Link } from 'react-router-dom';
import { DATA } from './constants';
import { Navbar } from './components/Navbar';
import { Home } from './pages/Home';
import { Fasti } from './pages/Fasti';
import { Imagina } from './pages/Imagina';
import { Tabularium } from './pages/Tabularium';
import { Glossarium } from './pages/Glossarium'; // Import new page
import { SectionHeader } from './components/SectionHeader';
import { Icons } from './constants';

const Nostri = () => (
    <div className="max-w-4xl mx-auto animate-fade-in px-4 pt-8">
        <SectionHeader title="NOSTRI" subtitle="Nuestra Historia" />
        <article className="bg-white p-8 md:p-10 rounded-lg shadow-xl mb-12 border-l-4 border-pompeyano">
            {DATA.nostri.mainText.split('\n').map((p, i) => (
                p.trim() && (
                    <p key={i} className={`text-lg leading-relaxed mb-4 text-gray-700 text-justify ${i === 0 ? 'first-letter:text-5xl first-letter:font-cinzel first-letter:text-pompeyano first-letter:float-left first-letter:mr-3 first-letter:mt-[-4px]' : ''}`}>
                        {p}
                    </p>
                )
            ))}
        </article>
        <article className="bg-white p-8 rounded-xl shadow-xl flex flex-col md:flex-row gap-8 items-center">
            <img src={DATA.nostri.founder.image} alt={DATA.nostri.founder.name} className="w-32 h-32 md:w-40 md:h-40 rounded-full border-4 border-dorado object-cover shadow-lg" />
            <div className="text-center md:text-left">
                <h4 className="font-cinzel text-2xl font-bold text-pizarra">{DATA.nostri.founder.name}</h4>
                <p className="text-pompeyano font-cinzel text-sm mb-3 tracking-widest">{DATA.nostri.founder.years}</p>
                <p className="text-gray-600 italic leading-relaxed">{DATA.nostri.founder.desc}</p>
            </div>
        </article>
    </div>
);

// Article Detail Page
const ArticleDetail = () => {
    const loc = useLocation();
    const id = loc.pathname.split('/').pop();
    const art = DATA.tabularium.find(a => a.id === Number(id));
    const [scrollProgress, setScrollProgress] = useState(0);

    useEffect(() => {
        const handleScroll = () => {
            const totalScroll = document.documentElement.scrollTop;
            const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scroll = `${totalScroll / windowHeight}`;
            setScrollProgress(Number(scroll));
        }
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    const handleShare = async () => {
        if (navigator.share) {
            try {
                await navigator.share({
                    title: art?.title,
                    text: art?.summary,
                    url: window.location.href,
                });
            } catch (err) { console.log(err) }
        } else {
            navigator.clipboard.writeText(window.location.href);
            alert('Enlace copiado');
        }
    };

    // Helper simple para renderizar markdown básico (negrita/cursiva)
    const renderText = (text: string) => {
        // Reemplaza *texto* por <em>texto</em>
        const html = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
        return <span dangerouslySetInnerHTML={{ __html: html }} />;
    };

    if (!art) return <div>No encontrado</div>;

    return (
        <>
         {/* Reading Progress Bar */}
         <div className="fixed top-28 left-0 h-1 bg-pompeyano z-40 transition-all duration-100 ease-out" style={{ width: `${scrollProgress * 100}%` }}></div>
         
         <article className="max-w-3xl mx-auto bg-white p-8 md:p-12 rounded-xl shadow-2xl my-8 animate-fade-in relative px-6 mt-4 md:mt-0">
            <div className="flex justify-between items-center mb-6">
                <Link to="/tabularium" className="text-gray-400 hover:text-pompeyano transition flex items-center text-sm font-bold"><Icons.ArrowLeft className="mr-1"/> Volver</Link>
                <button onClick={handleShare} className="text-gray-400 hover:text-dorado-safe transition flex items-center text-sm font-bold gap-1">
                     <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/></svg>
                     Compartir
                </button>
            </div>
            
            <header className="text-center mb-10 mt-2">
                <span className="text-xs font-cinzel text-dorado-safe uppercase tracking-widest block mb-2">{art.category}</span>
                <h1 className="font-cinzel text-3xl md:text-4xl font-bold text-pizarra mb-4">{art.title}</h1>
                <p className="text-gray-500 italic text-sm">Por {art.author} | {art.date}</p>
            </header>
            <img src={art.img} className="w-full rounded-lg mb-10 shadow-md" alt={art.title}/>
            <div className="prose max-w-none text-gray-800">
                {/* Intro with Drop Cap */}
                <p className="text-lg italic border-l-4 border-pompeyano pl-4 mb-8 bg-gray-50 p-4 rounded-r first-letter:text-5xl first-letter:font-cinzel first-letter:text-pompeyano first-letter:float-left first-letter:mr-3 first-letter:mt-[-4px]">
                    {art.intro}
                </p>
                {art.sections.map((s,i) => (
                    <div key={i} className="mb-8">
                        <h2 className="font-cinzel text-xl font-bold text-pompeyano mb-3 border-b border-gray-200 pb-1">{s.title}</h2>
                        <p className="text-justify text-gray-700 leading-relaxed mb-4">{s.content}</p>
                    </div>
                ))}
                
                {/* BIBLIOGRAFÍA */}
                {art.bibliography && art.bibliography.length > 0 && (
                    <div className="mt-12 pt-8 border-t-2 border-dorado/30 bg-gray-50 p-6 rounded-lg">
                        <h3 className="font-cinzel text-lg font-bold text-pizarra mb-4 flex items-center">
                            <Icons.Book className="w-5 h-5 mr-2 text-dorado-safe"/>
                            Fuentes y Bibliografía
                        </h3>
                        <ul className="list-none space-y-3 text-sm text-gray-600 font-merriweather pl-2">
                            {art.bibliography.map((item, idx) => (
                                <li key={idx} className="relative pl-4 before:content-['•'] before:absolute before:left-0 before:text-pompeyano">
                                    {renderText(item)}
                                </li>
                            ))}
                        </ul>
                    </div>
                )}
            </div>
        </article>
        </>
    )
}

const ScrollToTop = () => {
  const { pathname } = useLocation();
  useEffect(() => window.scrollTo(0, 0), [pathname]);
  return null;
};

const Footer = () => {
  const location = useLocation();
  // Hide global footer on mobile Fasti/Tabularium to use the integrated sticky footer
  const isMobileAppView = (location.pathname === '/fasti' || location.pathname === '/tabularium');

  return (
    <footer className={`bg-pizarra text-pergamino py-6 md:py-10 border-t-4 border-dorado mt-auto ${isMobileAppView ? 'hidden md:block' : ''}`}>
        <div className="container mx-auto px-4 text-center">
            <div className="flex justify-center gap-6 md:gap-8 mb-4 md:mb-6">
                <a href={DATA.general.facebook} target="_blank" rel="noreferrer" className="hover:text-dorado transform hover:scale-110 transition"><Icons.Facebook className="w-6 h-6 md:w-8 md:h-8" /></a>
                <a href={DATA.general.instagram} target="_blank" rel="noreferrer" className="hover:text-dorado transform hover:scale-110 transition"><Icons.Instagram className="w-6 h-6 md:w-8 md:h-8" /></a>
                <a href={`mailto:${DATA.general.email}`} className="hover:text-dorado transform hover:scale-110 transition"><Icons.Mail className="w-6 h-6 md:w-8 md:h-8" /></a>
            </div>
            <p className="font-cinzel text-[10px] md:text-xs text-gray-500 tracking-widest mb-2">&copy; {new Date().getFullYear()} IBIDEM.</p>
        </div>
    </footer>
  );
};

export default function App() {
  return (
    <HashRouter>
      <ScrollToTop />
      <div className="flex flex-col min-h-screen">
        <Navbar social={DATA.general} />
        {/* Padding Top (pt-28 = 7rem) MUST match Navbar height to avoid overlap/cut-off content */}
        <main className="flex-grow pt-28 md:pt-36 pb-0 bg-noise">
          <Routes>
            <Route path="/" element={<Home data={DATA.home} heroImage={DATA.general.heroImageHome} />} />
            <Route path="/nostri" element={<Nostri />} />
            <Route path="/fasti" element={<Fasti data={DATA} />} />
            <Route path="/tabularium" element={<Tabularium />} />
            <Route path="/tabularium/:id" element={<ArticleDetail />} />
            <Route path="/imagina" element={<Imagina data={DATA} />} />
            <Route path="/imagina/:id" element={<Imagina data={DATA} />} />
            <Route path="/glossarium" element={<Glossarium />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </HashRouter>
  );
}