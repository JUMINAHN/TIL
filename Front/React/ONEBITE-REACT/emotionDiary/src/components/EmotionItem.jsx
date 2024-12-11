import { getEmotionImage } from '../util/get-motion-image'
import './EmotionItem.css'


const EmotionItem = ({emotionId, emotionName, onClick, isSelected}) => {
  return (
    <div className={`EmotionItem ${isSelected ? `EmotionItem_${emotionId}` : ""}`}
    onClick={onClick}>
      <img className="emotion_img" src={getEmotionImage(emotionId)} alt="" />
      <h4 className="emotion_name">{emotionName}</h4>
    </div>
  )
}

export default EmotionItem