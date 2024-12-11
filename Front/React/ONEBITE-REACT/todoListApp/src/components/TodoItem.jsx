import './TodoItem.css'


const TodoItem = ({todo, onChangeCheck, onDeleteData}) => {
  //onChangeCheck를 누르면 checked가 수정될 것
  const onChangeUpdate = (todo) => {
    console.log(todo)
    onChangeCheck(todo.id) //todo의 id를 전달해준다.
  }

  const onClickDelete = (todo) => {
    onDeleteData(todo.id)
  }

  //checked가 수정되어야 함
  return (
    <div className="TodoItem">
      <input 
        type="checkbox"
        onChange={()=>onChangeUpdate(todo)}
        checked={todo.isDone}
      />
      <h4>{todo.title}</h4>
      <h5>{new Date(todo.date).toLocaleDateString()}</h5>
      <button
      onClick={()=>onClickDelete(todo)}>삭제</button>          
    </div>
  )
}

export default TodoItem