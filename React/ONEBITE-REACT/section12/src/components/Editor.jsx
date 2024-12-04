import Button from './Button'
import './Editor.css'
import EmotionItem from './EmotionItem'

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

const Editor = () => {
  //이모션별로 어떠한 감정이 선택되었는지 담아줘야 함
  const emotionId = 5 //이거와 일치하면 특별한 메서드 제공

  return (
    <div className='Editor'>
      <section className='date_section'>
        <h4>오늘의 날짜</h4>
        <input type="date"/>
      </section>
      <section className='emotion_section'>
        <h4>오늘의 감정</h4>
        <div className='emotion_list_wrapper'>
          {EmotionList.map((item) => <EmotionItem 
          key={item.emotionId}
          // emotionId={item.emotionId}
          // emotionName={item.emotionName}
          {...item}
          isSelected={item.emotionId === emotionId}/>)} 
          {/* item 모두 활용? Q.? */}
        </div>
      </section>
      <section className='content_section'>
        <h4>오늘의 일기</h4>
        <textarea name="" id="" placeholder='오늘은 어땟나요?'></textarea>
      </section>
      <section className='button_section'>
        <Button
        text={'취소하기'}/> 
        <Button
        text={'작성완료'}
        type={"POSITIVE"}/> 
      </section>
    </div>
  )
}

export default Editor