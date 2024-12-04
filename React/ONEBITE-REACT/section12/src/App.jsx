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
    createdData : new Date("2024-12-04").getTime(),
    emotionId : 1,
    content : "1번 일기 내용"
  },
  {
    id : 2,
    createdData : new Date("2024-12-03").getTime(),
    emotionId : 2,
    content : "2번 일기 내용"
  },
  {
    id : 3,
    createdData : new Date("2024-11-02").getTime(),
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
      // id값이 일치하면 거기에 해당하는 값만 바꾸면 된다.. 
      // 즉 일치하는 애들만 action data있는 것으로 하고 아니면 기존 값으로 바꿔주면 된다.
      // map의 {} 이거 다시
      return state.map((item) => String(item.id) === String(action.data.id) ? action.data : item)
    case "DELETE" :
      return state.filter((item) => String(item.id) !== String(action.data.id))
    case "default":
      return state
  } 
}
//모든 곳에서 사용가능할 수 있도록 공급
//DiaryState를 다른데서 사용해야하니까 내보내야함 
export const DiaryStateContext = createContext() //data state 값을 routes 밑의 모든 페이지가 접근할 수 있도록 한다.
export const DiaryDispatchContext = createContext()

function App() {
  const refId = useRef()
  const [data, dispatch] = useReducer(reducer, mockData) //state 대신 reducer 전체 복잡한 코드 쉽게 관리하기 위함

  //새로운 일기 추가 = newpage()가 정상 호출될거라 생각하고
  //data에 무엇인가를 추가하기 위해선 dispatch를 추가한다.
  //create 함수 호출
  const onCreate = (createData, emotionId, content) => { //매개변수로 전달받을 내용 => 왜냐하면 mockData와 일치시켜줘야함
    dispatch({
      type : "CREATE",
      data : {
        id : refId.current++,
        createData,
        emotionId,
        content
      }
    })
  }
   
  //기존 일기 수정
  const onUpdate = (id, createData, emotionId, content) => { //id 내용을 받아와서 그게 맞는지 확인 후 수정되어야 함
    dispatch({
      type : "UPDATE",
      data : {
        id,
        createData,
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
