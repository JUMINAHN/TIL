import './App.css'
import Header from './components/Header' //react는 파일 확장자 생략 가능
import Main from './components/Main' 
import Footer from './components/Footer' 
import Button from './components/Button'


//여기서는 @/components가 안되나?


function App() { //함수의 이름을 따서 컴포넌트라고 부른다.

  //여기서 props로 전달하는 것이 Vue랑 비슷한지? 
  //그떄는 :sth = {} 이런식으로 전달하고
  //define으로 받았었는데 ?
  //헷갈리는게 지금 text={"sth"}그냥 단순 이런구조로 접근해도 되는건가?

  const buttonProps = {
    text : '메일',
    color : 'red',
    a : 1,
    b : 2,
    c : 3
  }


  return ( 
    <>
    {/* 다른 text를 전달 -> 일단 이거 제공해준 것이고 활용 아직 X*/}
    <Button {...buttonProps}/> 
    <Button text={"카페"}/>
    <Button text={"블로그"}>
      <div>자식요소</div>
      {/* 자동으로 자식요소? : 자동으로 children */}
    </Button>
      {/* <Header />  */}
      {/* 반환값을 불러와서 함께 랜더링 된다. == 즉 자식 컴포넌트 */}
      {/* <h1>안녕 리액트</h1>  */}
      {/* <Main/> */}
      {/* <Footer /> */}
      {/* html 반환 가능 => 앱은 랜더링 됨 ==이건 부모컴포넌트 (ROOT) */}
      {/* Root가 무엇인지에 따라 달라짐 : 관례상 APP이 루트 컴포넌트 */}
    </>
  )
}

export default App
