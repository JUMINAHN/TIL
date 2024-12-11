const todoForm = document.querySelector("#todo-form") // form
const todoInput = document.querySelector("#todo-form input") // input 태그 자체를 넣어야 함
const toDoList = document.querySelector("#todo-list") // ul

const TODOS_KEY = "toDos";

function deleteToDo(event) { 
  const li = event.target.parentElement; 
  //console.log(li);  //삭제할때도 toDos의 localStorage를 업데이트 해주어야 함
  li.remove();
  toDos = toDos.filter((toDo) => toDo.id !== parseInt(li.id)) //클릭했던 li의 id를 갖고 있는 toDo를 지우고 싶음
  //여기 확인 중요
  //즉 우리가 클릭한 것을 제외한 todo를 남겨두고 싶은 것
  //지운뒤에 지운 데이터를 저장
  saveToDos();

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

//중요한 점은 filter function이 새 array를 주는 것을 기억하는 것
//즉 기존값은 유지하고 새로운 값을 return으로 반환한다.