import { Route, Routes } from 'react-router-dom'
import './App.css'
import Home from './pages/Home'
import MindSet from './pages/MindSet'
import Profile from './pages/Profile'
import Project from './pages/Project'
import Skill from './pages/Skill'
import Strong from './pages/Strong'
import Weak from './pages/Weak'

function App() {
  // 리덕스는 추후 학습에서 사용할 것,, => 동영상 꼭 보기

  return (
    <Routes>
      <Route path='/' element={<Home />}>Home</Route>
      <Route path='/profile' element={<Profile />}>Profile</Route>
      <Route path='/skill' element={<Skill />}>Skill</Route>
      <Route path='/project' element={<Project />}>Project</Route>
      {/* <Route path='/strong' element={<Strong />}>Strong</Route> */}
      {/* <Route path='/weak' element={<Weak />}>Weak</Route> */}
      <Route path='/mindSet' element={<MindSet />}>MindSet</Route>
    </Routes>
  )
}

export default App
