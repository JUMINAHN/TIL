import { emotionData } from '../util/get-matching-image'
import Button from './Button'
import EmotionItem from './EmotionItem'
import './Editor.css'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'



const changeFormatter = (date) => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  //근데 단순히 작성하면 2024-12-8 => 우리가 원하는 00-00이 아님
  if (month < 10 && day < 10) {
    return `${year}-0${month}-0${day}`
  } else if (month < 10) {
    return `${year}-0${month}-${day}`
  } else if (day < 10) {
    return `${year}-${month}-0${day}`
  } else {
    return `${year}-${month}-${day}`
  }
} 

//new로부터 onCreate 데이터 받음 => 이걸 실행하면 => new에 전달해줘야 함
const Editor = ({onCreate}) => {
  const nav = useNavigate()
  const [todayDate, setTodayDate] = useState(changeFormatter(new Date())) 
  const [todayDiary, SetTodayDiary] = useState() 
  const [todayEmotion, SetTodayEmotion] = useState([]) 
  //감정도 보관해야 함

  // Q. 클릭하면 선택이 되는 것 .. 그럼 background는 자체적으로 설정이되는 것인데 => 선택된 데이터를 넘겨주나?

  //날짜 데이터
  const onChangeDate = (e) => {
    setTodayDate(e.target.value)
  }

  //일기 데이터
  const onChangeDiary = (e) => {
    SetTodayDiary(e.target.value)
  }

  //감정 데이터 == 이게 애초에 onChange를 담을 수 없음 컴포넌트라서 => 
    //Q. 이 감정을 그러면 EmoitonItem에서 관리해야하는건지? 지금 여기서 관리하는 상태 전달 못하는지?
  const onClickEmotion = (emotionId) => {
    const findEmotion = emotionData.find((item) => String(item.emotionId) === String(emotionId)) //일치되는 값 찾기
    SetTodayEmotion(findEmotion) 
  }
 

  return (
    <div className='Editor'>
      <section className='Editor_Date'>
        <h1 className='Editor_Date_Title'>오늘의 날짜</h1>
        <input className='Editor_Date_Input' type="date" 
        value={todayDate} onChange={onChangeDate} name="" id="" />
      </section>
      <section className='Editor_Emotion'>
        <h1 className='Editor_Emotion_Title'>오늘의 감정</h1>
        <div className="Editor_Emotion_Item">
          {emotionData.map((item) => 
          <EmotionItem
          value={todayEmotion}
          onClick={() => onClickEmotion(item.emotionId)}
          // 제대로 담기는지 먼저 테스트만?
          key={item.emotionId}
          {...item}/>)}
        </div>
      </section>
      <section className='Editor_Diary'>
        <h1 className='Editor_Diary_Title'>오늘의 일기</h1>
        <textarea className='Editor_Diary_Input' 
        value={todayDiary} onChange={onChangeDiary}
        name="" id="" placeholder='오늘은 어땠나요?'></textarea>
      </section>
      <section className='Editor_Button'>
        <Button text={"취소하기"}
        onClick={() => {nav('/')}}/>
        <Button text={"작성 완료"}
        // onCreate 호출
        type={"POSITIVE"}/>
      </section>
    </div>
  )
}
export default Editor