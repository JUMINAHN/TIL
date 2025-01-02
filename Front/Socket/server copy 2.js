//Q. 왜 굳이 모듈과 express를 같이 혼용하는지 무슨 이유가 있는지?
import { Server } from "socket.io"
import express from "express" //express 내부의 값을 express로
import * as http from "http" //모든 Http 관련 내용 => Q.이거 왜이렇게 하는 것인지
import ViteExpress from "vite-express"
import cors from "cors"
//Q. 공식문서에서 어떤걸 가져올지에 대한 판단X => 이건 또 왜 App.jsx/

const app = express() //앱을 만들고
app.use(cors())
// const app = require("express")()
const server = http.createServer(app) //앱 기반으로 서버를 만든다
const io = new Server(server, {
  cors: {
    origin: "http://localhost:5173", // 클라이언트의 실제 주소로 변경
    methods: ["GET", "POST"],
    credentials: true,
    // origin: "*", // 모든 서버 핸들링
  },
}) //서버를 기반으로 socketIo를 만들었다.
// io.listen(3000)
// const server = require("http").createServer(app)
// const io = require("socket.io")(server) //서버를 기반으로 socketIo를 만들었다.
// server가 listen하기 때문에 io listen은 없어도 된다.
io.on("connection", (client) => {
  //on은 event handler가 적용이된다는 것 => connection이라는 헨들러가 들어오면 화살표 함수가 실행된다.
  //연결 & 끊겼을때
  console.log("server listen to 3000")
  // console.log("사용자가 들어왔습니다", client)
  console.log("사용자가 들어왔습니다")

  // 이 사용자에게 disconnect listener르 건다
  client.on("disconnect", () => {
    console.log("사용자가 나갔습니다.")
  })
})
// io.on("connection", (socket) => { //언제 App에서ㅓ
//   setTimeout(() => socket.disconnect(true), 5000);
//   console.log("사용자가 나갔습니다.")
// });
server.listen(3000) //3000으로 서버가 듣는다.
app.get("/message", (_, res) => res.send("Hello from express!")) //앱에 메세지가 들어오게 되면, hello from express가 들어오게 된다는 의미
app.get("/api", (_, res) => res.send("Hello from api!")) //앱에 메세지가 들어오게 되면, hello from express가 들어오게 된다는 의미
//get로 주소창을 받고 & response를 받게되면 response에 대한 응답을 보내주는 것

ViteExpress.bind(app, server) //앱이랑 서버가 같이 들을 수 있게끔 만들어준다.
//이걸 어떻게 알 수 있지? => 오만 공식문서를 다 봐야하나요? 어떻게 멀 보고 이렇게 판단해서 만드는건지 궁금
