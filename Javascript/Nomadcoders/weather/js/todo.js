const todoForm = document.querySelector("#todo-form") // form
const todoInput = document.querySelector("#todo-form input") // input 태그 자체를 넣어야 함
const toDoList = document.querySelector("#todo-list") // ul

const TODOS_KEY = "toDos";

function deleteToDo(event) { 
  const li = event.target.parentElement; 
  li.remove();
  toDos = toDos.filter((toDo) => toDo.id !== parseInt(li.id))
  

}

let toDos = []; 

function saveToDos() { 
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos));
}


function paintTodo(newTodoObj) {
  const li = document.createElement("li");
  li.id = newTodoObj.id;
  const span = document.createElement("span");
  span.innerText = newTodoObj.text; 
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

  const newTodoObj = { 
    text : newTodo,
    id : Date.now(), 
  };

  toDos.push(newTodoObj); 


  paintTodo(newTodoObj);
  saveToDos(); 
}

todoForm.addEventListener("submit", handleToDoSubmit)



const savedToDos = localStorage.getItem(TODOS_KEY);

if (savedToDos) {
  const parsedToDos = JSON.parse(savedToDos); 
  toDos = parsedToDos;

  parsedToDos.forEach(paintTodo); 

} 
