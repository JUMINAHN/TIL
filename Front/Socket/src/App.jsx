import { useCallback, useEffect, useState } from "react"
import reactLogo from "./assets/react.svg"
import viteLogo from "/vite.svg"
import "./App.css"
import { io } from "socket.io-client"
//이제 사용자의 username을 받아와야 함
//사용자의 name을 식별할 수 있어야 함 => 이건 자체 local에서만 사용될게 아니기 떄문에 서버에서

function App() {
  const [nickName, setNickName] = useState("")
  const [socket, setSocket] = useState(null) //연결 링크 및 사용자 정보
  const [isConnect, setIsConnect] = useState(false) // 연결 유무
  const [inputMsg, setInputMsg] = useState("")
  const [message, setMessage] = useState([])

  // 받는메세지
  const receiveMsg = useCallback((msg) => {
    console.log(msg)
    setMessage((prev) => [...prev, msg])
  }, []) //메세지가 올때마다

  useEffect(() => {
    if (socket) {
      socket.on("new message", receiveMsg)
      return () => {
        socket.off("new message", receiveMsg)
      }
    }
  }, [socket, receiveMsg]) //socketEvent Listen

  useEffect(() => {
    window.scrollTo({
      top: document.body.scrollHeight,
      left: 0,
      behavior: "smooth",
    })
  }, [message]) //message가 변경되면 scroll 변경

  const connectSocket = useCallback(() => {
    if (socket) return // 연결된 경우 재연결 방지
    const _socket = io("http://localhost:3000", {
      reconnectionDelayMax: 1, //reconnectDelayMax시간
      autoConnect: false,
      query: {
        nickName: nickName,
      },
    })
    _socket.connect()
    console.log("사용자의 연결이 성공했습니다.")
    setSocket(_socket) //socket정보
    setIsConnect(true)
  }, [nickName, socket]) //nickname이나 socket 변경시

  const disconnectSocket = useCallback(() => {
    socket.disconnect()
    setIsConnect(false)
    console.log("사용자의 연결이 해제되었습니다.")
  }, [socket]) //nickname과 무관

  const sendMsg = () => {
    console.log(`유저의 메세지 입니다 : ${inputMsg}`)
    if (socket && inputMsg.trim() !== "") {
      socket.emit("new message", { username: nickName, message: inputMsg })
      setInputMsg("") //다시 inputMsg초기화
    }
  }

  const messageList = message.map((msg, index) => (
    <li key={index}>
      {msg.username} : {msg.message}
    </li>
  ))

  const onKeyDown = (e) => {
    if (e.code === "Enter") {
      sendMsg()
    }
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

      <div className="card">
        {/* 로그인 관련 데이터 입력 */}
        <div className="card">
          <h4>당신의 닉네임 : {nickName}</h4>

          <input type="text" name="" id="" placeholder="닉네임을 입력해주세요" value={nickName} onChange={(e) => setNickName(e.target.value)} />
          <button disabled={isConnect} onClick={() => connectSocket()}>
            입장
          </button>
          <button disabled={!isConnect} onClick={() => disconnectSocket()}>
            퇴장
          </button>
        </div>
        <h5>{isConnect ? `${nickName}님 환영합니다!` : "방에 입장해주세요!"}</h5>
        <div className="card">
          <input type="text" placeholder="message를 입력해주세요" value={inputMsg} onChange={(e) => setInputMsg(e.target.value)} onKeyDown={onKeyDown} />
          <button onClick={sendMsg}>전송</button>
        </div>
      </div>

      <div>
        <ul>{messageList}</ul>
      </div>
    </>
  )
}

export default App
