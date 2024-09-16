const loginForm = document.querySelector("#login-form");
//input이랑 button을 끌어오는 것 

//document자체에서 가져오는 것 대신, loginForm을 이용해서 해당 태그를 가져올 수 있음 
//element 자체를 긁어오는 것이기 떄문에, 그 중 해당 되는 element를 뽑아옴
const loginInput = loginForm.querySelector("input");
const loginButton = loginForm.querySelector("button");

//더 코드를 줄일 수 있는 방법
//document에서 바로 찾기
const loginInput2 = document.querySelector("#login-form input");
const loginButton2 = document.querySelector("login-form button");


//click event와 연결시켜주기

function clickTheButton() {
  console.dir("hello " + loginInput.value); //button과 관련된 tag요소들을 볼 수 있음
  //단, 아무런 값이 입력되지 않았을땐 보기 좋지 않음
  //현재 value : ""임을 확인할 수 있음
  //input-tag안에 아무런 value가 없기 떄문에
  console.log("click!!!");
}

loginButton.addEventListener("click", clickTheButton)
