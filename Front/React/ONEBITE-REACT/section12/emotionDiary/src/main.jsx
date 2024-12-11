import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { BrowserRouter } from 'react-router-dom'


createRoot(document.getElementById('root')).render(
  // 어디에 base를 달고있는지에 대한 정보를 얻을 수 있음
  // path가 어디에 있는지? == BrowserRouter자체를 볼 수 있음 == 주소 관련 정보 보관
  <BrowserRouter>
    <App /> 
  </BrowserRouter>
)
