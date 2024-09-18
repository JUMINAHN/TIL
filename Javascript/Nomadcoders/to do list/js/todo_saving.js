const todoForm = document.querySelector("#todo-form") // form
const todoInput = document.querySelector("#todo-form input") // input 태그 자체를 넣어야 함
const toDoList = document.querySelector("#todo-list") // ul

//to do list 삭제하기
function deleteToDo(event) { 
  const li = event.target.parentElement; 
  li.remove();
}

//to do list 저장하기 == 새로 고침하면 사라짐
//데이터를 저장하기 위해서 localStorage에 등록해주어야 함
//즉 투두리스트를 만들고 불러와야 함
//단순 setItem을 하면 계속적으로 내용이 초기화 됨

//todo와 관련된 배열을 만들어 주어야 함 
//즉 newTodo가 그려질때마다 배열에 push를 해주어야 함
//즉 이 toDos를 localStorage에 등록해주어야 함

//단 localStorage에 array를 저장할 수 없음 -> text로 저장은 됨
const toDos = [];
//const는 업데이트할 수 없다. 다만, 배열은 업데이트가 가능하다.
//즉 배열 자체가 참조형이기 때문에 이러한 상황이 가능한 것


function saveToDos() { // localStorage에 toDos값을 저장하는 것
  localStorage.setItem("toDos", JSON.stringify(toDos)); //배열로 저장가능
  //stringify == 변수등을 문자열로 바꿈
  //parse == 문자열을 json으로 바꿈
  //즉 stringify로 array 자체를 문자열로 바꾸고
  //local에서 가지고 온 다음 문자열을 array로 만들어서 불려들이는 느낌

  //localStorage안에는 배열은 저장되지 않고, `텍스트만 저장`된다.
  //즉 스트링 형태로 저장이된다.
  //따라서 json.stringify를 이용해서 배열 형태로 저장시켜준다. 
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
  toDos.push(newTodo); //해당 값을 배열에 담을 수 있음
  paintTodo(newTodo); //값을 모두 집어넣고 saveTodos를 한다.
  saveToDos();



  //그러면 여기에 localStorage에 담을 데이터를 넣고
  //if와 else로 구분해줌 -> 즉 list가 있다면, 즉 localstorage의 값이 있다면
}

todoForm.addEventListener("submit", handleToDoSubmit)

