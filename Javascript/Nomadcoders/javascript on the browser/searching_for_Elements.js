const title = document.getElementsByTagName("h1");
// 모든 h1을 가져오는 것
// h1이 들어있는 배열이 나오는 것을 확인할 수 있음

console.log(title);


// 단 하나의 요소
const title2 = document.querySelector(".hello h1");
// element를 css방식으로 검색할 수 있음
// class hello를 찾고 -> 내부에 있는 h1 태그를 가져올 수 있음
// 즉 클래스를 찾고, 특정 태그 요소를 찾아올 수 있음

// 단 하나의 element를 return 해준다.
console.log(title2);


// 하나의 요소만 출력 됨
// 모든 조건에 성립이 되지만, 첫번쨰 element만 가져오게 된다.
const title4 = document.querySelector(".hello2 h1");
console.log(title4);

// 또 다른 방법으로 여러 요소 중 첫번쨰만 가져오고 싶을 떄
const mini = document.querySelector(".hello2 h1:first-child");
console.log(mini); //<h1>Grab me!</h1>

// 여러 요소
const title3 = document.querySelectorAll(".hello2 h1");
console.log(title3); //NodeList(3) [h1, h1, h1]
