//중요 point

//현재 필요한 것은 login-form 자체 (input/btn 포함)
const loginForm = document.querySelector("#login-form")
const loginInput = document.querySelector("#login-form input")


//해당 function에 대한 argument로 정보를 얻고있음 
//즉 발생한 일에 대해 우리가 필요로 할만한 정보를 제공하고 있음
//첫번째 argument에 대한 정보는 발생한 일에 대해 필요로 할만한 정보를 제공 ->js가 우리에게 제공
//즉 argument가 들어갈 공간을 제공하면 js가 알아서 필요한 데이터를 제공할 것

function onLoginSubmit(event) {
  //const userName = loginInput.value; //input 내부의 value를 확인하게 되면 받는 변수
  //console.log(userName);
  event.preventDefault(); //event의 기본 행동이 발생되지 않도록 막는 것
  //즉 새로 고침의 동작을 막고 있는 것
  console.log(loginInput.value);
  console.log(event);
}


//submit은 엔터를 누르거나 버튼을 클릭할 떄 발생한다는 것 유의
//form에 대한 submit event가 발생하는 것을 볼 수 있음
//즉 form을 submit할 떄 입력값을 받아내는 것
//브라우저는 submit할 때 새로고침할 수 있도록 만들어줌 --> 초기값임
//기본적으로 function ()는 즉시 실행한다는 것을 의미 함 : 브라우저가 자동으로 실행

//사실 실제는 addEventListener에서 onLoginSubmit을 호출하고,
//브라우저가 function을 실행시키고는 있음
//중요한 것은 function()안에서 argument로 나에게 정보를 제공하고 있다는 것!!
//실제로 비어있는 function을 호출하는 것이 아니라 argument에 추가적 정보를 가진채로 호출
//즉 브라우저내에서 event로 정보를 잡아내서 onLoginSubmit function 실행 버튼을 누르고 있음


//따라서 addEventListener을 봤을 떄는 바로 실행시키려고 하는 것은 아니다.
loginForm.addEventListener("submit", onLoginSubmit); //loginForm의 submit event를 listen

