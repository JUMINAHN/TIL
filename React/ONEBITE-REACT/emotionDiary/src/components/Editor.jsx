import { emotionData } from '../util/get-matching-image'
import Button from './Button'
import EmotionItem from './EmotionItem'
import './Editor.css'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'



const changeFormatter = (date) => { 
// input으로 입력되는 친구도 똑같은 문자열이기 때문에 날짜로 다시 변환
  console.log(date)
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
const Editor = ({onSubmit}) => {
  // const [todayDate, setTodayDate] = useState(changeFormatter(new Date())) 
  // const [todayDiary, SetTodayDiary] = useState() 
  // const [todayEmotion, SetTodayEmotion] = useState([]) 
  //감정도 보관해야 함
  //일기 데이터
  // const onChangeDiary = (e) => {
  //   setInput({
  //     ...input,
  //     content : e.target.value
  //   })
  //   // SetTodayDiary(e.target.value) //제거 예정
  // }

  //감정 데이터 == 이게 애초에 onChange를 담을 수 없음 컴포넌트라서 => 
    //Q. 이 감정을 그러면 EmoitonItem에서 관리해야하는건지? 지금 여기서 관리하는 상태 전달 못하는지?
  // const findEmotion = emotionData.find((item) => String(item.emotionId) === String(emotionId)) //일치되는 값 찾기
  
  // const onClickEmotion = (emotionId) => {
  //   // name을 통해서 각각 다른 메서드의 값을 그대로 유지하는  오..
  //   setInput({
  //     ...input, ///나머지는 그대로
  //     emotionId : emotionId
  //   })
  //   // SetTodayEmotion(emotionId) //제거 예정
  // }
 
  //onCreate를 넘겨받게되는데

  const nav = useNavigate()
  const [input, setInput] = useState({ //여러 데이터 한꺼번에 전달
    //date, diary, emotion값 한꺼번에 저장하는 방식
    createdDate : new Date(), //기본값 ==> 여기서 애초에 changeFormatter를 걸었기 떄문에 input에 안걸어도 되었던 것
    emotionId : "",
    content : "" //임시
  })

  //onClickEvent도 전체 통합
  const onChangeInput = (e) => {
    let name = e.target.name
    let value = e.target.value
    if (name === "createdDate") {//생성날짜가 name값이면
      value = new Date(value) //새로운 밸류 == 생성된 날짜가 문자일 수 있기 때문에 => new Entry
    }
    setInput({
      ...input, 
      //즉 방법은 다르지만 결국 똑같은 상태
      //이름에 따라 필터링
      [name] : value //또 여기에 있는 애가 문자로 저장 될 것
    })
    // setTodayDate(e.target.value) //제거 예정
  }

  //일단 create기준
  const onClickBtn = () => {
    onSubmit(input) //그냥 입력값 자체를 전달한다.
  }

  // 사실 지금 하나로 통합하는 것 뿐 아까랑 다를건 없음
  return (
    <div className='Editor'>
      <section className='date_section'>
        <h4 className='Editor_Date_Title'>오늘의 날짜</h4>
        <input className='Editor_Date_Input' type="date" 
        // nametag도 연결시켜서 => formatter 가능하게.. 
        value={changeFormatter(input.createdDate)} onChange={onChangeInput} name="createdDate" id="" />
      </section>

      <section className='emotion_section'>
        <h4>오늘의 감정</h4>
        <div className="emotion_list_wrapper">
          {emotionData.map((item) => 
          <EmotionItem
          value={input.emotionId}
          onClick={() => onChangeInput({//changeInput이 가능한 것 처럼 만들기
            // 기존 onChange가 전달하는 내용을 target으로 바꾼 것 뿐
            target : {
              name : "emotionId",
              value : item.emotionId
            },
          })}
          // 제대로 담기는지 먼저 테스트만?
          // 그냥 선택이 올바르게 되어있는지에 대한 판단을 위해서 단순 데이터만 설정
          isSelected={item.emotionId === input.emotionId}
          key={item.emotionId}
          {...item}/>)}
        </div>
      </section>

      <section className='content_section'>
        <h4 className='Editor_Diary_Title'>오늘의 일기</h4>
        <textarea className='Editor_Diary_Input' 
        value={input.content} onChange={onChangeInput}
        name="content" id="" placeholder='오늘은 어땠나요?'></textarea>
      </section>

      <section className='button_section'>
        <Button text={"취소하기"}
        onClick={() => {nav('/')}}/>
        <Button text={"작성 완료"}
        // onCreate 호출
        onClick={onClickBtn}
        type={"POSITIVE"}/>
      </section>
    </div>
  )
}
export default Editor