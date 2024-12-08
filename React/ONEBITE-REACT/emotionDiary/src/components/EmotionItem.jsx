import { getEmotionImage } from '../util/get-motion-image'
import './EmotionItem.css'


const EmotionItem = ({emotionId, emotionName, onClick, isSelected}) => {

  // selected가 트루면 => 아닌 애들은 false이고
  // true인 애들은 이거가 들어갈 것
  return (
    <div className={`EmotionItem ${isSelected ? `EmotionItem_${emotionId}` : ""}`}
    onClick={onClick}>
      {/* 여기는 또 className들을 다 존재시켜줌 */}
      <img className="emotion_img" src={getEmotionImage(emotionId)} alt="" />
      <h4 className="emotion_name">{emotionName}</h4>
    </div>
  )
}

export default EmotionItem