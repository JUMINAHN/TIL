const clock = document.querySelector("h2#clock"); 

//Interval
//~초마다 실행
//setInterval(sayHello, 5000); 
//즉 뭔가를 다시 실행하고 싶을 때 사용

function getClock() {
  const date = new Date(); //시, 분, 초 추출을 위해 객체 생성
  //시, 분, 초 추출
  //단순히 getHours를 하면 되는 것이 아님, ()를 붙여줘야 함 해당 부분 유의
  //즉 새로운 object를 만들고 있음
  //당장 보기에는 0초를 띄고는 있지만 00를 만들고 싶음
  //그리고 초가 바로 뜨지 않는 문제를 확인할 수 있음 -> 1초 지연

  console.log(`${date.getHours()} : ${date.getMinutes()} : ${date.getSeconds()}`)
  //따라서 이 데이터 내용을 h2 tag안으로 넣을 수 있게 해야 함
  clock.innerText = `${date.getHours()} : ${date.getMinutes()} : ${date.getSeconds()}`
  //반영해줘야할 곳 명확하게 표기하기

  //근데 왜 그냥 console.log에 date.getSeconds를 하면 안되는 것인지?
  //문자를 깔끔하게 연결 시키지 못함
  //console.log(date.getMinutes(), date.getSeconds());
}

//웹사이트가 load되자말자 getclock을 실행하고, 매초마다 다시 실행될 수 있도록
getClock(); //getclock을 즉시호출하고

//매초마다 getclock을 다시실행하고 있음
setInterval(getClock, 1000); //매초마다 실행




//TImeout
//시간이 ~만큼 흐른 뒤 실행하는 것
//setTimeout(sayHello, 5000);
//호출하려고 하는 function을 먼저 넣는다.
//얼마나 기다릴지 넣는다.