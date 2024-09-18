const todoForm = document.querySelector("#todo-form") // form
const todoInput = document.querySelector("#todo-form input") // input 태그 자체를 넣어야 함
const toDoList = document.querySelector("#todo-list") // ul


//todo를 삭제하는 버튼을 만드는 것이 목표

//button이 클릭될 때, 모두 같은 event를 기다리고 있고, 같은 function을 실행하고 있음
function deleteToDo(event) { //클릭에도 event 정보를 받아볼 수 있음
  //console.log(event) //parentNode, parentElement확인 -> Null인 경우 다시 확인
  //무엇이 부모인지 알 수 있음

  //target은 클릭된 HTML element
  //console.dir(event.target.parentElement); //부모 확인 -> element의 부모
  //console.dir(event.target.parentElement.innerText); //무엇이 선택되었는지도 알 수 있음
  
  //삭제하고 싶은 target
  const li = event.target.parentElement(); //event는 target을 줄 것 -> target이 부모를 주고
  li.remove(); // 삭제하기

  //내부의 path를 보고 싶어도 나오지 않을 경우 하기 메서드 사용
  //console.log(event.composedPath());

}


function paintTodo(newTodo) { 
  const li = document.createElement("li");
  const span = document.createElement("span");
  span.innerText = newTodo; 
  const button = document.createElement("button");
  //button을 가리킬 text를 넣어주어야 함
  button.innerText = "❌";
  button.addEventListener("click", deleteToDo); //click을 할 때 todo를 삭제할 것
  //그런데 다 같은 click을 가리키고 있음, 어떤 btn이 클릭되었는지를 알 수 없음

  li.appendChild(span);   
  li.appendChild(button); //아무런 동작요소를 넣지 않았기 떄문에 작동하지 않음
  //따라서 클릭했음을 알게하고, 그에 따른 event를 작동하게 한다.



  toDoList.appendChild(li);

}


//새로 고침 event를 막을 것
function handleToDoSubmit(event) { 
  event.preventDefault();
  const newTodo = todoInput.value;
  todoInput.value = ""; 
  paintTodo(newTodo); 
}

todoForm.addEventListener("submit", handleToDoSubmit)

