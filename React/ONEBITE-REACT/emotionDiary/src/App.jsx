import { Link, Route, Routes, useNavigate } from 'react-router-dom'
import './App.css'
import Diary from './pages/Diary'
import Edit from './pages/Edit'
import Home from './pages/Home'
import New from './pages/New'
import NotFound from './pages/NotFound'
import { createContext, useContext, useEffect, useReducer, useRef, useState } from 'react'
import js from '@eslint/js'


function reducer(state, action) { //값들이 들어가있을떄 => set으로 넣은 후 다시 mount되도록
  let nextState 
  //각각 새로운 state를 리턴하는게 아니라 nextState를 활용해서 return 시켜줄 것
  switch(action.type) {
    case "INIT" : //초기 값은 기존 값 전달
      return action.data //기존 값 전달  == nextState는 로컬 스토리지 변경된 데이터를 보관하기 위함 == 방금 불러온 값 : 바로 리턴
    case "CREATE": {
      nextState = [action.data , ...state]
      break
    }
    case "UPDATE": {
      nextState = state.map((item) => String(item.id) === String(action.data.id) ? action.data : item)
      break
    }
    case "DELETE": {
      nextState = state.filter((item) => String(item.id) !== String(action.data.id)) 
      break
    }
    case "default":
      return state //state 현태 상태 그대로를 돌려준다.
  }
  //localStorage에 해당 메서드를 실행될 때 저장되도록 해준다.
  localStorage.setItem("diary", JSON.stringify(nextState)) // 저장해줄 것이니까 => set이니까
  return nextState
}  

const mockData = [
  // 그냥 new Date의 날짜 작성해도 형식에 맞게 입력됨 => new Date("2024-12-06")
  {id : 1, createdDate : new Date("2024-12-07").getTime() , emotionId : 1, content : '1번 일기'},
  {id : 2, createdDate : new Date("2024-12-06").getTime() , emotionId : 2, content : '2번 일기'},
  {id : 3, createdDate : new Date("2024-11-07").getTime() , emotionId : 3, content : '3번 일기'},
  {id : 4, createdDate : new Date("2024-10-07").getTime() , emotionId : 4, content : '4번 일기'},
  {id : 5, createdDate : new Date("2024-10-06").getTime() , emotionId : 1, content : '5번 일기 : 내 생일'},
]

//사용할때 useContext로 사용할 것
//이것도 export? => data값을 넣으려니까 맨 상기에서 접근은 불가능 ==> export 공급을 하려면 맨 위로
export const DiaryStateContext = createContext() //data값을 넣고 == state값이니까
export const DiaryDispatchContext = createContext() // 여러개니까 객체를 넣나..? dispatch관련 data들을 넣을 것

function App() {
  //로딩 상태를 보관하는 컴포넌트가 있어야함 아니면 rendering전체 들어가면 제대로 호출되지 않음
  //초기는 일단 loading 상태니까 treu
  const [isLoading, setIsLoading] = useState(true)
  //값이 수정되거나 삭제될때도 진행되게 해야함 => 해당 값을 저장하기 위해
  // console.log(localStorage.getItem("diary"), 'diary') //그대로 그냥 => 문자열로 됨
  // console.log(JSON.parse((localStorage.getItem("diary"))), 'parse')
  // const [data, dispatch] = useReducer(reducer, JSON.parse((localStorage.getItem("diary"))), 'parse') //일단 빈배열
  const [data, dispatch] = useReducer(reducer, []) //일단 빈배열
  const idRef = useRef(0) //4번부터니까

  //마운트 되고, localStorage값을 깁나으로 값을 설정
  useEffect(() => {
    const storedData = localStorage.getItem("diary")
    if (!storedData) {
      setIsLoading(false); // 데이터가 없을 경우 로딩 종료
      return;
    }
    
    const parsedData = JSON.parse(storedData)
    if (!Array.isArray(parsedData)) {
      setIsLoading(false); // 배열이 아닐 경우 로딩 종료
      return;
    }
  
    console.log(parsedData); // 초기 데이터 확인
  
    // 최대 ID 찾기
    let maxId = 0;
    parsedData.forEach((item) => {
      if (Number(item.id) > maxId) {
        maxId = Number(item.id)
      }
    });
    
    idRef.current = maxId + 1 // 새로운 ID 설정
    dispatch({
      type: "INIT",
      data: parsedData,
    });
  
    setIsLoading(false) // 데이터 초기화 후 로딩 종료
  }, [])
  //가장 큰 값부터 확인
  // const diary = JSON.parse(localStorage.getItem("diary"))
  // const [data, dispatch] = useReducer(reducer, localStorage.getItem("diary")) //일단 빈배열
  // localStorage.setItem("diary", mockData) //저장 == [object Object],[object Object],[object Object],[object Object],[object Object]
  // localStorage.setItem("diary", JSON.stringify(mockData))

  const onCreate = (createdDate, emotionId, content) => { //들어올 데이터들
      dispatch({ //맞게 들어간것을 볼 수 있음
      type: "CREATE", //create로 들어갈 값 임시로 생성
      data: {//data에 들어갈 값
        id : Number(idRef.current++), 
        createdDate : createdDate,
        emotionId : emotionId,
        content : content}
    })
  }

  const onUpdate = (createdDate, emotionId, content, id) => { //id값을 받아서 matching => 여기에 대한 처리를 어떻게 할지에 대한 고민
    dispatch({ 
      type:"UPDATE",
      //이미 들어가 있는 키값에 변수명 넣기 == 값이 똑같아서 상관없지 않는가..? == 상관없음
      data : {
        id,
        createdDate : createdDate,
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

  if (isLoading) {
    return <div>데이터가 로딩중입니다..</div>
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
