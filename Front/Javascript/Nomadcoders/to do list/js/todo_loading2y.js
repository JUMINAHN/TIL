const todoForm = document.querySelector("#todo-form") // form
const todoInput = document.querySelector("#todo-form input") // input 태그 자체를 넣어야 함
const toDoList = document.querySelector("#todo-list") // ul

const TODOS_KEY = "toDos";

//단 현재 문제는 local에 data를 삭제해도 완벽한 삭제가 이루어지지 않았다는 점



//to do list 삭제하기
function deleteToDo(event) { 
  const li = event.target.parentElement; 
  li.remove();
}

let toDos = []; //application이 시작될 때 array가 항상 비어있기 떄문에
//값이 초기화되는 문제가 발생함 
//const를 let로 바꿔서 업데이트가 가능하도록 변경
//local에 todo가 있다면, todo를 복원

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
  toDos.push(newTodo); //새로 고침할때 빈 array에 push하게 됨
  paintTodo(newTodo); 
  saveToDos(); 
}

todoForm.addEventListener("submit", handleToDoSubmit)


//여기서 궁금한 것
//그냥 local에 있으면 그냥 새로고침해도 사라지지 않는 것?
//새로 고침해도 왜 local에서는 사라지지 않는 것인지?


//local에 있는 내용 저장
const savedToDos = localStorage.getItem(TODOS_KEY);

if (savedToDos) {
  const parsedToDos = JSON.parse(savedToDos); 
  toDos = parsedToDos; //배열에 값을 넣어준다. -> local에 값이 있을 경우 -> 유지

  parsedToDos.forEach(paintTodo); //실제로 painTodo를 순회하는 것
  //즉 하나하나에 painTodo를 적용할 것
  //즉 새로고침을 해도 화면에서 사라지지 않음
  //다만 새로고침을 하고 contents를 추가하면 예전 것을 덮어씌우는 문제가 있음
  //기존과 새로운 것 모두 유지하고 싶음

} 