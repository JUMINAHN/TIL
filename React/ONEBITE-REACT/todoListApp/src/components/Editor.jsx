import { useState } from 'react'
import './Editor.css'


const Editor = ({onClickAddBtn}) => {
  //바로 onClickAddBtn을 하면 원하는 값을 전달하지 못하는 문제
  const [input, setInput] = useState() //state선언
  //input에 원하는 값들이 담김

  //Q. 매개변수에 인자값이 없어도 상기에 언급한 내용을 넣어도 돌아가는지?
  const onChangeInput = (e) => {
    // console.log('input 값이 들어갔나요?', e)
    // console.log(e.target, '타겟')
    console.log(e.target.value, '타겟 value')
    //근본적인 문제는 setInput에 이상한 값을 넣고있었다..!
    setInput(e.target.value)
    //setInput(input) //일단 input값이 뭐가 들어갈 때 마다 이거 확인
  }

  //그리고 실제 clickEvent 발생을 위한 command 작성
  
  //input값을 넣지 않아도 되는것인지?
  //매개변수 input이 들어가면 => 얘가 우선시 됨

  const onClickBtn = () => { //input값을 받았고
    //이걸 하면 onClickAddBtn이 작동된다.
    //그럼 무엇을 전달?
    //즉 하기 형태로 쓰면 event 자체가 들어와짐

    //클릭은 잘되는지 디버깅
    console.log('클릭됨')
    console.log('onClickAddBtn 전달될 것', input, '얘는 인풋값')
    onClickAddBtn(input)
  }

  return (
    <div className="Editor">
      <input type="text"
      value={input}
      onChange={onChangeInput}

      placeholder="새로운 Todo..."/>
      <button
      // 다시 e.target.value로 접근하려 했으나 => 여기 보면 value의 값이 비어있음..
      onClick={onClickBtn}>추가</button>
    </div>
  )
}

export default Editor 