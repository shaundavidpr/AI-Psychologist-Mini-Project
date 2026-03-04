import React, { useEffect } from 'react'
import Indroduction from '../src/Pages/Indro'
import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom'
import Navbar from './Components/navbar'
import Landing from '../src/Components/Landing'
import Detailscollection from './Components/Detailscollection'
import Dashboard from './Components/Dashboard'
import Home from './Components/Home'
import Crisis from './Components/Crisis'
import Profile from './Components/Profile'
import About from './Components/About'
import Features from './Components/Features'
import Cardsection from './Components/Cardssection'
import Resourses from './Components/Resourses'
import Contact from './Components/Contact'

const App = () => {
  return (
    <div style={{ scrollBehavior: 'smooth' }}>
      
      <BrowserRouter>
      
      {/* Scroll to hash handler */}
      <ScrollToHash />
      <Routes>
        <Route path='/' element={<Indroduction/>}/>
        <Route path='/landing' element={<Landing/>}/>
        <Route path='/detailscollection' element={<Detailscollection/>}/>
        <Route path='/dashboard' element={<Dashboard/>}/>
        <Route path='/home' element={<Home/>}/>
        <Route path='/crisis' element={<Crisis/>}/>
        <Route path='/profile' element={<Profile/>}/>
        <Route path='/about' element={<About/>}/>
        <Route path='/features' element={<Features/>}/>
        <Route path='/cardsection' element={<Cardsection/>}/>
        <Route path='/resourses' element={<Resourses/>}/>
        <Route path='/contact' element={<Contact/>}/>
        
      </Routes>
      
      </BrowserRouter>
  
    </div>
  )
}

export default App

function ScrollToHash() {
  const { hash, pathname } = useLocation();

  useEffect(() => {
    if (hash) {
      const id = hash.replace('#', '');
      const el = document.getElementById(id);
      if (el) {
        // small timeout to ensure navigation rendered
        setTimeout(() => el.scrollIntoView({ behavior: 'smooth', block: 'start' }), 50);
      }
    }
  }, [hash, pathname]);

  return null;
}