import { useState } from 'react'

import './App.css'
import NavbarComponent from './components/NavbarComponent'
import FooterComponent from './components/FooterComponent'
import ContentComponent from './components/ContentComponent'

//1. 컴포넌트 매핑 객체 만들기
const componentMapping = { //component 자체를 Mapping할것이기 떄문에 function이 아닌 객체로
  Navbar : NavbarComponent,
  Footer : FooterComponent,
  Content : ContentComponent
}

//2. 동적으로 컴포넌트 렌더링하기
//DynamicComponent : 실제 맞는 것을 보여줄 내용
function DynamicComponent({componentName, ...props}) {// 컴포넌트 이름과, props
  const Component = componentMapping[componentName] //사용자에게 input값으로 받을 내용을 mapping => 키로
  // 컴포넌트 자체를 return 할것이니까 `<>`
  return <Component componentName={componentName} {...props}/> 
}

function App() {
  const [currentComponent, setCurrentComponent] = useState('Navbar') //기본은 navVar로 설정
  //Navbar라고 말하면 네비게이션, Footer라고 말하면 Footer가 나오도록

  return (
    <div>
      {/* 공통적으로 사용할 컴포넌트 자체를 작성 */}
      <DynamicComponent  //DynamicComponent를 작성한 위치를 볼 것
      componentName={currentComponent}
      title={`${currentComponent} 제목`}/>
      <button onClick={() => setCurrentComponent('Navbar')}>네비게이션 바</button>
      <button onClick={() => setCurrentComponent('Content')}>콘텐츠</button>
      <button onClick={() => setCurrentComponent('Footer')}>푸터</button>
    </div>
  )
}

export default App
