// 단 하나의 event만 알아보고 싶다.
const title = document.getElementById("title");
// HTML을 자바스크립트에서 읽을 수 있도록 해주어야 함
// **핵심 : HTML에서 id를 통해 `element`를 찾아줌 !!
// 동작 원리를 이해할 것

title.innerText = "Got you!"
console.log(title.id);
console.log(title.className); // 현재는 아무 것도 없음
title.className = "hello";
console.log(title.className); // hello가 생성된 것을 확인할 수 있음
