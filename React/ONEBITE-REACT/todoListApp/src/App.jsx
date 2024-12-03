import { useRef, useState } from 'react'
import Header from './components/Header'
import Editor from './components/Editor';
import List from './components/List';
import './App.css'


const todos = [
  {id : 0, isDone : false, title:'REACT 공부하기', date:new Date().getTime()},
  {id : 1, isDone : false, title:'빨래 널기', date:new Date().getTime()},
  {id : 2, isDone : false, title:'노래 연습하기', date:new Date().getTime()}
]

function App() {
  const [todo, setTodo] = useState(todos) 
  const num = useRef(3) //3부터 시작

  //update
  const onUpdateTodo = (checkedId) => {
    console.log(checkedId, 'app까지 왔는가?') //온 것 확인됨

    const newTodo = todo.map((item) => {
      if (item.id === checkedId) {
        //return 값 등록 
        return {
        ...item,
        isDone : !(item.isDone) //객체 그자체를 그대로 가져와야 함
        }
      }
      return item
    })
    setTodo(newTodo) // 새로운 Todo로 상태 업데이트
  }

  //delete도 동일할 것 같음
  const onDeleteTodo = (checkedId) => {
    console.log(checkedId, 'app까지 왔는가2?') //온 것 확인됨

    const newTodo = todo.filter((item) => { //일치하는 것만 뽑으면
      if (item.id === checkedId) {
        return //값 자체를 안넣고 지나감
      }
      return item //나머지는 넣고
    })
    setTodo(newTodo) // 새로운 Todo로 상태 업데이트
  }

  const onClickAddBtn = (input) => {
    const newTodo = { 
      id : num.current++, 
      isDone : false,
      title : input,
      date : new Date().getTime()
    }
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
      onUpdateTodo={onUpdateTodo}
      onDeleteTodo={onDeleteTodo}
      todo={todo}/>      
    </div>
  )
}

export default App
