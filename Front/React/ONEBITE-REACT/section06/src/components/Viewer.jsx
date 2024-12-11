import { useState } from "react"

const Viewer = ({count}) => {
  // const [count, setCount] = useState(0)
  //setcount를 controller에게 전달해야하는데 부모-자식관계가 아닌데 전달할 수 있는가?
  //형제 관계이기 떄문에 props로 전달하기 어렵다

  return (
    <>
    <div>현재 카운트 : </div>
    <h1>{count}</h1>
    </>
  )
}

export default Viewer