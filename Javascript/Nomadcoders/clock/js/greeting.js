const loginForm = document.querySelector("#login-form")
const loginInput = document.querySelector("#login-form input")
const greeting = document.querySelector("#greeting")
const linkData = document.querySelector("a") 

const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username"; 

function paintGreetings() {
  const userName = localStorage.getItem(USERNAME_KEY);

  greeting.innerText = `Hello ${userName}` 
  greeting.classList.remove(HIDDEN_CLASSNAME); }

function onLoginSubmit(event) {
  event.preventDefault(); 
  loginForm.classList.add(HIDDEN_CLASSNAME);

  paintGreetings();
  localStorage.setItem(USERNAME_KEY, userName); 
  console.log(userName);
}

const savedUserName = localStorage.getItem(USERNAME_KEY); 

if (savedUserName === null) {
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit", onLoginSubmit);
} else {
  const userName = loginInput.value;
  paintGreetings();
}


