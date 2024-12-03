import './TodoItem.css'
//매개변수로 todoListItem을 받아와야 함 
//어디서? List에서 

const TodoListItem = ({todo}) => {
  // const todos = [
  //   {id : 0, isDone : false, title:'REACT 공부하기', date:'Date'},
  //   {id : 1, isDone : false, title:'빨래 널기', date:'Date'},
  //   {id : 2, isDone : false, title:'노래 연습하기', date:'Date'}  
  // ]

  return(
    <div>
      {todo.map((todo) => (
        <div className="TodoItem"
        key={todo.id}>
          <input type="checkbox"
          />
          <h4>{todo.title}</h4>
          <h5>{todo.date}</h5>
          <button>삭제</button>          
        </div>
      ))}
    </div>
  )
}

export default TodoListItem