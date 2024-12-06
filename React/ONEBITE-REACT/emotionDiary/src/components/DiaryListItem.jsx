import { getEmotionImage } from '../util/get-motion-image'
import Button from './Button';
import './DiaryListItem.css'

//item에 들어있는 요소들 => 다 구조분해 할당으로 진행하고
//img를 어떻게 가져올 것인가?

const DiaryListItem = ({id, createdDate, emotionId, content}) => {
  // 받아온 데이터들 item 자체
  return (
    <div className="DiaryListItem">
      <section className={`img_section img_section_${emotionId}`}>
        <img src={getEmotionImage(emotionId)} alt="" />
      </section>
      <section className='info_section'>
        {/* div 구조로 만들기 각각 데이터 타입 관리를 위해 */}
        <div className='created_date'>{createdDate}</div>
        {/* 일단 이거 추후 2022.05.31 구조로 바꿀 것 */}
        <div className='content'>{content}</div>
      </section>
      <section className='btn_section'>
        <Button 
        text={"수정하기"}/>
      </section>
    </div>
  )
}

export default DiaryListItem