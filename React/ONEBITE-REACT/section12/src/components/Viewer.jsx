import './Viewer.css'
import { getEmotionImage } from '../../util/get-emotion-image'
import { EmotionList } from '../../util/constant'

const Viewer = ({emotionId, content}) => {
  //emotion Id를 기준으로 const Emotion id 내용 꺼내온다
  const emotionItem = EmotionList.find((item) => 
  String(item.emotionId) === String(emotionId))

  return (
    <div>
      <div className='Viewer'>
        <section className="img_section">
          <h4>
            오늘의 감정
          </h4>
          <div className={`emotion_img_wrapper emotion_img_wrapper_${emotionId}`}>
            <img src={getEmotionImage(emotionId)} alt="" />
            <div>{emotionItem.emotionName}</div>
          </div>
        </section>
        <section className="content_section">
          <h4>오늘의 일기</h4>
          <div className="content_wrapper">
            <p>{content}</p>
          </div>
        </section>
      </div>
    </div>
  )
}

export default Viewer