const loginForm = document.querySelector("#login-form")
const loginInput = document.querySelector("#login-form input")
const greeting = document.querySelector("#greeting")
const linkData = document.querySelector("a") 

//prevent

const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username"; 

function paintGreetings() {
  const userName = localStorage.getItem(USERNAME_KEY);
  //local에 저장되면 호출하는 순간에 이미 userdata는 이미 저장되어 있을 것
  //local을 두번 열어보는 것
  greeting.innerText = `Hello ${userName}` 
  greeting.classList.remove(HIDDEN_CLASSNAME); }

function onLoginSubmit(event) {
  event.preventDefault(); 
  loginForm.classList.add(HIDDEN_CLASSNAME);
  //const userName = loginInput.value;

  paintGreetings();
  localStorage.setItem(USERNAME_KEY, userName); 
  console.log(userName);
}

const savedUserName = localStorage.getItem(USERNAME_KEY); 
//localstorange에 유저 정보가 존재하는 것을 알고 있다.

if (savedUserName === null) {
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit", onLoginSubmit);
} else {
  const userName = loginInput.value;
  paintGreetings();
}


