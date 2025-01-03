import { useCallback, useEffect, useState } from "react"
import reactLogo from "./assets/react.svg"
import viteLogo from "/vite.svg"
import "./App.css"
import { io } from "https://cdn.socket.io/4.8.1/socket.io.esm.min.js"

function App() {
  const [username, setUserName] = useState("")
  const [inputMsg, setInputMsg] = useState("")
  const [userMsg, setUserMsg] = useState([])
  const [socket, setSocket] = useState() //그 뒤 연결 => socket 자체 통신
  //연결 유무는 별도 => socket에 대한 정보를 주고받는 것
  const [isConnect, setIsConnect] = useState(false)

  // 클릭 누르면 socket 연결
  const connectWithServer = useCallback(() => {
    if (!username) {
      alert("유저 이름을 입력하지 않으면, 접속이 어려워요")
      return
    }
    const _socket = io("http://localhost:3000", {
      autoConnect: false,
      query: {
        username: username, //username
      },
    })
    _socket.connect() //socket이라는 io를 connect 서버와 연결해야하는 것 => axios fetch같은 것?
    // _socket.on("enter message", (msg) => {
    //   console.log("enter", msg) //왜 출력이 안될까?
    // })
    // 근데 그러면 이때 알려주면 되지 않나?
    // console.log("socket", _socket) //보면 여기 고유 id값
    //관리자의 message를 보고 싶음 => io.emit관련

    setSocket(_socket) //socket을 담는다
    setIsConnect(true) // 연결 true
  }, [username]) //연결 유무 => 딱 처음 링크받아올 때

  const disconnectWithServer = useCallback(() => {
    if (socket) {
      socket.disconnect() //socket이라는 io를 connect 서버와 연결해야하는 것 => axios fetch같은 것?
      setIsConnect(false) //socket을 담는다
    }
  }, [socket]) //연결 유무 => 딱 처음 링크받아올 때

  // 이 메세지를 서버에 보낼 것
  const onClickChatMsg = () => {
    if (inputMsg && inputMsg !== "" && inputMsg.trim()) {
      // console.log("채팅 메세지 :", inputMsg)
      socket.emit("chat message", inputMsg) //socekt에 inputMsg 보낼거야
      //이건 message로 전송 완료..
      setInputMsg("")
    } else {
      alert("메세지 내용을 정확하게 입력해주세요") //자체 modal창
    }
  }

  //그렇다면 client에서 보내니까 socket에서 받아야 함
  useEffect(() => {
    if (socket) {
      socket.on("enter message", (msg) => {
        console.log(msg) //왜 출력이 안될까?
        // 이게 채팅에도 출력되어야함
        setUserMsg((prev) => [...prev, msg]) //여기 누락됨
      })

      socket.on("out message", (msg) => {
        console.log(msg)
        setUserMsg((prev) => [...prev, msg])
      })
      //client에서 보내고 io자체에서도 보냄
      //socket.on이 되어있다면 => login user을 받아올 수 있을 것 같음
    }

    return () => {
      // socket off
    }
  }, [socket]) //socket이 변경될 때 마다

  //클린업 함수 나중에 만들기
  //emit으로 받은 것 => socket.on으로
  useEffect(() => {
    // socket이 있을 떄만 읽을 수 있음

    if (socket) {
      const chatMessageHandler = (msg) => {
        // socket.on("chat message", (msg) => {
        //기존에 배열 이슈
        const data = `${msg.username} : ${msg.message}`
        setUserMsg((prev) => [...prev, data])
      }
      socket.on("chat message", chatMessageHandler) //값을 담고 실행

      return () => {
        socket.off("chat message", chatMessageHandler)
      }
    }
  }, [socket])

  //msg받아서 => socket에서 발생하는 chat message

  useEffect(() => {
    window.scrollTo(0, document.body.scrollHeight)
  }, [userMsg]) //메세지가 추가할떄마다

  const onKeyDownMsg = (e) => {
    if (e.key === "Enter") {
      e.preventDefault()
      onClickChatMsg()
    }
  }

  return (
    <div className="App">
      <div className="logo_zone">
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <div className="join_zone">
        <h1>{username ? `"${username}"님 환영합니다!` : "유저 이름을 입력해주세요"}</h1>
        <div className="join_zone_wrap">
          <input type="text" name="" id="" placeholder="유저 이름을 입력해주세요" value={username} onChange={(e) => setUserName(e.target.value)} />
          {!isConnect ? <button onClick={connectWithServer}>입장</button> : <button onClick={disconnectWithServer}>퇴장</button>}
        </div>
      </div>
      {/* connect안하면 못보게 */}
      {isConnect ? (
        <div className="chat_zone">
          <div className="chat_zone_list">
            {/* item */}
            <ul>
              {/* 여기 li가 싸이게 되는 것 */}
              {/* window.scrollTo(0, document.body.scrollHeight) */}
              {userMsg.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>
          </div>
          {/* 제출 submit event 방지 */}
          <form className="chat_zone_wrap" action="" onSubmit={(e) => e.preventDefault()}>
            <input type="text" name="" id="" placeholder="메세지를 입력해주세요." value={inputMsg} onChange={(e) => setInputMsg(e.target.value)} onKeyDown={onKeyDownMsg} />
            <button onClick={onClickChatMsg}>전송</button>
          </form>
        </div>
      ) : (
        <div className="join_message">접속하셔야 대화를 확인할 수 있습니다.</div>
      )}
    </div>
  )
}

export default App
