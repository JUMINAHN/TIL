const todoForm = document.querySelector("#todo-form") // form
const todoInput = document.querySelector("#todo-form input") // input 태그 자체를 넣어야 함
const toDoList = document.querySelector("#todo-list") // ul

const TODOS_KEY = "toDos";

function deleteToDo(event) { 
  const li = event.target.parentElement; 
  console.log(li);   
  li.remove();
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

//만약 array에서 뭔가를 삭제할 떄,실제로 array에서 그것을 지우는 것이 아님
//실제로는 지우고 싶은 item을 빼고 새로운 array를 만드는 것임
//item을 제외하는 것, 즉 이전 array는 사실상 있는 것 == filter함수 사용

// function sexyFilter() { //forEach와 유사함

// }//이것은 반드시 true를 리턴해야 함
//새 array에서 해당 object를 유지하고 싶으면 반드시 true를 리턴해야 함

// [1,2,3,4].filter(sexyFilter); //filter는 sexyFilter를 부르고, 1234에 sexyfilter가 차례대로 실행될 것
//즉 sexyFilter의 함수가 할 일은 질문을 던지는 것임, item을 제외할지에 대한


// 사실상 하기 처럼 작동 -> true를 리턴하면 해당 값을 유지할 것
// sexyFilter(1); -> true일시 1 유지
// sexyFilter(2); -> true일시 2 유지
// sexyFilter(3); -> true일시 3 유지
// sexyFilter(4); -> true일시 4 유지