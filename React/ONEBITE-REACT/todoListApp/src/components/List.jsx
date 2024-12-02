import './List.css'

const List = () => {
  const todos = [
    {id : 0, isDone : false, title:'REACT 공부하기', date:new Date().getDate().toString()},
    {id : 1, isDone : false, title:'빨래 널기', date:new Date().getDate().toString()},
    {id : 2, isDone : false, title:'노래 연습하기', date:new Date().getDate().toString()}
  ]

  return (
    <div className="List">
      <div>Todos 🔍</div>
      <div className="ListSearch">
        <input type="text" 
        placeholder="검색어를 입력하세요" />
      </div>
      <div className="ListInput">
        {/* filter는 안되는지? */}
        {/* 또 헷갈리는 ({}) */}
        {/* ()로는 원하는게 나오는데 {}로는 안나옴*/}
        {todos.map((todo) => (
          <div className='ListDetail'
          key={todo.id}>
            <input type="checkbox"
            />
            <h4>{todo.title}</h4>
            <h5>{todo.date}</h5>
            <button>삭제</button>          
          </div>
        ))}
      </div>
    </div>
  )
}

export default List 