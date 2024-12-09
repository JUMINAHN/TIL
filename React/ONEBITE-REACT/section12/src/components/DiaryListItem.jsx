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
        <div className='content'>{content}</div>
      </section>
      <section className='btn_section'>
        <Button 
        onClick={()=> {nav(`/edit/${id}`)}}
        text={"수정하기"}/>
      </section>
    </div>
  )
}

export default DiaryListItem