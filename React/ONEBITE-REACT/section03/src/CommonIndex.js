console.log('안녕 nodeJs') //node index.js => python sth 같은 느낌
//경로까지 같이 확인해줘야 한다.


//math module로 부터 sub, add를 내보내야 한다.
//내보내진
require("./CommonMath") //r그대로 반환
const moduleData = require("./CommonMath")
console.log(moduleData)
console.log(moduleData.add(1,2))
console.log(moduleData.sub(1,2))

//구조 분해 할당으로도 가능
//math module 자체에 있는 것들 구조 분해 할당 => 그 안의 요소들
//math module 내부에 있는 각각의 함수들
const {add, sub} = require("./CommonMath") //exports로 내보내진 내용
console.log(add(2,3))
console.log(sub(2,3))