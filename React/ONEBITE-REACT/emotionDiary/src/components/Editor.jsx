import { emotionData } from '../util/get-matching-image'
import Button from './Button'
import EmotionItem from './EmotionItem'
import './Editor.css'
import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { changeFormatter } from './../util/get-matching-date';

// const changeFormatter = (date) => { 
// // input으로 입력되는 친구도 똑같은 문자열이기 때문에 날짜로 다시 변환
//   // console.log(date)
//   const year = date.getFullYear()
//   const month = date.getMonth() + 1
//   const day = date.getDate()
//   //근데 단순히 작성하면 2024-12-8 => 우리가 원하는 00-00이 아님
//   if (month < 10 && day < 10) {
//     return `${year}-0${month}-0${day}`
//   } else if (month < 10) {
//     return `${year}-0${month}-${day}`
//   } else if (day < 10) {
//     return `${year}-${month}-0${day}`
//   } else {
//     return `${year}-${month}-${day}`
//   }
// } 

//input값을 기반으로 매칭 => input => 근데 input값? => 들어있는가? : New에서 있었던 것..? => 그냥 data자체에서 매칭시켜야할 것 같은데
// const findData = (params, data) => { //id를 기반으로 일치값 찾기
//   const innerData = data.find((item) => String(item.id) === String(params.id))
//   return innerData
// }

const Editor = ({onSubmit, data}) => {
  // let innerData
  // if (params) {
  //   innerData = findData(params, data) //무작정 실행이 되니까
  //   // console.log(innerData, 'undefined')
  // } 

  const nav = useNavigate()
  const [input, setInput] = useState({ //여러 데이터 한꺼번에 전달
    //date, diary, emotion값 한꺼번에 저장하는 방식 => 기존 데이터 받아왔고
    // id : params ? innerData.id : "", 
    createdDate : new Date(), //new Date(), // 
    emotionId : "", //"", //
    content : "" //임시, "" //
  })

  useEffect(()=> {
    if (data) {
      console.log(data, 'data')
      console.log(data.createdDate, 'date?')
      setInput({
        ...data,
        createdDate : new Date(Number(data.createdDate)) //오류
      })
    }
  }, [data]) //데이터가 변경될 때 마다



  //onClickEvent도 전체 통합
  const onChangeInput = (e) => {
    let name = e.target.name
    let value = e.target.value
    if (name === "createdDate") {//생성날짜가 name값이면
      value = new Date(value) //새로운 밸류 == 생성된 날짜가 문자일 수 있기 때문에 => new Entry
    }
    setInput({
      ...input, 
      //이름에 따라 필터링
      [name] : value //또 여기에 있는 애가 문자로 저장 될 것
    })
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