import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render( //앱 컴포넌트 랜더링
  <StrictMode>
    <App />
  </StrictMode>,
)
