import { useState } from 'react'
import './List.css'
import TodoItem from './TodoItem'

const List = ({todo, onUpdateTodo, onDeleteTodo}) => {
  const [search, setSearch] = useState('')

  const onChangeSearch = (e) => {
    // console.log(e.target.value)
    setSearch(e.target.value)
  }
  
  //궁극적으로 todos APp에서 받아온 todo에 있는 isDone을 true로 해줘야한다는 것
  //어디에 영향을 줘야하는건가? => onUpdateTOdo에 값을 줘야 함
  //그럼 checkbox의 일치여부를 판단해줘야 함
  const onChangeCheck = (checkId) => {
    //일단 checkID 테스트
    console.log(checkId, 'onChangeCheck까지 들어옴 => 확인 완료')
    onUpdateTodo(checkId)
  }

  const onDeleteData = (checkId) => {
    console.log(checkId, 'onDeleteData까지 들어옴 => 확인 완료')
    onDeleteTodo(checkId)
  }


  const searchFilter = (search) => { //참인것만 반환
    //애초에 그런데 강의에서는 === ''인것으로 설정함
    return todo.filter((item) => item.title.toLowerCase().includes(search.toLowerCase()))
  }//참인 데이터만 반환

  return (
    <div className="List">
      <div>Todos 🔍</div>
      <div className="ListSearch">
        <input type="text" 
        value={search}
        placeholder="검색어를 입력하세요" 
        onChange={onChangeSearch}/>
      </div>
      <div className="ListInput">
        {searchFilter(search).map((item) => (
          <TodoItem 
            key={item.id}
            todo={item}
            onChangeCheck={onChangeCheck}
            onDeleteData={onDeleteData}
          />
        ))}
      </div>
    </div>
  )
}

export default List