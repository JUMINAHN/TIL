import { useState } from 'react'

const Counter = () => {
  const [count, setState] = useState(0) //구조 분해 할당이 일반적
  return (
    <div>
    <h1>{count}</h1>
    {/* 일반 click event처럼 사용 */}
    {/* 상태를 변화시키는 함수 */}
    {/* 상태가 바뀌면 `리랜더링` 해주는 것 == 즉 다시 랜더링한다 : state를 */}
    <button onClick={() => {
      setState(count + 1) //plus만 클릭했는데도 계속 리랜더링된다 => bulb의 값이 
    }}>+</button>
  </div>
  )
}

export default Counter 