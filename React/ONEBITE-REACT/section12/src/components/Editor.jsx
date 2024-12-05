import { useState } from 'react'
import Button from './Button'
import './Editor.css'
import EmotionItem from './EmotionItem'
import { useNavigate } from 'react-router-dom'
import { useEffect } from 'react';

const EmotionList = [
  {
    emotionId : 1,
    emotionName : '완전 좋음'
  },
  {
    emotionId : 2,
    emotionName : '좋음'
  },
  {
    emotionId : 3,
    emotionName : '그럭 저럭'
  },
  {
    emotionId : 4,
    emotionName : '나쁨'
  },
  {
    emotionId : 5,
    emotionName : '최악'
  }
]

const getStringDate = (targetDate) => {
  let year = targetDate.getFullYear()
  let month = targetDate.getMonth() + 1
  let date = targetDate.getDate()

  if (month < 10) {
    month = `0${month}`
  }
  if (date < 10) {
    date = `0${date}`
  }

  return `${year}-${month}-${date}`
}

//initData가 초기값으로 설정
const Editor = ({initData, onSubmit}) => {
  const [input, setInput] = useState({ //여러 요소 객체로 담아줘야 함
    // 더미
    createdDate: new Date(), 
    emotionId : 3,
    content : "하하",
  })
  const nav = useNavigate()
  useEffect(()=> {
    if(initData) {
      //initData가 있을떄만
      setInput({
        ...initData,
        createdDate: new Date(Number(initData.createdDate))
        //new Date그 자체로 들ㅇ거ㅏ면 우리가 날짜를 객체로 바꾼 것에 대한 에러가 있을 수 있기 때문에 저렇게 설정
      })
    }
  }, [initData]) //initData => ctrl + s 로 뜨게 되는 이유는 의존성 배열이 명확하게 되어있지 않아서
  
  const onClickSubmit = () => {
  if (input.content.length < 1) {
    window.alert("일기 내용을 작성해주세요")
    return
  }
  
  if (window.confirm(initData ? "일기를 수정하시겠습니까?" : "새로운 일기를 작성하시겠습니까?")) {
    onSubmit(input)
  }
}

  //new에서 한 것 처럼 동일하게 onsubmit

  // 일단 오늘의 날짜 관련 함수로만 받아와보기
  const onChangeInput = (e) => {
    let name = e.target.name
    let value = e.target.value

    if (name === "createdDate") {
      value = new Date(value) //value를 date형식으로
    }

    setInput({
      // 다른 부분 유지
      ...input,
      [name] : value
      // date객체가 문자열로 저장되니까 이부분 조심하기
    })
  }

  // const onClickSubmit = () => {
  //   onSubmit(input) //그냥 inputsatc넘겨준다
  // }

  return (
    <div className='Editor'>
      <section className='date_section'>
        <h4>오늘의 날짜</h4>
        <input value={getStringDate(input.createdDate)} 
        name="createdDate"
        onChange={onChangeInput}
        type="date"/>
      </section>
      <section className='emotion_section'>
        <h4>오늘의 감정</h4>
        <div className='emotion_list_wrapper'>
          {EmotionList.map((item) => <EmotionItem 
          onClick={() => onChangeInput({
            target : {
              name : "emotionId",
              value : item.emotionId
            }
          })}
          key={item.emotionId}
          {...item}
          isSelected={item.emotionId === input.emotionId}/>)} 
        </div>
      </section>
      <section className='content_section'>
        <h4>오늘의 일기</h4>
        <textarea name="content" 
        value={input.content}
        onChange={onChangeInput}
        id="" placeholder='오늘은 어땟나요?'></textarea>
      </section>
      <section className='button_section'>
        <Button
        onClick={() => nav(-1)}
        text={'취소하기'}/> 
        <Button
        text={'작성완료'}
        onClick={onClickSubmit}
        type={"POSITIVE"}/> 
      </section>
    </div>
  )
}

export default Editor