import { useSearchParams } from "react-router-dom"
import { getEmotionImage } from "../util/get-motion-image"
import Button from "../components/Button"
import Header from "../components/Header"
import DiaryList from "../components/DiaryList"
import { useContext, useEffect, useState } from "react"
import { DiaryDispatchContext, DiaryStateContext } from "../App"


const getMonthlyData = (pivotDate, data) => {
  const beginDate = new Date(pivotDate.getFullYear(), pivotDate.getMonth(), 1, 0, 0, 0).getTime() //0시 0분 0초
  const endDate = new Date(pivotDate.getFullYear(), pivotDate.getMonth()+1, 0, 23, 59, 59).getTime() //0으로 설정하면 => -1일 마지막 값이 됨 => 따라서 마지막 날 시분초 조심
  return data.filter((item) => beginDate <= item.createdDate && item.createdDate <= endDate) 
}

const Home = () => {
  const data = useContext(DiaryStateContext) //받아온 data => date와 일치여부 판단 진행할 것
  const [pivotDate, setPivotDate] = useState(new Date()) //기준이 될 날짜

  const onClickBeforeDate = (pivotDate) => {
    setPivotDate(new Date(pivotDate.getFullYear(), pivotDate.getMonth()-1))
  }

  const onClickAfterDate = (pivotDate) => {
    setPivotDate(new Date(pivotDate.getFullYear(), pivotDate.getMonth()+1))
  }
  const filterDiaryData = getMonthlyData(pivotDate, data) 

  return (
    // Header 컴포넌트 생성필요
    <div>
      <Header text={`${pivotDate.getFullYear()}년
      ${pivotDate.getMonth()+1}월`}
      rightChild={<Button
      onClick={() => onClickAfterDate(pivotDate)}
      text={">"}/>}
      leftChild={<Button 
      onClick={() => onClickBeforeDate(pivotDate)}
      text={"<"}/>}/> 
      <DiaryList data={filterDiaryData}/>
    </div>
  )
}

export default Home