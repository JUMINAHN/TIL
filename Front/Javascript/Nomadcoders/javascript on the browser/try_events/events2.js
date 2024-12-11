//how can I use? -> 사용 실패
// const intro1 = document.querySelector(".intro1 h1");
// function animationevent() {
//   console.log("moving font!");
// }
// intro1.addEventListener("animationstart", animationevent)
// addEventListener()

//find inner
const findInner = document.querySelector(".intro1");
console.dir(findInner);

//copy
//paste
const intro1 = document.querySelector(".intro1 h1");
function copycontents() {
  console.log("U copy data!");
}
intro1.addEventListener("copy", copycontents)

//dbclick
const intro2 = document.querySelector(".intro2 h2");
function find2click() {
  intro2.innerHTML = "change -> Double Click!";
}
intro2.addEventListener("dblclick", find2click);

//drag
const intro3 = document.querySelector(".intro3 h3");
function dragData() {
  console.log("drag your data!");
}
intro3.addEventListener("drag", dragData)

//scroll
const intro4 = document.querySelector(".intro4 h4");
function scrollpage() {
  intro4.innerHTML = "U scroll page?";
}
intro4.addEventListener("scroll", scrollpage);

//wheel