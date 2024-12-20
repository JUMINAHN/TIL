import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App.jsx'
import './index.css'  
import { Provider } from 'react-redux'
import store from './store';


createRoot(document.getElementById('root')).render(
  // 브라우저 라우터보다 상위에 있어야 함
  <Provider store={store}>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Provider>
)
