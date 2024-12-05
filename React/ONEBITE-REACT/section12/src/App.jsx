import { act, createContext, useContext, useEffect, useReducer, useRef, useState } from 'react'
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

//localStorage에 mockData값 저장해줌
//reducer은 신기하게
function reducer(state, action) {
  let nextState
  switch(action.type) {
    case "INIT":
      return action.data;
    case "CREATE":
      nextState = [action.data, ...state];
      break
    case "UPDATE":
      nextState = state.map(item => String(item.id) === String(action.data.id) ? action.data : item);
      break
    case "DELETE":
      nextState = state.filter(item => String(item.id) !== String(action.data.id))
      break
    default:
      return state;
  }
  localStorage.setItem("diary", JSON.stringify(nextState))
  return nextState
}

export const DiaryStateContext = createContext() 
export const DiaryDispatchContext = createContext()

function App() {
  // 로딩중일 때 페이지 컴포넌트 불러오는
  // 로딩상태 불러오는 상태 state
  const [isLoading, setIsLoading] = useState(true)


  const refId = useRef(0) //가장 높은 아이디값 + 1
  const [data, dispatch] = useReducer(reducer, []) //mockData 
  //화면에 처음나타날때 local기반
  useEffect(() => {
    const storedData = localStorage.getItem("diary");
  
    if (!storedData) {
      // 데이터가 없을 경우 mockData로 초기화
      localStorage.setItem("diary", JSON.stringify(mockData));
      dispatch({
        type: "INIT",
        data: mockData,
      });
      refId.current = mockData.length + 1; // 새로운 ID 설정
      return;
    }
  
    try {
      // storedData가 null이 아닐 때만 파싱 시도
      const parsedData = JSON.parse(storedData);
  
      if (!Array.isArray(parsedData)) {
        setIsLoading(false)
        throw new Error("Parsed data is not an array.");
      }
  
      let maxId = 0;
      parsedData.forEach(item => {
        if (Number(item.id) > maxId) {
          maxId = Number(item.id);
        }
      });
      refId.current = maxId + 1;
  
      dispatch({
        type: "INIT",
        data: parsedData,
      });
      // data state 초기화한 순간 loading 완료
      setIsLoading(false)

      // data의 정보를 모두 활용 => 초기값이 설정되지 않을 때 오류 
    } catch (error) {
      console.error("로컬 저장소 데이터 파싱 오류:", error);
      
      // 오류 발생 시 mockData로 초기화
      localStorage.setItem("diary", JSON.stringify(mockData));
      dispatch({
        type: "INIT",
        data: mockData,
      });
      refId.current = mockData.length + 1; // 새로운 ID 설정
    }
  }, []);

  // 문자열로 전환
  // localStorage.setItem('person', JSON.stringify({name : '이정환'}))
  // console.log(localStorage.getItem('test'))
  // console.log(localStorage.getItem('person')) //객체형태의 문자열로 출력되는 것을 볼 수 있음
  // //문자열을 다시 객체로 전환
  // console.log(JSON.parse(localStorage.getItem('person'))) //undefine이나 null이면 오류
  // localStorage.removeItem("test")

  //일기 데이터 보관
  //data => reducer가 작동될때마다~~

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

  if (isLoading) {
    return <div>데이터 로딩 중입니다...</div>
  }

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
