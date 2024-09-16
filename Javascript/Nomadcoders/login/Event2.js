//현재 필요한 것은 login-form 자체 (input/btn 포함)
const loginForm = document.querySelector("#login-form")
const loginInput = document.querySelector("#login-form input")

const linkData = document.querySelector("a") //link data를 받아오기


function onLoginSubmit(event) {
  event.preventDefault(); //event의 기본 행동이 발생되지 않도록 막는 것
  console.log(loginInput.value);
}

//첫번쨰 argument에 데이터를 담아서 정보를 전달할 수 있음

//event의 종류는 다양함 mouseEvent, pointerEvent etc...
//유저가 어디를 클릭했는지도 확인할 수 있음
function handleLinkClick(event) {
  event.preventDefault(); //기본적인 것을 막고 있음
  //alert("move to course!")
  console.log(event);
  //브라우저가 동작을 하는것을 허용하지 않는다.
  //alert는 일시적으로 동작을 중지하도록 만듬
}




loginForm.addEventListener("submit", onLoginSubmit); //loginForm의 submit event를 listen
linkData.addEventListener("click", handleLinkClick) //click했을 때 handle event가 작동하지 않도록 만들고 싶음
//해당 함수를 실행시키는 것은 내가 아니고, 다른 유저가 js를 이용해서 동작시킴

// 즉 중요한 것은 ()는 브라우저가 실행을 하고
// 브라우저는 event에 대한 정보도 담아줄 것
// preventDefault를 호출하면 브라우저에 기본적인 것을 막아주는 역할을 수행할 것