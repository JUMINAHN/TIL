import { getEmotionImage } from "../util/get-motion-image"
import { emotionData } from "../util/get-matching-image"
import "./Viewer.css"


//특정 data 받아오는 것 => edit 페이지에서 사용 => 필터링
//emotionData 필터링하는 것 => 불러오기
const Viewer = ({diaryDate}) => {
  // console.log('content', content)
  // console.log('createdDate', createdDate) //undefined
  // console.log('emotionId', emotionId) //undefined
  // console.log('id', id) //undefined
  // console.log(diaryDate, '받아옴')
  const emotion = 5
  //호출말고 일단 불러오는 것 사용
  // const findContent = emotionData.find((item) => String(item.emotionId) === String(emotion))
  const findContent = emotionData.find((item) => String(item.emotionId) === String(diaryDate.emotionId))
  // console.log(params.id)
  return (
    <div className="Viewer">
      <section className="img_section">
        <h4>오늘의 감정</h4> 
        <div className={`emotion_img_wrapper emotion_img_wrapper_${diaryDate.emotionId}`}>
          <img src={getEmotionImage(Number(diaryDate.emotionId))} alt="" />
          <div>{findContent.emotionName}</div>
        </div>
      </section>
      <section className="content_section">
        <h4>오늘의 일기</h4>
        <div className="content_wrapper">
          <p>{diaryDate.content}</p>
        </div>
      </section>
    </div>
  )
}

export default Viewer