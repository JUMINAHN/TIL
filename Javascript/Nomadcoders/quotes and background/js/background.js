const images = [
  "img1.jpg",
  "img2.jpg",
  "img3.jpg"
]; //img 폴더에 있는 이미지들이랑 이름을 통일 시켜주면 됨


const chosenImg = images[Math.floor(Math.random()*images.length)]
//math모듈은 3까지 작성을 했을떄 3을 미포함한다는 특징이 있다.
//따라서 length-1을 하지 않아도 되는 것
//undefine 발견되는 이유는 round를 할떄 3이 나오는 문제 때문이다.

console.log(chosenImg);

//랜덤 이미지를 가져오기
//이때까지 html에서 가져오는 것
//즉 getElementID, className, query etc ..
//js에서 생성해서 html에 반영해본적은 없음

//목표는 div 태그 밑에 img src를 넣어주는 것
//create sth 진행할 것
const bgImg = document.createElement("img"); //Element를 만들겠다는 의미
//img 태그가 있다면 src에 접근 가능
bgImg.src = `/quotes and background/img/${chosenImg}`; //랜덤한 이미지 명
//해당 값에 값을 넣어주는 것이기 떄문에
console.log(bgImg);

//끝으로 해당 img를 body 내부에 추가해주어야 함
document.body.appendChild(bgImg); //body에 하위 속성으로 html을 추가해주는 것