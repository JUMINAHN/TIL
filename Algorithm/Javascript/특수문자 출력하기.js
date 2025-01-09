const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


//inline이 없는데?
// let input = []
// rl.on('line', function(line) { //on으로 line이라는 내용을 받아서 function으로 전달
//     input = [line]
// }) //해당 문제는 입력이 없다.
rl.on('close', function () {
    // str = input[0] //이게 없었음
    
    //그런데 (\로만은 오류가 뜸
    //console.log(`${!@#$%^&*(\'"<>?:;'}`) //이것도 아님
    //console.log('!@#$%^&*(\'"<>?:;') //지금 일단 )에 이상은 없음 => ''를 어떻게 인식하는 것인지?
    // console.log(`${!@#$%^&*(\\'"<>?:;}`) 
    // console.log(`!@#$%^&*(\\'"<>?:;`) 
    console.log("!@#$%^&*(\\\'\"<>?:;")  //결론적으로 \를 1개씩
    
})