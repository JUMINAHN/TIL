import { useState } from "react"
import KoreanFood from "./KoreanFood"
import ChineseFood from "./ChineseFood"
import ItalianFood from "./ItalianFood"

const FoodList = () => {
  //한식, 양식, 중식 관련 => foodcategory들을 선택하고, 담을 state 필요
  const [category, setCategory] = useState("All") //일단 모든 음식을 보여주도록
  //기본 값으로
  //선택한다
  const getCategory = () => {
    switch (category) {
      case "Korean": //KoreanFood 자체
        return <KoreanFood /> 
      case "Chinese" :
        return <ChineseFood />
      case "Italian":
        return <ItalianFood />
      default : //모든 카테고리
        return ( //기본 값으로
          <ul>
            <li>김치찌개</li>
            <li>피자</li>
            <li>불고기</li>
            <li>파스타</li>
            <li>탕수육</li>
            <li>비빔밥</li>
            <li>짜장면</li>
            <li>라자냐</li>
            <li>볶음밥</li>
          </ul>
        )
    }
  }
  
  //category 값
  return (
    <div>
      <h1>ZOOM'S KITCHEN MENU</h1>
      <select onChange={(e) => setCategory(e.target.value)}>
        <option value="All">All</option>
        <option value="Korean">한식</option>
        <option value="Chinese">중식</option>
        <option value="Italian">양식</option>
      </select>
    {getCategory()}
    </div>
  )
}

export default FoodList