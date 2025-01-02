import { useState } from "react"
import reactLogo from "./assets/react.svg"
import viteLogo from "/vite.svg"
import "./App.css"
import { io } from "socket.io-client"

function App() {
  const [count, setCount] = useState(0)
  const [socket, setSocket] = useState(null) //socket의 연결 유무 => 밑 connect
  //사용자가 연결을 성공했을 떄
  const successConnect = () => {
    // 왜 5173? 3000포트..?
    const _socket = io("http://localhost:3000", {
      //서버의 주소
      //여기서는 사용자 서버 자체
      autoConnect: false,
    }) //socket 자체를 사용자에게 불러오는 것이지 => 그니까 async로 매번 불러왔던 것 처럼
    //내장으로 지금 진행가능하게 하는 것
    _socket.connect()
    // console.log(_socket, "_socket")
    // console.log(_socket.connect(), "_socket")
    console.log("사용자의 연결이 성공했습니다.") //연결의 성공 유무
    setSocket(_socket)
    //reconnect
    // _socket.on("disconnect", () => {
    //   socket.connect()
    //   setSocket(_socket) //socket의 연결 상태
    // })
  }

  const failConnect = () => {
    //연결 유무에 따라 disconnect
    socket.disconnect() //단순 disconnect
    console.log("사용자의 연결이 해제되었습니다.")
    //socket의 값이 있따면? => disconnect이긴 하겠지만
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
        <button onClick={() => successConnect()}>입장</button>
        <button onClick={() => failConnect()}>퇴장</button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">Click on the Vite and React logos to learn more</p>
    </>
  )
}

export default App
