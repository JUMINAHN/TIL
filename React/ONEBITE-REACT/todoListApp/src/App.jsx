import { useRef, useState } from 'react'
import Header from './components/Header'
import Editor from './components/Editor';
import List from './components/List';
import './App.css'


//list에 요소들을 전해줘야 활용할 수 있음
const todos = [
  {id : 0, isDone : false, title:'REACT 공부하기', date:new Date().getTime()},
  {id : 1, isDone : false, title:'빨래 널기', date:new Date().getTime()},
  {id : 2, isDone : false, title:'노래 연습하기', date:new Date().getTime()}
]

//여기까지가 todo추가하기
function App() {
  const [todo, setTodo] = useState(todos) 
  const num = useRef(3) //3부터 시작
  //QQid의 순서는 계속해서 바뀌어야 한다. ref 일반 let? state값이 바뀔떄마다 반응? QQ?

  const onClickAddBtn = (input) => {
    //input 데이터를 받아서 보완한다.
    //새로운 객체로 만들어져야 함 => 이것도 어떻게보면 반응형으로 해줘야하는 요소인지? QQ?


    //일단 input이 맞게 들어오지는가?
    //input값으로 새로들어왔는데
    const newTodo = { //새로운 객체 하나 => ()과 ({})의 차이 QQ?
      id : num.current++, //객체 자체이기 떄문에
      isDone : false,
      title : input,
      date : new Date().getTime()
    }

    //이전 상태를 고려하지 않음?
    // setTodo([input, ...todo])
    setTodo((prev)=> {
      const updateTodo = [...prev, newTodo]
      return updateTodo
    })
  }


  return (
    <div className='App'>
      <Header />      
      <Editor 
      onClickAddBtn={onClickAddBtn}/>      
      <List 
      todo={todo}/>      
    </div>
  )
}

export default App
