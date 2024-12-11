const loginForm = document.querySelector("#login-form")
const loginInput = document.querySelector("#login-form input")
const greeting = document.querySelector("#greeting")
const linkData = document.querySelector("a") 

const HIDDEN_CLASSNAME = "hidden";
//반복적으로 발생하는 내용 변수 설정하기 --> userName
const USERNAME_KEY = "username"; //오타로 발생할 수 있는 추가 이슈 사전 대응

//똑같은 작업 반복
function paintGreetings(userName) {
  greeting.innerText = `Hello ${userName}` //저장된 data를 반영할 것이기 떄문에
  greeting.classList.remove(HIDDEN_CLASSNAME); //form 삭제
}

function onLoginSubmit(event) {
  event.preventDefault(); 
  loginForm.classList.add(HIDDEN_CLASSNAME);
  const userName = loginInput.value;
  //greeting.innerText = `Hello ${userName}`

  //greeting.classList.remove(HIDDEN_CLASSNAME);
  paintGreetings(userName);
  localStorage.setItem(USERNAME_KEY, userName); //키와 값 적기
  console.log(userName);
}

//localStorage에 값이 없다면 null이 나옴
//값이 담기게 될 것
const savedUserName = localStorage.getItem(USERNAME_KEY); 
console.log(savedUserName);

//만약 userName이 없다면 form을 보여줄 것이고,
//userName이 있다면 화면에 나의 이름을 보여줄 것
//즉 local 정보에 userName이 없을떄 
if (savedUserName === null) {
  //form, greeting 자체를 모두 숨기고 시작한다.
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit", onLoginSubmit);
  //없으면 자체적으로 반영을 시킨다.
} else {
  //그게 아니라면 이름을 보여줄 것
  //show greetings
  const userName = loginInput.value;
  paintGreetings(savedUserName);
  //greeting.innerText = `Hello ${savedUserName}` //저장된 data를 반영할 것이기 떄문에
  //greeting.classList.remove(HIDDEN_CLASSNAME); //form 삭제
}


