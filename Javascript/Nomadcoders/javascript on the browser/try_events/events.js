// 첫 번째 색깔 바꾸기
const clickMe = document.querySelector(".hello1 h1:first-child");

function changeColor() {
  clickMe.style.color = "red";
}

clickMe.addEventListener("click", changeColor) //자동으로 되도록 한다.


// 두 번째 바꿔보기
// 그런데 지금 두번째 태그를 실행하고 싶은데도 불구하고, 첫번째 tag만 작동이 되는 듯함
// 그 이유는 addEventListener() 메서드를 전역적으로 사용하기 떄문에
// 즉 -> addEventListener("mouseenter", mouseEnter); 로만 사용하는 문제 발견



// 하기는 버블링이 발동됨 : 자식에서 발동되는 것이 부모에게도 작용이 되는 것
const touchMe = document.querySelector(".hello1 h2");

function mouseEnter() {
  console.log("Hi mouse! I see you");
}

touchMe.addEventListener("mouseover", mouseEnter);

const newD = document.querySelector(".hello1 h3");
function newDAction() {
  console.log("mouse out!");
}

newD.addEventListener("mouseout", newDAction);

