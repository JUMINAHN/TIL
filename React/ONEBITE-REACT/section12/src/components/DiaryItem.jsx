import { useNavigate } from "react-router-dom"
import { getEmotionImage } from "../../util/get-emotion-image"
import Button from "./Button"
import './DiaryItem.css'


const DiaryItem = ({id, emotionId, createdData, content}) => {
  const nav = useNavigate()
  return(
    <div className="DiaryItem">
      <div 
      onClick={() => {
        nav(`/diary/${id}`)
      }}
      className={`img_section img_section_${emotionId}`}>
        <img src={getEmotionImage(emotionId)} alt="" />
      </div>
      <div 
      onClick={() => {
        nav(`/diary/${id}`)
      }}
      className="info_section">  
        <div className="created_date">
          {createdData}
        </div>
        <div className="content">{content}</div>
      </div>
      <div className="button_section">
        <Button 
        onClick={() => {
          nav(`/edit/${id}`)
        }}
        text={'수정하기'}/>
      </div>
    </div>
  )
}

export default DiaryItem