import { useReducer, useState } from 'react'
import Home from '../pages/Home'
import New from '../pages/New'
import Diary from '../pages/Diary'
import NotFound from '../pages/NotFound'
import Edit from '../pages/Edit'
import { Link, Route, Routes, useNavigate, useRoutes } from 'react-router-dom'
import { getEmotionImage } from '../util/get-emotion-image'
import Button from './components/Button'
import Header from './components/Header'
import './App.css'

//일기 데이터 여러개
const mockData = [
  {
    id : 1,
    createdData : new Date().getTime(),
    emotionId : 1,
    content : "1번 일기 내용"
  },
  {
    id : 2,
    createdData : new Date().getTime(),
    emotionId : 2,
    content : "2번 일기 내용"
  },
]

//reducer은 신기하게
function reducer(state, action){//상태랑 action
  return state
}

function App() {
  //여러개의 일기 데이터 보관해야하니까 []로 일단 임시 저장
  const [data, dispatch] = useReducer(reducer, mockData) //state 대신 reducer 전체 복잡한 코드 쉽게 관리하기 위함
  // dispatch({
  //   type:,
  //   data:
  // })

  const nav  = useNavigate()

  // const onclickBtn = () => [
  //   nav("/new") //nav에 link
  // ]
  return (
    <>
    {/* 상단에 components 뜨는 것 생각 */}
    <Header title={"Header"}
    leftChild={<Button text={"<"}/>}
    rightChild={<Button text={">"}/>}/>
{/* 
    <Button 
    text={123}
    type="DEFAULT"
    onClick={()=> {
      console.log('123번 버튼 클릭')
    }}/>

    <Button 
    text={234}
    type="POSITIVE"
    onClick={()=> {
      console.log('234번 버튼 클릭')
    }}/>

    <Button 
    text={345}
    type="NEGATIVE"
    onClick={()=> {
      console.log('345번 버튼 클릭')
    }}/> */}

    {/* <div>
      <h1>asset 내부</h1>
      <img src={getEmotionImage(1)} alt="" />
      <img src={getEmotionImage(2)} alt="" />
      <img src={getEmotionImage(3)} alt="" />
      <img src={getEmotionImage(4)} alt="" />
      <img src={getEmotionImage(5)} alt="" />
    </div> */}

    {/* <div>
      <Link to={"/"}>Home</Link> | 
      <Link to={"/new"}>New</Link> | 
      <Link to={"/diary"}>Diary</Link> | 
    </div> */}
    {/* <button
    onClick={onclickBtn}>New page로 이동</button> */}
      <Routes>
        {/* routes안에 route밖에 못들어간다. */}
        <Route path="/" element={<Home />} />
        <Route path="/new" element={<New />} />
        <Route path="/diary/:id" element={<Diary />} />
        <Route path="/edit/:id" element={<Edit />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </>
  )
}

export default App
