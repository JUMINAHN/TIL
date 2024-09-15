const title = document.querySelector(".hello2:first-child h1")
const title2 = document.querySelector("div.hello2:first-child h1") 
// div태그 안의 hello2의 first child h1 tag
// css selector 전달 가능

// element의 내부를 보고 싶다면 dir 사용
console.dir(title2);

// 또 다른 태그 호출 방법
// .hello h1
// .hello2 h1:first-child

//title2.style.color = "blue";
// title2로 해당 element 접근
// style요소가 있는 것을 확인 -> style요소의 color에 접근
// js로 변경 가능

//event란? : click을 하는 것도 event => js는 이벤트를 listen할 수 
function handleTitleClick() {
  //console.log("title was clicked!");
  title2.style.color = "blue";
}
title2.addEventListener("click", handleTitleClick) //무엇을 listen하고 싶은지 적기
// event를 listen하고, 작동할 function을 js로 넘겨준다. (events를 호출할 곳)
// 직접 실행 버튼을 누르지 않고, 유저가 실행할 때 직접 누를 수 있도록 동작