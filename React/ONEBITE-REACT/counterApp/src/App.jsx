import { useState } from 'react'
import './App.css'
import Controller from './components/Controller'
import Viewer from './components/Viewer'


//1차 UI 출력은 완료
//2차 실제 기능적 동작?
//state값이 interface에 반영되고, click된 값들에 맞게 다시 state변경
//props로 전달할 수 있냐의 유무

function App() {//전체 최상위 부모
  const [count, setCount] = useState(0)
  //count를 세고 있음
  // console.log(count, '현재 카운트의 값 확인')
  //해당값을 Viewer에서 다룰 것이기 떄문에 Viewer에 전달
  //state의 반영과 setCount의 반환여부 같이 관리해야 함..
  //기능적 동작은 Controller에서 해야하고, 값을 주고 받는 것도 기능적 측면

  const onClickCount = (value) => {
    // console.log('click', value)
    //value가 무엇인지 확인해보기 => 일단 onClickCount자체를 props로 자식에게 내려보냄

    //click하면 state에 직접 영향을 줄 것
    setCount(count + value) //얼만큼 카운트할거냐? => 새로운 값 담길 것
    //-1, -10, -100에 대한 값들 
  }

  return (
    //큰 상위 최상위 묶음
    <div className='App'>
      <section>
      <Viewer
        count={count}/>
      {/* component자체에 click을 주는것은 아님 */}
      {/* 행동을 제공해줌 */}
      </section>
      <section>
        <Controller
        onClickCount={onClickCount}/>
      </section>
      {/* 일단 ClickCount 실행 : 어떠한 것도 전달되지 않음 */}
    </div>
  )
}

export default App
