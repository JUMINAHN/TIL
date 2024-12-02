
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

export default TodoItem