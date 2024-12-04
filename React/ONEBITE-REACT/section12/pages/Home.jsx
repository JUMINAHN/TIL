import { useContext, useState } from "react"
import Button from "../src/components/Button"
import Header from "../src/components/Header"
import DiaryList from './../src/components/DiaryList'
import { DiaryStateContext } from "../src/App"


// 이번달과 끝달의 위치를 알아야 그 범위를 알 수 있음
// Q. 그런데 궁금한게 이건 왜 Home component안에서 안함? 밖에서 해도 되는 기준이 뭔지 
// Q. getMethod
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
  // 생성 날짜 범으; 확인
  // console.log(beginTime, 'beginTime');
  // console.log(endTime, 'endTime');

  //Q?여기 보면 filter에 또 
  return data.filter((item) => beginTime <= item.createdData && item.createdData <= endTime)
  
  //하기와 뭔차이 QQ?? 
  // const filteredData = data.filter((item) => {
  //   console.log(item.createdDate, 'item.createdDate');
  //   return beginTime <= item.createdDate && item.createdDate <= endTime;
  // });
  // console.log(filteredData, 'filteredData');
  // return filteredData;
}

// 일기 내용을 data로 받아와야 함
// 달력에 맞는 값 출력을 위해서
const Home = () => {
  const data = useContext(DiaryStateContext) // 일기 전체의 데이터
  const [pivotDate, setPivotDate] = useState(new Date())
  const monthlyData = getMonthlyData(pivotDate, data) //#Q??
  // console.log(data, 'data')
  // console.log(pivotDate, 'pivotDate')
  console.log(monthlyData, 'monthlyData')

  const onIncreaseMonth = () => {
    //새로운 값을 줘야하니까 => 근데 기준이 지금 가지고 있는 년 기준
    // Q. 어떻게 월이 바뀌고 년도 자동으로 바뀜?
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