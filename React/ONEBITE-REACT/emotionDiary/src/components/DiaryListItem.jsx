import { useNavigate } from 'react-router-dom';
import { getEmotionImage } from '../util/get-motion-image'
import Button from './Button';
import './DiaryListItem.css'


const DiaryListItem = ({id, createdDate, emotionId, content}) => {
  const nav = useNavigate()
  return (
    <div className="DiaryListItem">
      <section className={`img_section img_section_${emotionId}`}>
        <img src={getEmotionImage(emotionId)} alt="" />
      </section>
      <section className='info_section'
      onClick={() => nav(`/diary/${id}`)}>

        <div className='created_date'>{new Date(createdDate).toLocaleDateString()}</div>
        {/* 일단 이거 추후 2022.05.31 구조로 바꿀 것 */}
        <div className='content'>{content}</div>
      </section>
      <section className='btn_section'>
        <Button 
        //특정 id로 이동할 수 있또록 => 받은 id를 기반으로
        onClick={()=> {nav(`/edit/${id}`)}}
        text={"수정하기"}/>
      </section>
    </div>
  )
}

export default DiaryListItem