import { Route, Routes, useLocation, useNavigate } from 'react-router-dom'
import './App.css'
import Home from './pages/Home'
import MindSet from './pages/MindSet'
import Profile from './pages/Profile'
import Project from './pages/Project'
import Skill from './pages/Skill'
// import Strong from './pages/Strong'
// import Weak from './pages/Weak'
import myBag from '../src/assets/mainImg/001.png'
import { useEffect } from 'react'


function App() {
  // 리덕스는 추후 학습에서 사용할 것,, => 동영상 꼭 보기
  const location = useLocation() //지속해서 추적이 가능함
  const nav = useNavigate()

  // 초기 랜더링을 profile로
  useEffect(() => {
    nav('/profile')
  }, [])

  const onClickMoveLink = () => {
    nav('/')
  }

  // console.log(location)
  // console.log(location.pathname)

  return (
    <div className='App'>
      <Routes>
        <Route path='/profile' element={<Profile />}>Profile</Route>
        <Route path='/' element={<Home />}>Home</Route>
        <Route path='/skill' element={<Skill />}>Skill</Route>
        <Route path='/project' element={<Project />}>Project</Route>
        <Route path='/mindSet' element={<MindSet />}>MindSet</Route>
        {/* <Route path='/strong' element={<Strong />}>Strong</Route> */}
        {/* <Route path='/weak' element={<Weak />}>Weak</Route> */}
      </Routes>

      <div className='bag_icon' onClick={onClickMoveLink}>
        {
          location.pathname === '/' ? '' : <img src={myBag} alt="" />
        }
      </div>
    </div>
  )
}

export default App
