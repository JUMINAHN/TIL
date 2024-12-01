import { useState } from 'react'

const Bulb = () => { //자식 컴포넌트로 배치
  const [light, setLight] = useState("OFF") //꺼진 것이 초기값 == 초기값
  console.log(light) //자신이 받는 state가 변경되지 않아도 부모의 props가 변경되면 rerendering된다.
  return (
    <div>{light === "ON" ? <h1 style={{
      backgroundColor : "orange"
    }}>ON</h1> : <h1 style={{
      backgroundColor : "grey"
    }}>OFF</h1>}

    <button onClick={()=> {
      setLight(light === "ON" ? "OFF" : "ON")
      //현재값이 ON인지 OF인지? => 자체 toggle
    }}>{light === "ON" ? "끄기" : "켜기"}</button>
   </div>
  )
}

export default Bulb