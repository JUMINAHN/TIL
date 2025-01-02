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
io.on("connection", (socket) => {
  //클라이언트가 연결되었을 때
  console.log("사용자가 입장하였습니다. 박수로 환영해주세요!") //이거 지금 안되잖아 => connect 안된거 아님?
  // console.log(client) //이건 공식 문서대로 진행되었는데?
  socket.on("disconnect", (reason) => {
    console.log(reason)
    console.log("사용자가 퇴장하였습니다.")
  })
})
server.listen(3000, () => {
  //server가 돌아간다.
  console.log("CORS-enabled web server listening on port 3000")
  console.log("server running at http://localhost:3000")
})
app.get("/message", (_, res) => res.send("Hello from express!"))
ViteExpress.bind(app, server)
