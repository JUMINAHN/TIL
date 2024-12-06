import { Link, Route, Routes, useNavigate } from 'react-router-dom'
import './App.css'
import Diary from './pages/Diary'
import Edit from './pages/Edit'
import Home from './pages/Home'
import New from './pages/New'
import NotFound from './pages/NotFound'



function App() {
  //Router로 이동시킬 수 있어야 함
  //실제 A tag 사용하면 우리가 원하는 SPA 원칙을 못지킴
  //버튼이 navigate잖아
  //Link to
  const nav = useNavigate()
  //버튼말고, 그냥 url 링크로 이동하기..
  return (
    <div>
      <div>
        <Link to="/">HOME</Link>|
        <Link to="/new">New</Link>|
        <Link to="/diary">Diary</Link>|
        <Link to="/edit">Edit</Link>|
      </div>

      <div>
        <button
        onClick={()=> {
          nav('/new')
        }}>New Page로 이동합니다.</button>
      </div>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/new" element={<New />}></Route>
        <Route path="/edit/:id" element={<Edit />}></Route>
        {/* id로 설정 하면  */}
        <Route path="/diary" element={<Diary />}></Route>
        <Route path="*" element={<NotFound />}></Route>
      </Routes>
    </div>
  )
}

export default App
