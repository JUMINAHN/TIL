const loginForm = document.querySelector("#login-form")
const loginInput = document.querySelector("#login-form input")
const greeting = document.querySelector("#greeting")
const linkData = document.querySelector("a") 

const HIDDEN_CLASSNAME = "hidden";

//사용자에게 받은 input value를 저장하는 방법 == 기억하기
//브라우저가 기억할 수 있는 기능 == localStorage
//localStorage를 보고싶으면 개발자 tool을 확인하면 됨_application의 localstroage


//단 하기처럼 진행해도 DB에는 데이터가 저장되어있지만, form이 남아있는 문제가 있음
function onLoginSubmit(event) {
  event.preventDefault(); 
  loginForm.classList.add(HIDDEN_CLASSNAME);
  const userName = loginInput.value;
  greeting.innerText = `Hello ${userName}`
  //유저가 이름을 제출할 때 그 것을 저장하는 것
  localStorage.setItem("username", userName); //키와 값 적기
  greeting.classList.remove(HIDDEN_CLASSNAME);
  console.log(userName);
}



loginForm.addEventListener("submit", onLoginSubmit);