const loginForm = document.querySelector("#login-form")
const loginInput = document.querySelector("#login-form input")
const greeting = document.querySelector("#greeting")

const linkData = document.querySelector("a") 

//string만 포함된 변수는 대문자로 작성하는게 관습
//중복적으로 특정 값을 사용하는 경우 변수 선언
const HIDDEN_CLASSNAME = "hidden";


function onLoginSubmit(event) {
  event.preventDefault(); //event의 기본 행동이 발생되지 않도록 막는 것
  //console.log(loginInput.value);
  loginForm.classList.add(HIDDEN_CLASSNAME); //제출 버튼을 클릭하면, loginForm에 hidden이라는 클래스 이름을 넣어줄 것 -> from자체를 사라지게 만들 것
  const userName = loginInput.value; //input에 들어있는 value를 담아주는 변수
  //즉 console.log에 데이터는 기록이 남고, 원하는 바와 같이 사라지는 것을 확인할 수 있음
  
  //greeting.innerText = "Hello " + userName; 
  greeting.innerText = `Hello ${userName}`//python의 f_string과 비슷함
  
  //받은 data를 활용한 값을 나타내는 것

  greeting.classList.remove(HIDDEN_CLASSNAME);
  console.log(userName);
}



loginForm.addEventListener("submit", onLoginSubmit);