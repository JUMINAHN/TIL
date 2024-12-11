import { useState } from 'react'
import Viewer from './components/Viewer'
import Controller from './components/Controller'
import './App.css'
import './index.css'

function App() {
  const [count, setCount] = useState(0)

  //원래는 count와 setcount를 모두 전달해줘야하는데 번거로움 발생
  //따라서 이벤트 핸들러 자체를 전달
  const onClickButton = (value) => { //어떤 버튼이 클릭되었는지
    setCount(count + value) //매개변수를 더해줌 => 여기서 setCount는 count에 직접 영향을 주는 것
    //따라서 count + value
    //어떤 value가 전달될지 모르기 때문에
  }

  return (
    <div className='App'>
      <h1>Simple Counter</h1>
      <section>
        <Viewer
        count={count} />
      </section>
      <section>
        <Controller
        onClickButton={onClickButton}/>
        {/* 일반적인 onClick과 다름 컴포넌트 자체라서, 그래서 함수명 자체를 내려줌 */}
      </section>
    </div>
  )
}

export default App
