import { getEmotionImage } from '../util/get-motion-image'
import './EmotionItem.css'


// div태그들로 구성됨
const EmotionItem = ({emotionId, emotionName}) => {
  return (
    <div className='EmotionItem'>
      {/* 임시로 */}
      {/* <img src={getEmotionImage(1)} alt="" /> */}
      <img src={getEmotionImage(emotionId)} alt="" />
      {/* <h4>완전 좋음</h4> */}
      <h4>{emotionName}</h4>
    </div>
  )
}

export default EmotionItem