const todoForm = document.querySelector("#todo-form") // form
const todoInput = document.querySelector("#todo-form text") // input
const toDoList = document.querySelector("#todo-list") // ul

//새로 고침 event를 막을 것
function handleToDoSubmit(event) { //handle의 첫번쨰 인자로 준다.
  event.preventDefault();
  
  //submit을 할 때 input의 value를 얻어내고 싶은 것
  const inputValue = todoForm.value;
  console.log(inputValue); //undefined


  // null로 출력 됨
  // const inputValue = todoInput.value;
  // console.log(inputValue);
}

// form 자체에서 submit을 하면 새로 고침이 됨
todoForm.addEventListener("submit", handleToDoSubmit)

// 다음으로 input의 value를 얻어내고 싶을 떄,