import { useNavigate } from "react-router-dom"
import Button from "./Button"
import DiaryItem from "./DiaryItem"
import './DiaryList.css'
import { useState } from "react"


const DiaryList = ({data}) => {
  const nav = useNavigate()

  //드롭다운 => 선택된 option의 value를 가져온다
  //예를 들어 "최신순"을 선택하면 "latest", "오래된 순"을 선택하면 "oldest" 값을 가져옵니다
  const [sortType, setSortType] = useState("latest") 
  const onChangeSortType = (e) => {
    setSortType(e.target.value)
    //setSortType으로 그 값을 저장하면:sortType이 바뀌고 그에 따라 일기 목록이 다시 정렬됩니다
  }

  const getSortedDate = () => {
    return data.toSorted((a,b) => {
      if (sortType === "oldest") {
        return new Date(a.createdDate) - new Date(b.createdDate) 
      } else {
        return new Date(b.createdDate) - new Date(a.createdDate) 
      }
    })
  }

  const sortedData = getSortedDate() 

  return (
    <div className="DiaryList">
      <div className="menu_bar">
        <select
        onChange={onChangeSortType}>
          {/* 정렬관련 */}
          <option value={"latest"}>최신순</option>
          <option value={"oldest"}>오래된 순</option>
        </select>
        <Button 
        onClick={() => nav('/new')}
        text={'새 일기 쓰기'}
      type={"POSITIVE"}/>
      </div>
      <div className="list_wrapper">
        {sortedData.map((item) => <DiaryItem 
        key={item.id}
        {...item}/>)}
        {/* <DiaryItem/>  */}
      </div>
    </div>
  )
}

export default DiaryList