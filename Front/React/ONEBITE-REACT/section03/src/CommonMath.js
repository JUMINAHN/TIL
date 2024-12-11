//math module

function add(a, b) {
  return a + b
}

function sub(a, b) {
  return a - b
}

//내보낼 값들 == commonJs
module.exports = { //키 밸류값이 똑같을 경우 => math로 내보내짐
  add,
  sub
} //객체로 내보냄

//ES Module system
//package.json >> type : module : esmodule을 설정하겠다.