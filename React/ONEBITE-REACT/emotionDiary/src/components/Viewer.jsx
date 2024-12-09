import { useParams } from "react-router-dom"
import { getEmotionImage } from "../util/get-motion-image"
import { emotionData } from "../util/get-matching-image"
import "./Viewer.css"
import useDiary from "../hooks/useDiary"
import { useContext } from "react"
import { DiaryStateContext } from './../App';

//특정 data 받아오는 것 => edit 페이지에서 사용 => 필터링
//emotionData 필터링하는 것 => 불러오기
const Viewer = ({diaryDate}) => {
  // console.log('content', content)
  // console.log('createdDate', createdDate) //undefined
  // console.log('emotionId', emotionId) //undefined
  // console.log('id', id) //undefined
  console.log(diaryDate, '받아옴')
  const emotion = 5
  //호출말고 일단 불러오는 것 사용
  // const findContent = emotionData.find((item) => String(item.emotionId) === String(emotion))
  const findContent = emotionData.find((item) => String(item.emotionId) === String(diaryDate.emotionId))
  // console.log(params.id)
  return (
    <div className="Viewer">
      <section className="emotion_section">
        {/* 이것도 보고 div태그 */}
        <h4>오늘의 감정</h4> 
        {/* 변경 예정 => 특정 emotionImage로, backgroundColor도 */}
        <div className={`emotion_section_img emotion_section_img_${diaryDate.emotionId}`}>
          {/* div로 형식 통일 */}
          <img src={getEmotionImage(Number(diaryDate.emotionId))} alt="" />
          <h4>{findContent.emotionName}</h4>
          {/* div로 */}
        </div>
      </section>
      <section className="content_section">
        <h4>오늘의 일기</h4>
        <div className="content_section_info">{diaryDate.content}</div>
      </section>
    </div>
  )
}

export default Viewer