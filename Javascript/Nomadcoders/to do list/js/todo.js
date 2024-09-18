const todoForm = document.querySelector("#todo-form") // form
const todoInput = document.querySelector("#todo-form input") // input 태그 자체를 넣어야 함
const toDoList = document.querySelector("#todo-list") // ul

//to do list 삭제하기
function deleteToDo(event) { 
  const li = event.target.parentElement(); 
  li.remove();
}

const toDos = [];

function saveToDos() { // localStorage에 toDos값을 저장하는 것
  localStorage.setItem("toDos", JSON.stringify(toDos)); 



}


//to do list 만들기
function paintTodo(newTodo) { 
  const li = document.createElement("li");
  const span = document.createElement("span");
  span.innerText = newTodo; 
  const button = document.createElement("button");
  button.innerText = "❌";
  button.addEventListener("click", deleteToDo);

  li.appendChild(span);   
  li.appendChild(button); 

  toDoList.appendChild(li);
}



//새로 고침 event를 막을 것
function handleToDoSubmit(event) { 
  event.preventDefault();
  const newTodo = todoInput.value;
  todoInput.value = ""; 
  toDos.push(newTodo); //해당 값을 배열에 담을 수 있음

  paintTodo(newTodo); //값을 모두 집어넣고 saveTodos를 한다.
  saveToDos();



 
}

todoForm.addEventListener("submit", handleToDoSubmit)

