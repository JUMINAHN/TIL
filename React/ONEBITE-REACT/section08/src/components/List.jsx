import { useState } from 'react';
import './List.css';
import TodoItem from './TodoItem';

const List = ({todos, onUpdate, onDelete}) => {
  const [search, setSearch] = useState("")
  const onChangeSearch = (e) => {
    setSearch(e.target.value)
  }

  const getFilteredData = () => {
    //filtering된 todos => search값 존재하는 애들만 필터링
    if(search === "") {
      return todos
    }

    //왜 여기 {} 안쓰이는지
    return todos.filter((todo) => 
      todo.content.toLowerCase().includes(search.toLowerCase()) //참이되는 
      //include => 해당 값이 일치하는지 찾아서 확인 
    )
  }

  const filteredTodos = getFilteredData()

  return (
    <div className='List'>
      <h4>
        Todo List🔍
      </h4>
        <input type="text" 
        value={search}
        onChange={onChangeSearch}
        placeholder='검색어를 입력하세요'/>
      <div className='todos_wrapper'>
        {filteredTodos.map((todo) => {
          //필터링된 투두스
          return <TodoItem 
          key={todo.id}
          {...todo} 
          onUpdate={onUpdate}
          onDelete={onDelete}/>
        })}
        {/* <TodoItem/>
        <TodoItem/>
        <TodoItem/> */}
      </div>  
    </div>
) 
}

export default List