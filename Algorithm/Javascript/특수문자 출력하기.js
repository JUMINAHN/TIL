const readline = require("readline")
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

rl.on("close", function () {
  console.log("!@#$%^&*(\\'\"<>?:;") //결론적으로 \를 1개씩
})
