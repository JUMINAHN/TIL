import { useState } from 'react'

import './App.css'
import BooksComponent from './components/BooksComponent'
import ClothingComponent from './components/ClothingComponet'
import ElectronicsComponent from './components/ElectorincsComponent'


//공통 props와 특정 props
//일단 각각 component를 묶어야한다
const componentMapping = {
  Books : BooksComponent,
  Clothing : ClothingComponent,
  Electronic : ElectronicsComponent
}

//Proudct를 Mapping할 상위 컴포넌트
const DynamicComponent = ({componentName, ...props}) => {// ProudctName을 기반으로 props 받기
  const Component = componentMapping[componentName] //Component가 어떠한 컴포넌트인지 잡아오고

  //Q1. props 값 활용 => 내용이 많으니까 일단 ...props로 묶고
  return <Component {...props}
  />
} 

function App() {
  //동적으로 바뀔 컴포넌트 앱 => 앱 컴포넌트는 존재하니, 들어갈 매개변수 값들이 바뀔 것
  const [title, setTitle] = useState('Books') //책을 기본값으로 설정 
  //근데 title에 따라서 object 내부 값들이 다른데 객체로 저장해서 접근해야하는가?

  //Q2.여기서 또 추가적으로 props를 설정한다?.
  const categoryProps = { //속성값을 내부에서
    Electronic: {featuredBrand : 'Samsung', itemCount : 10},
    Clothing: {salePercentage : 20, itemCount : 50},
    Books: {bestSeller : 'React 마스터하기', itemCount : 20}
  }

  return (
    <div>
      <h1>온라인 쇼핑몰</h1>
      <button onClick={() => setTitle('Books')}>책</button>
      <button onClick={() => setTitle('Clothing')}>옷</button>
      <button onClick={() => setTitle('Electronic')}>전자기기</button>
      {/* 일단 dyanmucComponent 자체가 앱이고, 그걸 클릭으로 바꿀 것 */}
      <DynamicComponent
      // 지금 들어가 있는 title로 설정 
      {...categoryProps[title]}
      itemCount={100}
      componentName={title}
      title={`${title} 카테고리`}
      />
    </div>
  )
}

export default App
