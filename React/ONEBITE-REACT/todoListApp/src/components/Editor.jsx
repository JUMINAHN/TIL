import { useRef, useState } from 'react'
import './Editor.css'


const Editor = ({onClickAddBtn}) => {
  const [input, setInput] = useState('') //초기값 
  const inputRef = useRef()//빈값

  const onChangeInput = (e) => {
    console.log(e.target.value, '타겟 value')
    //지금 input만 했는데도 error가 뜨는 문제 
    setInput(e.target.value)
  }

  const onClickBtn = () => { 
    if (input === '') {
      alert('값을 입력해주세요')
      inputRef.current.focus()
      return
    }
    onClickAddBtn(input)
    console.log('input 값 출력 형태 : ', input)
    //하자말자 비워주기
    setInput('') // state 자체가 초기화되는 것
  }

  //키로 설정
  const onKeyDownEnter = (e) => {
    //13번? => keycode
    if (e.keyCode === 13) {
      //똑같이 전송
      onClickBtn() //btn 실행
    }
  }


  return (
    <div className="Editor">
      <input type="text"
      ref={inputRef}
      value={input}
      onKeyDown={onKeyDownEnter}
      onChange={onChangeInput}
      placeholder="새로운 Todo..."/>
      <button
      onClick={onClickBtn}
      >추가</button>
    </div>
  )
}

export default Editor 