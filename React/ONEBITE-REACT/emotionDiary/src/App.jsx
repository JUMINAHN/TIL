import { Link, Route, Routes, useNavigate } from 'react-router-dom'
import './App.css'
import Diary from './pages/Diary'
import Edit from './pages/Edit'
import Home from './pages/Home'
import New from './pages/New'
import NotFound from './pages/NotFound'
import { createContext, useContext, useEffect, useReducer, useRef } from 'react'


function reducer(state, action) { 
  switch(action.type) { 
    case "CREATE":
      return [action.data , ...state]
    case "UPDATE":
      return state.map((item) => String(item.id) === String(action.data.id) ? action.data : item)
    case "DELETE":
      return state.filter((item) => String(item.id) !== String(action.data.id)) 
    case "default":
      return state //state 현태 상태 그대로를 돌려준다.
  }
}

const mockData = [
  // 그냥 new Date의 날짜 작성해도 형식에 맞게 입력됨 => new Date("2024-12-06")
  {id : 1, createdDate : new Date("2024-12-07").getTime() , emotionId : 1, content : '1번 일기'},
  {id : 2, createdDate : new Date("2024-12-06").getTime() , emotionId : 2, content : '2번 일기'},
  {id : 3, createdDate : new Date("2024-11-07").getTime() , emotionId : 3, content : '3번 일기'},
  {id : 5, createdDate : new Date("2024-10-06").getTime() , emotionId : 1, content : '5번 일기 : 내 생일'},
  {id : 4, createdDate : new Date("2024-10-07").getTime() , emotionId : 4, content : '4번 일기'},
]

//사용할때 useContext로 사용할 것
//이것도 export? => data값을 넣으려니까 맨 상기에서 접근은 불가능 ==> export 공급을 하려면 맨 위로
export const DiaryStateContext = createContext() //data값을 넣고 == state값이니까
export const DiaryDispatchContext = createContext() // 여러개니까 객체를 넣나..? dispatch관련 data들을 넣을 것

function App() {
  const [data, dispatch] = useReducer(reducer, mockData) //일단 빈배열
  const idRef = useRef(4) //4번부터니까

  const onCreate = (createdDate, emotionId, content) => { //들어올 데이터들
      dispatch({ //맞게 들어간것을 볼 수 있음
      type: "CREATE", //create로 들어갈 값 임시로 생성
      data: {//data에 들어갈 값
        id : idRef.current++, 
        createdDate : new Date().getTime(),
        emotion : emotionId,
        content : content}
    })
  }

  const onUpdate = (id, createdDate, emotionId, content) => { //id값을 받아서 matching => 여기에 대한 처리를 어떻게 할지에 대한 고민
    dispatch({ 
      type:"UPDATE",
      //이미 들어가 있는 키값에 변수명 넣기 == 값이 똑같아서 상관없지 않는가..? == 상관없음
      data : {
        id,
        createdDate : new Date().getTime() + 1,
        emotionId,
        content,
      }
    })
  }

  const onDelete = (id) => {
    dispatch({
      type : "DELETE",
      data : {
        id
      }
    })
  }

  return (
    <div>
      <DiaryStateContext.Provider value={data}>
        <DiaryDispatchContext.Provider value={{
          onCreate,
          onUpdate,
          onDelete
        }}>
          <Routes>
            <Route path="/" element={<Home />}></Route>
            <Route path="/new" element={<New />}></Route>
            <Route path="/edit/:id" element={<Edit />}></Route>
            {/* id로 설정 하면  */}
            <Route path="/diary/:id" element={<Diary />}></Route>
            <Route path="*" element={<NotFound />}></Route>
          </Routes>
        </DiaryDispatchContext.Provider>
      </DiaryStateContext.Provider>
    </div>
  )
}

export default App
