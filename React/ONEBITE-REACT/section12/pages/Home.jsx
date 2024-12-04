import { useContext, useState } from "react"
import Button from "../src/components/Button"
import Header from "../src/components/Header"
import DiaryList from './../src/components/DiaryList'
import { DiaryStateContext } from "../src/App"


const getMonthlyData = (pivotDate, data) => { //오늘 날짜, 일기 데이터(날짜)
  
  const beginTime = new Date(
    pivotDate.getFullYear(),
    pivotDate.getMonth(),
    1, //1일 기준
    0,
    0,
    0
  ).getTime() //timestamp

  const endTime = new Date(
    pivotDate.getFullYear(),
    pivotDate.getMonth() + 1, //다음달
    0, //0으로 설정했을때(0일) => 마지막 날로 된다.
    23,
    59,
    59
  ).getTime()
  return data.filter((item) => beginTime <= item.createdData && item.createdData <= endTime)
  

}

const Home = () => {
  const data = useContext(DiaryStateContext) // 일기 전체의 데이터
  const [pivotDate, setPivotDate] = useState(new Date())
  const monthlyData = getMonthlyData(pivotDate, data) 

  console.log(monthlyData, 'monthlyData')

  const onIncreaseMonth = () => {
    setPivotDate(new Date(pivotDate.getFullYear(), pivotDate.getMonth() + 1))
  }

  const onDecreaseMonth = () => {
    setPivotDate(new Date(pivotDate.getFullYear(), pivotDate.getMonth() - 1))
  }

  return (
    <div>
      <Header title={`${pivotDate.getFullYear()}년  
      ${pivotDate.getMonth() + 1}월`}
      // 왼쪽을 누르면 한달이전
      leftChild={<Button 
        onClick={onDecreaseMonth}
        text={'<'}/>}
      // 오른쪽으 한달뒤로
      rightChild={<Button 
        onClick={onIncreaseMonth}
        text={'>'}/>}
      />
      <DiaryList 
      data={monthlyData}/>
    </div>
  )
}

export default Home