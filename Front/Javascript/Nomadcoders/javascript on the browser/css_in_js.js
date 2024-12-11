const title = document.querySelector(".hello2:first-child h1")
const h1 = document.querySelector("div.hello2:first-child h1") 

// function handleTitleClick() {
//   console.log(h1.style.color); //getter
//   h1.style.color = "blue";
//   console.log(h1.style.color); //setter
// }


//만약 blue라면 -> tomato로 바꿔주시고,
//blue가 아니라면 -> blue로 바꿔주세요
//더 깔끔한 코드를 위해서 변수를 지정해주는 것이 좋음
//let을 설정하니까 바뀌지 않음
//const를 설정하니까 
//css_in_js.js:23 Uncaught TypeError: Assignment to constant variable.


// 이 코드를 함수 밖에 두면, 처음 페이지가 로드될 때
// 단 한 번만 h1.style.color가 설정되고 이후로는 업데이트되지 않으므로, 
//클릭할 때마다 그 값이 갱신되지 않는다. 
function handleTitleClick() {
  const currentColor = h1.style.color; //click할때 해당 값들이 적용되기 떄문에 밖에 있으면 안됨
  let newColor;  
  //여기서 ===는 3개의 값이 일치하는지 확인하기 위함
  //h1의 color값이 blue와 일치하는지 확인
  if (currentColor === "blue") { //색상도 ""로 맞게 표기
    newColor = "tomato"; //변수 자체에 값을 넣는 것이기 떄문에
  } else {
    newColor = "blue";
  }
  //이렇게 변경해보았자 h1 color에 아무 영향도 미치지 않는 것을 확인할 수 있음
  h1.style.color = newColor; //실제 h1.style.color에 해당 값을 넣어줘야 함
} //실제에서는 비선호

h1.addEventListener("click", handleTitleClick);