const todoForm = document.querySelector("#todo-form") // form
const todoInput = document.querySelector("#todo-form input") // input 태그 자체를 넣어야 함
//text로 작성하면 오류가 발생함
//const toDoInput = todoForm.querySelector("input")
const toDoList = document.querySelector("#todo-list") // ul

//새로 고침 event를 막을 것
function handleToDoSubmit(event) { //handle의 첫번쨰 인자로 준다.
  event.preventDefault();

// 다음으로 input의 value를 얻어내고 싶을 떄,

  const newTodo = todoInput.value;
  // const inputValue = todoInput.value; 
  // console.log(inputValue);

  //enter를 누를 때 마다 입력값이 사라지게 만들고 싶음
  //todoinput의 value에 빈 값을 넣어줌
  todoInput.value = ""; //단 이 것은 값을 저장하지 못함
}

// form 자체에서 submit을 하면 새로 고침이 됨
todoForm.addEventListener("submit", handleToDoSubmit)

