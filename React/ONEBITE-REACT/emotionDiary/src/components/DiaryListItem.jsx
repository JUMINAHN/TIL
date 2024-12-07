import { useNavigate } from 'react-router-dom';
import { getEmotionImage } from '../util/get-motion-image'
import Button from './Button';
import './DiaryListItem.css'

// 각 요소들을 클릭했을떄 원하는 동작을 수행할 수 있도록 진행
// 일단 수정하기를 누르면 이동할 수 있도록


const DiaryListItem = ({id, createdDate, emotionId, content}) => {
  const nav = useNavigate()
  return (
    <div className="DiaryListItem">
      <section className={`img_section img_section_${emotionId}`}>
        <img src={getEmotionImage(emotionId)} alt="" />
      </section>
      <section className='info_section'
      onClick={() => nav(`/diary/${id}`)}>
        {/* onClick 했을때 해당 내용이 실행되게 구현을 하는거 아닌가? 왜 그냥 nav를 해도 이동이 되는것인지 궁금함 */}

        {/* div 구조로 만들기 각각 데이터 타입 관리를 위해 */}
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