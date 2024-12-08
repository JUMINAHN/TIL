import Button from './Button'
import DiaryListItem from './DiaryListItem'
import './DiaryList.css'
import { useNavigate } from 'react-router-dom'
import { useState } from 'react'



const DiaryList = ({data}) => {
  const [dateStatus, setDateStatus] = useState("latest") //최신순 기준?

  const onChangeStatus = (e) => {
    setDateStatus(e.target.value) // 값을 바꿔준다.

  }

  const sortData = () => {
    // 중복 코드 제거
    return data.toSorted((a, b) => {
    if (dateStatus === 'oldest') {
      return new Date(a.createdDate) - new Date(b.createdDate)
    } else {
      return new Date(b.createdDate) - new Date(a.createdDate)
    }
    })
}

  const resultSortDate = sortData()

  const nav = useNavigate()
  return (
  <div className="DiaryList">
    <div className='menu_bar'>
      <select onChange={onChangeStatus} value={dateStatus}>
        <option value={"latest"} >최신순</option>
        <option value={"oldest"} >오래된 순</option>
      </select>
      <Button 
      onClick={() => {nav("/new")}}
      text={"새 일기쓰기"}
      type={"POSITIVE"}/>
    </div>

    <div className='list_wrapper'>
      {resultSortDate.map((item) => 
      <DiaryListItem 
      key={item.id}
      {...item}/>)}
    </div>
  </div>
  )
}

export default DiaryList