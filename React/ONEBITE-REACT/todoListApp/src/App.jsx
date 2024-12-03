import { useState } from 'react'
import Header from './components/Header'
import Editor from './components/Editor';
import List from './components/List';
import './App.css'

//list에 요소들을 전해줘야 활용할 수 있음
const todos = [
  {id : 0, isDone : false, title:'REACT 공부하기', date:'Date'},
  {id : 1, isDone : false, title:'빨래 널기', date:'Date'},
  {id : 2, isDone : false, title:'노래 연습하기', date:'Date'}
]

//여기까지가 todo추가하기
function App() {
  //state에 변경이 되려면?
  //Q. 새로운 값이 추가되어야 함 => 단순 todos.push하면 적용되지 않음 (why?)
  //그럼 set메서드 활용해서 새로운 배열로 넣어줘야 함..
  //input에 대한 값을 == 변화가 일어나야 가능
  const [todo, setTodo] = useState(todos) //여기서 초기 todo의 값은 todos

  //여기 setTodo에 영향을 주려면? 일단 Editor에 추가와 click버튼을 눌러줘야 함
  const onClickAddBtn = (input) => {//새로운 값, 그리고 todo
    setTodo( //input data를 기존에 추가
      [input, ...todos] //todo가 여러개니까 == 기존 todos 활용
    )
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
