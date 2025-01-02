import { useState } from "react"
import reactLogo from "./assets/react.svg"
import viteLogo from "/vite.svg"
import "./App.css"
import { io } from "socket.io-client" //io를 통해서 연결을 시도한다.

function App() {
  const [count, setCount] = useState(0)
  const [socket, setSocket] = useState(null)

  const connectChatServer = () => {
    // 로컬 host 3000으로 돌아가고 있음 => server.js에서
    console.log("connect Chat Server")
    // 또 공식문서에는 쿼리로 추가로 socket을 더 만드는데 여기서는 그냥?
    const _socket = io("http://localhost:3000", {
      //Q.왜 여기서 _
      autoConnect: false,
      withCredentials: true,
    })
    _socket.connect()
    setSocket(_socket) // setSocket
  }

  const disconnectChatServer = () => {
    // const _socket = io.on("connection", (socket) => {
    // setTimeout(() => socket.disconnect(true), 5000);
    // })
    console.log("disconect Chat server")
    socket?.disconnect() //socket 값이 있다면 연결 해제
    // console.log("disconnect Chat Server")
    // setSocket(_socket)
  }

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>count is {count}</button>
        <button onClick={() => connectChatServer()}>접속</button>
        <button onClick={() => disconnectChatServer()}>접속해제</button>

        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">Click on the Vite and React logos to learn more</p>
    </>
  )
}

export default App
