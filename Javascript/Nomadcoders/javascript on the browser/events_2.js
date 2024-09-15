const title = document.querySelector(".hello2:first-child h1")
const title2 = document.querySelector("div.hello2:first-child h1") 

// js로 css를 변경할 수는 있지만, css는 직접 css에서 변경하는 것이 좋다.

console.dir(title2);
// property 앞에 on이 붙어있는 것들이 event이다.
// on은 작성하지 않고 click만 작성하면 된다.

function handleMouseEnter() {
  //console.log("mouse is here!");
  title2.innerHTML = "mouse is here!";
}

function handleMOuseLeave() {
  //console.log("mouse is gone!");
  title2.innerHTML = "mouse is gone!";
}

title2.addEventListener("mouseenter", handleMouseEnter);
title2.addEventListener("mouseleave", handleMOuseLeave);
// js가 대신 실행버튼을 눌러줄 것이다.
