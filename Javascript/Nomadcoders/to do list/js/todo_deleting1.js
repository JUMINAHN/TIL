const todoForm = document.querySelector("#todo-form") // form
const todoInput = document.querySelector("#todo-form input") // input 태그 자체를 넣어야 함
const toDoList = document.querySelector("#todo-list") // ul

const TODOS_KEY = "toDos";

//localStorage는 toDos array를 복사해두는 곳
//즉 toDos array가 local Storage와 같지 않음
//즉 main에서 toDos array를 모두 지워도 local Storage item 내에서 자체를 제거하고 싶은 것
//그러나 어떤 item을 지워야하는지 알 수 없음
//다만, js html입장에서는 li 태그를 삭제해야함을 알고 있음 (데이터 베이스는 어디서 삭제?)
//a가 2번있을떄 첫번째인지 두번쨰인지 알 수 없음
//따라서 랜덤으로 id값을 부여하는 것이 목표


function deleteToDo(event) { 
  const li = event.target.parentElement; //삭제하기 전에 list를 얻게 됨
  console.log(li);   //따라서 여기서 보면 list의 id를 얻을 수 있음
  li.remove();
}

let toDos = []; 

function saveToDos() { 
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos));
}


//to do list 만들기

//id가 생성된 이유는 id를 통해서 각각의 li item을 구분하고 싶었기 떄문
//그리고 그에 따라서 li내부에 있는 button의 id를 알아야 적절한 삭제가 가능해진다.
function paintTodo(newTodoObj) { //object를 받게 됨
  const li = document.createElement("li");
  li.id = newTodoObj.id; //list 자체의 id 속성 값을 넣는 것
  const span = document.createElement("span");
  span.innerText = newTodoObj.text; //이제 innerText는 단순 newTodo가 아니라 newTodo의 text를 받아야 함
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
  const newTodo = todoInput.value; //text
  todoInput.value = "";

  const newTodoObj = { //그리고 해당 값을 array에 담을 것
    text : newTodo,
    id : Date.now(), //밀리 초 단위로 나타나기 때문에 부여
  };

  toDos.push(newTodoObj);  //여기서 매번 데이터베이스로 사용자가 적어둔 text를 push함
  //이제는 object를 push하고 싶음
  //id를 html에 두고 싶음


  paintTodo(newTodoObj); //여기도 텍스트 대신에 obj를 준다.
  saveToDos(); 
}

todoForm.addEventListener("submit", handleToDoSubmit)



const savedToDos = localStorage.getItem(TODOS_KEY);

if (savedToDos) {
  const parsedToDos = JSON.parse(savedToDos); 
  toDos = parsedToDos;

  parsedToDos.forEach(paintTodo); 

} 