import { useRef, useState } from 'react'
import './App.css'
import Header from './components/Header'
import Editor from './components/Editor'
import List from './components/List'
import TodoItem from './components/TodoItem'



  //모조품 == 리랜더링시 다시 생성할 필요가 없음, 상수라서 값바뀌지 않기떄문에 외부 선언 괜찮음
  const mockData = [//배열안에 객체 형태
    {id:0, isDone : false, content : 'REACT 공부하기', date:new Date().getTime()} ,//더미
    {id:1, isDone : false, content : '빨래하기', date:new Date().getTime()},   //더미
    {id:2, isDone : false, content : '노래연습하기', date:new Date().getTime()} //더미
  ]
  //객체의 일부를 바꿔줘야 함 => 토글 기능
  

function App() {
  const [todos, setTodos] = useState(mockData) //여러개의 투두를 넣을 것이니까 => 해당 값을 기반으로 초기화
  //todos값을 바꿔줘야 함
  const idRef = useRef(3)

  const onUpdate = (targetId) => {
    //targetId와 일치하는 id의 isDone 바뀜
    //새로운 배열 전달 => 다시
    setTodos(todos.map((todo) => {
      if(todo.id === targetId) {
        return {
          ...todo,
          isDone : !todo.isDone //그것만 변경
        }
      }
      return todo
    }))
  }

  const onCreate = (content) => { //content로 에디터에서 받아와서 이전에 만든 객체형태로 만들어줘야 함
    const newTodo = {
      id : idRef.current++, //임시
      isDone : false,
      content : content,
      date : new Date().getTime()
    }
    // todos.push(newTodo) //이렇게 하면 안됨 => state는 상태변화로 해야함 제공된 함수로
    setTodos([newTodo, ...todos])
  }

  const onDelete = (targetId) => {
    //target과 일치하는 요소만 걸러서 삭제한다.
    setTodos(todos.filter((todo) => todo.id !== targetId )) //아닌 애들만 다시 새로운 배열로 만들어줌
  }

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

    </div>
  )
}

export default App
