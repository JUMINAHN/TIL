const todoForm = document.querySelector("#todo-form") // form
const todoInput = document.querySelector("#todo-form input") // input 태그 자체를 넣어야 함
const toDoList = document.querySelector("#todo-list") // ul

const TODOS_KEY = "toDos";


//현재는 아직까지도 localStorage에 값은 남아있지만, 화면에는 나타나지 않음
//값을 string으로 저장하고 싶을 때 : stringify를 많이 사용할 것
//이 string을 json 형태로도 변환할 수 있음 : Json.parse로

//to do list 삭제하기
function deleteToDo(event) { 
  const li = event.target.parentElement; 
  li.remove();
}

const toDos = [];

function saveToDos() { 
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos));
}


//to do list 만들기
function paintTodo(newTodo) { 
  const li = document.createElement("li");
  const span = document.createElement("span");
  span.innerText = newTodo; 
  const button = document.createElement("button");
  button.innerText = "❌";
  button.addEventListener("click", deleteToDo); //click을 할 때 todo를 삭제할 것

  li.appendChild(span);   
  li.appendChild(button); 

  toDoList.appendChild(li);
}


//새로 고침 event를 막을 것
function handleToDoSubmit(event) { 
  event.preventDefault();
  const newTodo = todoInput.value;
  todoInput.value = ""; 
  toDos.push(newTodo); 
  paintTodo(newTodo); 
  saveToDos(); 
}

todoForm.addEventListener("submit", handleToDoSubmit)

// function sayHello(item) {
//   console.log("this is the turn of", item);
// }


//local에 있는 내용 저장
const savedToDos = localStorage.getItem(TODOS_KEY);
//savedToDos가 null이거나 아닐 수 있다.
//null이라는 것은 배열에 아무런 값을 받지 않은 초기상황일 때

//만약 savedToDos가 local에 존재한다면, json으로 다시 변환할 것
if (savedToDos) {
  //saveToDos 함수랑 구분할 것
  const parsedToDos = JSON.parse(savedToDos); //local에 있는 내용을 변환하는 것
  //array가 됨
  //js는 array에 있는 각각의 item에 대해 function을 실행할 수 있도록 한다.
  //foreach는 while과 for과 같은 사용용도
  
  //parsedToDos.forEach(sayHello);
  //단 가장 중요한 것은 함수를 처리하고 있는 item이 무엇인지 아는게 중요함

  //짧게하는 단축, shortcut도 있음
  //즉 function을 만드는 대신 item을 가지고 console.log를 하는 것
  parsedToDos.forEach((item) => console.log("this is the turn of", item))


} else {

}