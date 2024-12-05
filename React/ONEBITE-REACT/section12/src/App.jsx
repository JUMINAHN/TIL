import { act, createContext, useContext, useReducer, useRef, useState } from 'react'
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


// 일기 데이터 여러개
// 필터링을 위해서 임시데이터 변경해줌
const mockData = [
  {
    id : 1,
    createdDate : new Date("2024-12-04").getTime(),
    emotionId : 1,
    content : "1번 일기 내용"
  },
  {
    id : 2,
    createdDate : new Date("2024-12-03").getTime(),
    emotionId : 2,
    content : "2번 일기 내용"
  },
  {
    id : 3,
    createdDate : new Date("2024-11-02").getTime(),
    emotionId : 3,
    content : "3번 일기 내용"
  },

]

//reducer은 신기하게
function reducer(state, action){
  switch(action.type) {
    case "CREATE":
      return [action.data, ...state]
    case "UPDATE":
      return state.map((item) => String(item.id) === String(action.data.id) ? action.data : item)
    case "DELETE" :
      return state.filter((item) => String(item.id) !== String(action.data.id))
    case "default":
      return state
  } 
}

export const DiaryStateContext = createContext() 
export const DiaryDispatchContext = createContext()

function App() {
  const refId = useRef(4)
  const [data, dispatch] = useReducer(reducer, mockData) 


  const onCreate = (createdDate, emotionId, content) => { 
    dispatch({
      type : "CREATE",
      data : {
        id : refId.current++,
        createdDate,  
        emotionId,
        content
      }
    })
  }
   
  //기존 일기 수정
  const onUpdate = (id, createdDate, emotionId, content) => { //id 내용을 받아와서 그게 맞는지 확인 후 수정되어야 함
    dispatch({
      type : "UPDATE",
      data : {
        id,
        createdDate,
        emotionId,
        content
      }
    })
  }
   
  //기존 일기 삭제
  const onDelete = (id) => { 
    dispatch({
      type : "DELETE",
      data : {
        id,
      }
    })
  }
  const nav  = useNavigate()

  return (
    <>
      <DiaryStateContext.Provider value={data}>
        <DiaryDispatchContext.Provider value={{
          onCreate,
          onDelete,
          onUpdate
        }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/new" element={<New />} />
            <Route path="/diary/:id" element={<Diary />} />
            <Route path="/edit/:id" element={<Edit />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </DiaryDispatchContext.Provider>
      </DiaryStateContext.Provider>
    </>
  )
}

export default App
