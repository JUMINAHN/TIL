import { emotionData } from '../util/get-matching-image'
import Button from './Button'
import EmotionItem from './EmotionItem'
import './Editor.css'

// emotion Item에 대한 것을 map으로 출력할 것 => 여기서?
// 이것을 어디서 선택할지에 대해 생각해봐야 할 포인트 
// EmotionItem이 5개 돌아야 한다 == map 그럼 각각 emotionId와 emotion들이 어떻게 매칭되는가?

// 코드가 더럽혀진다 => 그리고 실제로 diary 페이지에서도 사용되는 것을 볼 수 있음
// 따로 매칭 => getEmoition(1)부터 5까지 다들어갈 수 있음 거기에 따른 이미지
// 일단 여기에 작성해보자
// const emotionData = [
//   {
//     emotionId : 1,
//     emotionName : '완전 좋음'
//   },
//   {
//     emotionId : 2,
//     emotionName : '좋음'
//   },
//   {
//     emotionId : 3,
//     emotionName : '그럭저럭'
//   },
//   {
//     emotionId : 4,
//     emotionName : '나쁨'
//   },
//   {
//     emotionId : 5,
//     emotionName : '최악'
//   }
// ]


const Editor = () => {
  return (
    <div className='Editor'>
      <section className='Editor_Date'>
        <h1 className='Editor_Date_Title'>오늘의 날짜</h1>
        {/* 여기 날짜 e.target.value로 선택할 수 있도록 할 것 */}
        <input className='Editor_Date_Input' type="date" name="" id="" />
      </section>
      <section className='Editor_Emotion'>
        <h1 className='Editor_Emotion_Title'>오늘의 감정</h1>
        <div className="Editor_Emotion_Item">
          {emotionData.map((item) => 
          <EmotionItem
          key={item.emotionId}
          {...item}/>)}
        </div>
      </section>
      <section className='Editor_Diary'>
        <h1 className='Editor_Diary_Title'>오늘의 일기</h1>
        <textarea className='Editor_Diary_Input' name="" id="" placeholder='오늘은 어땠나요?'></textarea>
      </section>
      <section className='Editor_Button'>
        <Button text={"취소하기"}/>
        <Button text={"작성 완료"}
        type={"POSITIVE"}/>
      </section>
    </div>
  )
}

export default Editor