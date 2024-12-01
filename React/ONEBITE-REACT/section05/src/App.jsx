//1. state변경
//2. props 변경되면 리랜더링
//3. 부모 컴포넌트 변경되면 자식도 리랜더링 => 따라서 관련없는 것 분류

import { useState } from 'react'
import './App.css'
import Bulb from './components/Bulb'
import Counter from './components/Counter'

function App() { 
  //const state = useState()
  //undefined, function => 2개의 배열을 볼 수 있음
  //2개의 요소를 담은 배열
  //초기값 => useState에 0을 넣으면 0이 출력 == state현재 값
  //함수 == 상태를 변화시키는 함수 == 상태변화함수
  //따라서 일반적으로 배열화 
  //가변적인 값을 state로 관리한다.
  //값과 함수 => 구조 분해 할당

  //교재에서 본 것처럼 다시

  return ( 
    <>
      {/* <h1>{light}</h1>/ */}
      {/* light라는 속성을 상기에 추가했기 때문에 light라는 곳에 light 속성값을 넣어주는 것 Q? */}
      {/* 자식 컴포넌트는 부모에게 받는 props가 바뀌게 되면 계속해서 리랜더링 된다.*Q */}
      <Bulb />
      <Counter />


    </>
  )
}

export default App
