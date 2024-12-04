import { useState } from 'react'
import Home from '../pages/Home'
import New from '../pages/New'
import Diary from '../pages/Diary'
import NotFound from '../pages/NotFound'
import './App.css'
import { Link, Route, Routes, useNavigate, useRoutes } from 'react-router-dom'
import { getEmotionImage } from '../util/get-emotion-image'

//매번 작성해야하는 귀찮음을모듈로 해결
// import emotion1 from './assets/emotion1.png'
// import emotion2 from './assets/emotion2.png'
// import emotion3 from './assets/emotion3.png'
// import emotion4 from './assets/emotion4.png'
// import emotion5 from './assets/emotion5.png'


//index의 기능
//1. / : 모든 일기를 조회하는 home 페이지
//2. /new : 새로운 일기를 작성하는 New 페이지
//3. /diary : 일기를 상세히 조회하는 Diary 페이지 

function App() {
  const nav  = useNavigate()

  const onclickBtn = () => [
    nav("/new") //nav에 link
  ]
  return (
    <>
    {/* 일반적 react 컴포넌트같은 것 : 공통적으로 사용될 것이 아니라면 route 외부에 사용하지 않는 것을 추천 */}
    {/* routes 위에 선언을 하면 모든 페이지에 들어간다. */}
    {/* 이미지가 최적화 되지 않음*/}
    {/* <div>
      <h1>public 내부</h1>
      <img src={"/emotion1.png"} alt="" />
      <img src={"/emotion2.png"} alt="" />
      <img src={"/emotion3.png"} alt="" />
      <img src={"/emotion4.png"} alt="" />
      <img src={"/emotion5.png"} alt="" />
    </div> */}

    <div>
      <h1>asset 내부</h1>
      <img src={getEmotionImage(1)} alt="" />
      <img src={getEmotionImage(2)} alt="" />
      <img src={getEmotionImage(3)} alt="" />
      <img src={getEmotionImage(4)} alt="" />
      <img src={getEmotionImage(5)} alt="" />
    </div>

    <div>
      <Link to={"/"}>Home</Link> | 
      <Link to={"/new"}>New</Link> | 
      <Link to={"/diary"}>Diary</Link> | 
    </div>
    <button
    onClick={onclickBtn}>New page로 이동</button>
      {/* <br />
      <p>a Tag</p>
      <a href="/">Home</a> |
      <a href="/new">New</a> |
      <a href="/diary">Diary</a> | */}

      <Routes>
        {/* routes안에 route밖에 못들어간다. */}
        <Route path="/" element={<Home />} />
        <Route path="/new" element={<New />} />
        <Route path="/diary/:id" element={<Diary />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </>
  )
}

export default App
