import { useState } from 'react'
import Button from './Button'
import './Editor.css'
import EmotionItem from './EmotionItem'
import { useNavigate } from 'react-router-dom'

//나의 감정 => 계속 랜더링 할필요가 없으니 외부에 선언
//emotionId 이름, emotionText
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

//지금은 초기값
const getStringDate = (targetDate) => {
  //날짜 yyyy-mm-dd 형식으로 바꿔줘야 함 => 데이터 소스 받아오기
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

const Editor = ({onSubmit}) => {
  //이모션별로 어떠한 감정이 선택되었는지 담아줘야 함
  //사용자가 입력한 값들 다 담아줘야함 => 감정, 날짜, 일기 등..
  //onCreate에 전달해주면 됨 => 근데 oncreate XX => edit페이지에서 업데이트를 시켜야하니까 이부분 조심해야 함
  //작성완료 -> page -> props로 전달받음 
  const [input, setInput] = useState({ //여러 요소 객체로 담아줘야 함
    // 더미
    createdDate : new Date(),
    emotionId : 3,
    content : "",
  })
  const nav = useNavigate()
  

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

  const onClickSubmit = () => {
    onSubmit(input) //그냥 inputsatc넘겨준다
  }
  // const emotionId = 5 //이거와 일치하면 특별한 메서드 제공

  return (
    <div className='Editor'>
      <section className='date_section'>
        <h4>오늘의 날짜</h4>
        {/* input은 createDate로 만든 Date()객체를 이해못함 -> string Type으로 바꿔줘야 함 */}
        <input value={getStringDate(input.createdDate)} 
        name="createdDate"
        onChange={onChangeInput}
        type="date"/>
      </section>
      <section className='emotion_section'>
        <h4>오늘의 감정</h4>
        <div className='emotion_list_wrapper'>
          {EmotionList.map((item) => <EmotionItem 
          //component 클릭이지만 onClick으로 이벤트 강제 발생
          // 직접 만들어서 전달해줘야함
          onClick={() => onChangeInput({
            //컴포넌트라서 자동으로 전달되지 않음
            // 여기 주의
            target : {
              name : "emotionId",
              value : item.emotionId
            }
          })}
          key={item.emotionId}
          // emotionId={item.emotionId}
          // emotionName={item.emotionName}
          {...item}
          isSelected={item.emotionId === input.emotionId}/>)} 
          {/* item 모두 활용? Q.? */}
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