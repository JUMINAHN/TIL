import { memo } from 'react';
import './TodoItem.css';

const TodoItem = ({id, isDone, content, date, onUpdate, onDelete}) => {

  const onChangeCheckbox = () => {
    onUpdate(id)
  }

  const onClickDeleteButton = () => {
    onDelete(id)
  }

  return (
    <div className="TodoItem">
      <input readOnly checked={isDone} type="checkbox" 
      onChange={onChangeCheckbox}/>
      <div className="content">{content}</div>
      <div className="date">{new Date(date).toLocaleDateString()}</div>
      <button onClick={onClickDeleteButton}>삭제</button>
    </div>
  )
}

const memoizedTodoItem = memo(TodoItem) //memo는 객체 타입에 얕은 비교를 하기 떄문에 귀찮음 => 하나하나 비교 귀찮음

export default memo(TodoItem)
//고차 컴포넌트 (HOC)
// export default memo(TodoItem, (prevProps, nexProps) => {
//   //반환값에 따라 props가 바뀌었는지 안바뀌었는지 판단
//   //True => props가 바뀌지 않음 : 리랜더링X
//   //False => props가 바뀜 : 리랜더링 O
//   if(prevProps.id !== nexProps.id) return false
//   if(prevProps.isDone !== nexProps.isDone) return false
//   if(prevProps.content !== nexProps.content) return false
//   if(prevProps.date !== nexProps.date) return false
//   return true
// })