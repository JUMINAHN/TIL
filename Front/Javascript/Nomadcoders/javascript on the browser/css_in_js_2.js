const h1 = document.querySelector(".hello:first-child h1")
// function handleTitleClick() { //h1에 active 클래스를 전달하고 싶을 때 (style.css참고)
//   h1.className = "active"; //js가 직접 css를 변경한 것은 아님 -> css자체에 접근
//   console.log(h1.className)

// } 

// 색깔을 blue, tomato를 적절하게 섞고 싶을 떄
// 단 해당 코드에서 string은 2번 사용되고 있다는 문제 -> error발생 위험이 있음(정확하게 작성)
// ex)nowColor === "active"
// 따라서 raw string을 사용하는 대신에 새로운 변수를 선언해주는게 좋음

function handleTitleClick() {
  const nowColor = h1.className;
  const clickedClass = "active";
  let changeColor;
  if (nowColor === clickedClass) {
    changeColor = ""
  } else {
    changeColor = clickedClass; //js가 직접 css를 변경한 것은 아님
  }
  h1.className = changeColor;
} 


h1.addEventListener("click", handleTitleClick);