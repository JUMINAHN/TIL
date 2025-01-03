import { Server } from "socket.io"
import express from "express"
import { createServer } from "node:http"
import ViteExpress from "vite-express"
import cors from "cors"

const app = express()
app.use(cors())
const server = createServer(app)
const io = new Server(server, {
  cors: {
    origin: "http://localhost:5173", //client의 주소
    methods: ["GET", "POST"],
    credentials: true,
  },
})
//매개변수 client / socket 모두 가능
io.on("connection", (client) => {
  //클라이언트가 연결되었을 때
  // console.log(client) //name은 주소. rooms : map으로 되어있고, id가 있고. nameSpace있고,clients 이쏙,
  //query에 원하는 데이터를 넣을 수 있음
  const enterUserName = client.handshake.query.nickName //이 부분
  console.log(`${enterUserName}가 입장하였습니다. 박수로 환영해주세요!`)

  // 모든 사람에게 전달 => Q. 해당 내용?
  // client.broadcast.emit("new message", { username: "관리자", message: `${enterUserName}님이 방에 들어왔습니다.` })
  io.emit("new message", { username: "관리자", message: `${enterUserName}님이 방에 들어왔습니다.` });

  client.on("new message", (msg) => {
    console.log(`${enterUserName} : `, msg)
    io.emit("new message", { username: msg.username, message: msg.message })
  })
  //else
  client.on("disconnect", (reason) => {
    console.log(`${enterUserName}가 퇴장하였습니다.`)
    //client에 접근이 안됨 => Q. client에 접근이 안됨 => disconnect
    // 모든 사람
    io.emit("new message", { username: "관리자", message: `${enterUserName}님이 방에서 나갔습니다.` });    // client.broadcast.emit("new message", { username: "관리자", message: `${enterUserName}님이 방에서 나갔습니다.` })
  })
})
// 여기가 맞는가? -> 재연결 동작안함s
// io.on("reconnect_attempt", (attempt) => {
//   console.log("재연결을 시도했습니다.")
//   console.log(attempt)
// })

server.listen(3000, () => {
  //server가 돌아간다.
  console.log("CORS-enabled web server listening on port 3000")
  console.log("server running at http://localhost:3000")
})
app.get("/message", (_, res) => res.send("Hello from express!"))
ViteExpress.bind(app, server)
