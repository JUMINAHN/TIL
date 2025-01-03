import { Server } from "socket.io"
import { createServer } from "node:http"
import ViteExpress from "vite-express"
import express from "express"
import cors from "cors"
// cors 정책

const app = express()
app.use(cors())
const server = createServer(app)
const io = new Server(server, {
  cors: {
    origin: "http://localhost:5173",
    // allowedHeaders: "*",
    credentials: true,
  },
})

app.get("/message", (_, res) => res.send("Hello from express!")) //message 가져왔을 때
//client측 에서
//client가 연결되었을 때 => io socket에 연결되었을 때 => npm : socket.io 공식문서 활용

io.on("connection", (client) => {
  // 이름을 받아오기
  const loginUser = client.handshake.query.username
  console.log(`${loginUser} 님이 입장하였습니다.`)
  client.broadcast.emit(`${loginUser} 님이 입장하였습니다.`)
  io.emit("enter message", `관리자 : "${loginUser}" 님이 입장하였습니다.`)

  //  client의 메세지가 온다면 => 메세지를 출력할 것
  // 여기서 안들어오는데? chat
  client.on("chat message", (msg) => {
    //근데 이게 연결되었을 때 기준
    console.log("server에서 받은 client message: " + msg)
    io.emit("chat message", { username: loginUser, message: msg })
  })

  //disconnect => 연결 끊었을 때
  client.on("disconnect", () => {
    console.log(`${loginUser} 님이 퇴장하였습니다.`)
    io.emit("out message", `관리자 : "${loginUser}" 님이 퇴장하였습니다.`)
    // 전체 메세지 전송이 안되는데? => client console창에서 안했으니까?
  })
})
//port 3000
server.listen(3000, () => {
  console.log("sever running at http:localhost:3000")
})
ViteExpress.bind(app, server)
