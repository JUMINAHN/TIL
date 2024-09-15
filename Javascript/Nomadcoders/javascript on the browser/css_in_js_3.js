const h1 = document.querySelector(".hello:first-child h1")

function handleTitleClick() {
  //className은 요소들을 모두 삭제하고, 새로 만들어 줌
  //다만 하기에 작성된 classList는 조금 다르게 작동 됨 -> 관련 함수도 있음
  const nowColor = h1.classList;
  //기존 변수의 내용을 잃어버릴수도 있는 문제를 야기함
  //따라서 className을 바꾸는 방법 중 -> class List를 사용

  // 하기 remove와 add를 활용할 수 있는 toggle
  h1.classList.toggle("active");  


  //const clickedClass = "active"; //이런식으로 버그를 피하기 위해 변수를 선언해줬을 떄
  // //해당 요소를 포함하고 있는지만 확인
  // if (nowColor.contains(clickedClass)) { //html element가 가지고 있는 또 다른 요소 사용
  //   h1.classList.remove(clickedClass); //활성화 내역을 없앨 것
  // } else {
  //   h1.classList.add(clickedClass); 
  // }
} 


h1.addEventListener("click", handleTitleClick);