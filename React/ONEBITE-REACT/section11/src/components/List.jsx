import { useContext, useMemo, useState } from 'react';
import './List.css';
import TodoItem from './TodoItem';
import { TodoStateContext } from '../App';


const List = () => {
  const todos = useContext(TodoStateContext) //구조분해X
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

  //computed같은건가?


  const {totalCount, doneCount, notDoneCount} = useMemo(() => {
    const totalCount = todos.length
    const doneCount = todos.filter((todo) => todo.isDone).length
    const notDoneCount = totalCount - doneCount

    return {
      totalCount,
      doneCount,
      notDoneCount
    }
  }, [todos])

//  const {totalCount, doneCount, notDoneCount} = getAnalyzedData()


  return (
    <div className='List'>
      <h4>
        Todo List🔍
      </h4>
      <div>total : {totalCount}</div>
      <div>done : {doneCount}</div>
      <div>notDone : {notDoneCount}</div>

        <input type="text" 
        value={search}
        onChange={onChangeSearch}
        placeholder='검색어를 입력하세요'/>
      <div className='todos_wrapper'>
        {filteredTodos.map((todo) => {
          //필터링된 투두스
          return <TodoItem 
          key={todo.id}
          {...todo} />
        })}
        {/* <TodoItem/>
        <TodoItem/>
        <TodoItem/> */}
      </div>  
    </div>
) 
}

export default List