import { useNavigate } from "react-router-dom"
import Button from "./Button"
import DiaryItem from "./DiaryItem"
import './DiaryList.css'
import { useState } from "react"


const DiaryList = ({data}) => {
  const nav = useNavigate()

  const [sortType, setSortType] = useState("latest") 
  const onChangeSortType = (e) => {
    setSortType(e.target.value)
  }

  //최신순으로 먼저 하고, 그다음 그 내부데이터도 진짜 정렬
  //Q. js의 sort와 toSorted => 새로운 배열 반환
  //사전순으로 ㅂ나환 : 객체는 제대로 작동XX
  //Q. 하기에 뭔말?
  const getSortedDate = () => {
    return data.toSorted((a,b) => {
      if (sortType === "oldest") {
        return Number(a.createdData) - Number(b.createdData)
      } else {
        return Number(b.createdData) - Number(a.createdData)
      }
    })
  }

  const sortedData = getSortedDate() //저장 => 이런거 왜해줌?

  return (
    <div className="DiaryList">
      <div className="menu_bar">
        <select
        onClick={onChangeSortType}>
          {/* 정렬관련 */}
          <option value={"latest"}>최신순</option>
          <option value={"oldest"}>오래된 순</option>
        </select>
        <Button 
        onClick={() => nav('/new')}
        text={'새 일기 쓰기'}
        // 여기서는 div로 안감싸고 바로 button 저긴 왜?div로 
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