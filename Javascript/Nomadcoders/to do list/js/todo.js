const todoForm = document.querySelector("#todo-form") // form
const todoInput = document.querySelector("#todo-form input") // input 태그 자체를 넣어야 함
const toDoList = document.querySelector("#todo-list") // ul

const toDos = [];

function saveToDos() { // localStorage에 toDos값을 저장하는 것
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos)); //우리의 값을 string으로 저장하고 싶을 때 이걸 사용
  //단순한 string을 js로 바꿔질 수 있다. -> 살아 있는 배열로
}

//to do list 삭제하기
function deleteToDo(event) { 
  const li = event.target.parentElement; 
  li.remove();
}

//"todos"를 계속 사용하기 떄문에 상수로 선언
const TODOS_KEY = "toDos"


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

todoForm.addEventListener("submit", handleToDoSubmit);

function sayHello() {
  console.log("hello");
}

const savedToDos = localStorage.getItem(TODOS_KEY);
//그리고 해당 값은 가끔 null이 될 때도 있다.

//만약 savedToDos가 local에 있다면, 없다면
if (saveToDos !== null) {
  const parsedToDos = JSON.parse(saveToDos); //다시 배열화
  //즉 array에 있는 각각의 요소에 function을 실행
  //js는 array에 있는 각각의 item에 function을 실행할 수 있게 해준다.
  //array는 forEach라는 것을 가지고 있음
  parsedToDos.forEach(sayHello) //parseToDos가 가지고 있는 각각의 item에 대해 hello 실행
  //for each가 while같은 기능
} 