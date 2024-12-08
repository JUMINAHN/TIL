import { getEmotionImage } from '../util/get-motion-image'
import './EmotionItem.css'

//emotionId를 기반으로 
// div태그들로 구성됨
const EmotionItem = ({emotionId, emotionName, onClick, value}) => {
  // console.log('emotionItem 내부 : onClick 알아보기', onClick)
  if (String(emotionId) === String(value)) {
    console.log('emotionId 번호는? ', emotionId)
    console.log('보관한 상태 전달확인? : ', value) //그럼 emotion을 클릭하면 1~5번까지 다 선택된다는 의미.. 
  }

  return (
    <div className={`EmotionItem EmotionItem_${value}`}
    onClick={onClick}>
      {/* 그냥 onClick이 실행되는 것 */}
      {/* 임시로 */}
      <img src={getEmotionImage(emotionId)} alt="" />
      {/* <h4>완전 좋음</h4> */}
      <h4>{emotionName}</h4>
    </div>
  )
}

export default EmotionItem