import { useEffect, useRef, useState } from 'react'
import Viewer from './components/Viewer'
import Controller from './components/Controller'
import Even from './components/Even'
import './App.css'
import './index.css'


function App() {
  const [count, setCount] = useState(0)
  const [input, setInput] = useState("") //새로운 배열 추가 => ref

  const isMount = useRef(false)//초기값이 설정되지 않았다. => false이면 mounted 되지 않았다.


  //useEffect => Q. Vue의 onMounted?
  //라이프 사이클
  //1. 마운트 : 탄생
  useEffect(()=>{
    console.log('mount') //최초로 한번 
  }, [])//depth 빈배열
  //2. 업데이트 : 변화, 리렌더링
  //depth 생략 => 업데이트 일어날때마다 실행, 뭔갈 할떄마다 실행됨
  useEffect(()=> {
    if(!isMount.current) { //flag로 사용
      isMount.current = true //true로 바뀜
      return //강제 return
    }
    console.log('update') //진짜 업데이트 되는 순간만 측정하고 싶다면?
  })

  //3. 언마운트 : 죽음

  //useEffect 원하는 동작 만들어줄 수 있음
  //첫번쨰 인자 : 콜백, 두번째 인자 : 배열
  //2번쨰 인자가 바뀌게 되면, 첫번쨰의 콜백함수를 실행시켜주는 것이 useEffect
  //상기 input의 값을 넣고, 바뀌더라도 count에만 영향이 가기 떄문에 출력이 되지 않는 것으로 볼 수 있음
  // useEffect(()=> {
  //   // console.log(`count : ${count} / ${input}`)
  // }, [count, input]) //배열에 count를 넣으면 count가 바뀔떄마다 callback 실행 
  //count가 바뀔때마다 callback이 계속 실행됨
  //useEffect 훅은 두번쨰 인자에 의존 => dependency array
  //deps == 의존성 배열, 여러개 넣어도 무관함

  

  const onClickButton = (value) => { 
    setCount(count + value)  //비동기로 동작한다 => setCount : 실제호출만된거지 완료된게 아님
    //즉각적 확인은 useEffect로 해야한다.
    console.log(count) //변경되기 이전의 값을 계속 출력한다.
  }

  return (
    <div className='App'>
      <h1>Simple Counter</h1>
      <section>
        <input value={input}
        onChange={(e)=> {
          setInput(e.target.value)
        }}/>
      </section>

      <section>
        <Viewer
        count={count} />
        {count % 2 === 0 ? <Even/> : null}
      </section>
      <section>
        <Controller
        onClickButton={onClickButton}/>
      </section>
    </div>
  )
}

export default App
