import { useReducer } from "react"
//test를 위해서 간단한 counter 기능

function reducer(state, action) {
  console.log(state, action)
  // if (action.type === "INCREASE") {
  //   return state + action.data
  // } else {
  //   return state - action.data
  // }
  switch (action.type){
    case "INCREASE" :
      return state + action.data
    case "DECREASE" :
      return state - action.data
    default:
      return state
  }
}

const Exam = () => {
  //dispatch는 발송하다, 급송하다
  //즉 상태변화가 있어야한다는 사실을 알리는, 발송하는 함수
  const [state, dispatch] = useReducer(reducer, 0)
  //상태변화 요청 => 실제로 상태를 처리하는 함수가 있어야 함 == 변환기 reducer, state 초기값

  const onClickPlus = () => {
    dispatch({
      type : "INCREASE",
      data : 1
    })
  }

  
  const onClickMinus = () => {
    dispatch({
      type : "DECREASE",
      data : 1
    })
  }

  //dispatch를 호출해서 state를 변화시킴
  return (
    <div>
      <h1>{state}</h1>
      <button
      onClick={onClickPlus}>+</button>
      <button
      onClick={onClickMinus}>-</button>
    </div>

  )
}

export default Exam