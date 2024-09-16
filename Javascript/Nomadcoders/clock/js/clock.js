const clock = document.querySelector("h2#clock"); 

function getClock() {
  const date = new Date(); 

  //내장 함수 자체가 조건이 포함되어 있는 것이기 때문에 내장 함수 모듈을 잘 활용하자
  const hours = String(date.getHours()).padStart(2, "0"); //해당 값은 numbers
  const minutes = String(date.getMinutes()).padStart(2, "0");
  const seconds = String(date.getSeconds()).padStart(2, "0");

  
  console.log(`${hours} : ${minutes} : ${seconds}`);
  clock.innerText = `${hours} : ${minutes} : ${seconds}`;

}

//padStart()라는 함수 알아보기
//string에 쓸 수 있는 function

//"1".padStart(2, "0");
//즉 자리수가 2일 때, 두자리 수를 넘지 않으면 0을 앞에 붙인다는 의미
//반대로 padEnd는 반대로 뒷자리를 채우는 것을 의미

getClock(); 

setInterval(getClock, 1000); 
