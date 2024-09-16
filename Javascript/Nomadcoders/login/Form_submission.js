const loginForm = document.querySelector("#login-form");

const loginInput = loginForm.querySelector("input");
const loginButton = loginForm.querySelector("button");



function clickTheButton() {
  const userName = loginInput.value;
  //브라우저가 돕고 있음
  //userName을 받는다는 것을 확d인하기 위해서 console.log를 남겨서 확인
  console.log(userName);
}

loginButton.addEventListener("click", clickTheButton)
