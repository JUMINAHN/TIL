const todoForm = document.querySelector("#todo-form") // form
const todoInput = document.querySelector("#todo-form input") // input 태그 자체를 넣어야 함
const toDoList = document.querySelector("#todo-list") // ul

//to do list를 그릴 함수 선언
//즉 handleTodoSubmit이 paintTodo를 사용할 것
//즉 제출하면 todo를 그려줄 것
function paintTodo(newTodo) { //지금 그려야할 것이 무엇인지 모름 따라서 인자를 줌
  const li = document.createElement("li");
  // //하기에 span값과 btn값을 추가하고 싶음
  // //단순 list element를 사용할 시, btn 속성을 사용할 수 없는 문제
  
  const span = document.createElement("span");
  //해당 span 태그는 li 속성 하기에 있음
  li.appendChild(span); //하기에 자식을 가지게 됨
  //span 자체에 값을 넣어줄 것임
  span.innerText = newTodo; //사용자가 준 것
  toDoList.appendChild(li);
  //즉 현재는 새로고침하면 다양한 데이터는 날라가고 삭제할 수 없다는 문제가 있음
  

}



//새로 고침 event를 막을 것
function handleToDoSubmit(event) { 
  event.preventDefault();
  const newTodo = todoInput.value;
  todoInput.value = ""; 
  paintTodo(newTodo); //인자 값은 아까 value로 받은 내용이 들어감

}

todoForm.addEventListener("submit", handleToDoSubmit)

