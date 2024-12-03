import './List.css'
import TodoItem from './TodoItem'

//todos를 App에서 받아서 todoItem에게 전달
//현재 Todos에서 에러
const List = ({todo}) => {
  return (
    <div className="List">

      <div>Todos 🔍</div>
      <div className="ListSearch">
        <input type="text" 
        placeholder="검색어를 입력하세요" />
      </div>
      <div className="ListInput">
        {/* 기존 내용을 todoListItem으로 변환 */}
        <TodoItem 
        todo={todo}/>
      </div>

    </div>
  )
}

export default List 