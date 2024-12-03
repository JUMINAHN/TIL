import { useRef, useState } from 'react';
import './Editor.css';


const Editor = ({onCreate}) => {
  const [content, setContent] = useState("")
  const contentRef = useRef()

  const onChangeContent = (e) => { //이거 왜 하나씩 이렇게 불러야하는지?
    setContent(e.target.value)
  }

  const onKeydown = (e) => {
    if(e.keyCode === 13) {
      onSubmit()
    }
  }

  const onSubmit = () => {
    if (content === "") {
      contentRef.current.focus() //focus가 잡힌다.
      return //값이 없으면 아무것도 실행되지 않음
    }

    onCreate(content)//input 태그 값 전달해주면 된다.
    setContent("")//초기화
    //input에 있는거 전달 => content state에 있는 값 전달
    //여기서는 preventDefault를 안하는?
  }

  return (
    <div className="Editor">
      <input type="text" 
      ref={contentRef}
      value={content}
      onKeyDown={onKeydown}
      onChange={onChangeContent}
      placeholder="새로운 Todo..."/>
      {/* 입력된 내용이 보관될 곳을 만들어 줘야 함 */}
      <button onClick={onSubmit}>추가</button>
    </div>
  ) 
}

export default Editor