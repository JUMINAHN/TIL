const clock = document.querySelector("h2#clock"); //해당 부분 유의
//#clock h1 이렇게는 내부에 있는 값에 접근할 때 사용되는 것
//일반적으로 태그 순서에 맞게 사용할 것, 띄워쓰기 유의
//querySelector에 대해 조금 더 이해할 필요가있음

//interval : 매번 일어나야하는 무언가
//주기적으로 무언가를 실행하고 싶을 때 -> 2초마다 주식시장을 확인하고 싶을때
//interval 호출

function sayHello() {
  console.log("hello~");
}

setInterval(sayHello, 5000); 
//실행할 함수를 첫번째 인자로 받고, 그 뒤로 5000 - 즉 5초에 한번씩 실행
//이것은 addEventListener와 약간 다름