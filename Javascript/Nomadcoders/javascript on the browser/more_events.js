const title = document.querySelector(".hello2:first-child h1")
const h1 = document.querySelector("div.hello2:first-child h1") 

function handleMouseEnter() {
  h1.innerHTML = "mouse is here!";
}

function handleMOuseLeave() {
  h1.innerHTML = "mouse is gone!";
}

h1.addEventListener("mouseenter", handleMouseEnter);
h1.addEventListener("mouseleave", handleMOuseLeave);


// more_events
// window는 자체적으로 제공하는 변수
function handleWindowResize() { //화면 크기가 바뀜
  document.body.style.backgroundColor = "tomato";

}
window.addEventListener("resize", handleWindowResize);
// h1자체는 resize할 수 없지만, window는 resize가능

function handleWindowCopy() {
  alert("copier!");
}
window.addEventListener("copy", handleWindowCopy);
// window는 브라우저 탭에 존재하는 자바스크립트 전역 최상위 객체이다. 
// 쉽게 말하면 브라우저의 창이고 어디서든 접근이 가능하다. 

// document는 window 객체의 속성으로 브라우저 창의 HTML 문서 객체다. 
// 즉, window 객체 안에 document 객체가 존재한다


// 와이파이 관련 events
function handleWindowOffline() {
  alert("sos no wifi");
}

function handleWindowOnline() {
  alert("find wifi!");
}

window.addEventListener("offline", handleWindowOffline);
window.addEventListener("online", handleWindowOnline);