import { StrictMode } from 'react'
import { BrowserRouter } from 'react-router-dom'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'


createRoot(document.getElementById('root')).render(
  // react의 모든 component들이 공급받아서 사용될 수 있음 
  <BrowserRouter>
    <App />
  </BrowserRouter>

)
