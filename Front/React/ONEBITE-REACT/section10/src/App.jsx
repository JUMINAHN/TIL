import { useCallback, useReducer, useRef, useState } from 'react'
import './App.css'
import Header from './components/Header'
import Editor from './components/Editor'
import List from './components/List'
import TodoItem from './components/TodoItem'
// import Exam from './components/Exam'


function reducer(state, action) {
  //action 객체에 따라 변화된 state값 return
  switch(action.type)  {
    //type이
    case "CREATE" :
      return [action.data, ...state] //action에 있는 데이터들 그대로 받아올 것 + 그리고 state : 기존에 있는 state값 가져오기 => mockData가 todos == state
    case "UPDATE" :
      return state.map((item) => item.id === action.targetId ? {...item, isDone:!item.isDone} : item)
    case "DELETE" :
      return state.filter((item) => item.id !== action.targetId)
    default:
      return state
  }
}
 
const mockData = [//배열안에 객체 형태
  {id:0, isDone : false, content : 'REACT 공부하기', date:new Date().getTime()} ,//더미
  {id:1, isDone : false, content : '빨래하기', date:new Date().getTime()},   //더미
  {id:2, isDone : false, content : '노래연습하기', date:new Date().getTime()} //더미
]  

function App() {
  const [todos, dispatch] = useReducer(reducer, mockData)
  const idRef = useRef(3)

  const onCreate = useCallback((content) => { 
    //setTodos가 없으니까 해당 부분 새로 바꿔줘야 함
    dispatch({
      type : "CREATE", //생성할거니까
      data : {
        id : idRef.current++, //임시
        isDone : false,
        content : content,
        date : new Date().getTime()
      }
    })
  }, [])

  const onUpdate = useCallback((targetId) => {
    dispatch({
      type:"UPDATE",
      targetId : targetId //어떠한 요소를 수정할건지만 말한다.
    })

  }, [])


  // const func = useCallback(()=> {}, []) //mount될때만 생성함 
  // 메모이제이션 하고시은거만 복사
  const onDelete = useCallback((targetId) => {
    dispatch({
      type:"DELETE",
      targetId : targetId
    })
  }, [])

  return (
    <div className='App'>
      <Header/>
      <Editor 
      onCreate={onCreate}
      />
      <List
      todos={todos}
      onUpdate={onUpdate}
      onDelete={onDelete}/>
      {/* <Exam /> */}
    </div>
  )
}


export default App
