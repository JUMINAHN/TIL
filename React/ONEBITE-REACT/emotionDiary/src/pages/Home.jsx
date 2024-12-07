import { useSearchParams } from "react-router-dom"
import { getEmotionImage } from "../util/get-motion-image"
import Button from "../components/Button"
import Header from "../components/Header"
import DiaryList from "../components/DiaryList"
import { useContext, useState } from "react"
import { DiaryDispatchContext, DiaryStateContext } from "../App"

// 특정 월의 첫번쨰 날짜, 마지막 날짜 구하기
// const getFirsLast = () => {
//   let firstDay = new Date(year, month-1, 1)
//   let nextMonth = new Date(year, month, 1) //다음 달의 첫번쨰 날짜
//   nextMonth.setDate(nextMonth.getDate()-1) //일자로 환산해서 -1시키고
//   //Q. setDate ??
//   let lastDay = nextMonth

//   //해당 date가 범위에 있으면 반환 filter로 

// }


// // 일단 dateformate을 변경해야함
// const dateFormatter = (date) => {
//   const year = date.getFullYear()
//   const month = date.getMonth() + 1 //month는 +1을 해줘야 함
//   const day = date.getDate() //날짜는 getDate 

//   //지금 반환하고 싶은 것은 year-month만 
//   //다같이 반환도 가능 => 이런식으로 데이트를 반환
//   return `${year}년 ${month}월`
// }


const Home = () => {
  const data = useContext(DiaryStateContext) //받아온 data => date와 일치여부 판단 진행할 것
  console.log('home에서 data확인', data)
  //일단 현재날짜로 초기 설정을 해줘야 함 => 왜냐면 지금 다이어리도 현재 날짜 기준 
  const [date, setDate] = useState(new Date()) //useState값이 없기 때문 -> 지금 바로 date => dateFormatter Error 발생
  // const monthYear = dateFormatter(date) // 오타 문제 => Header와 관련된 날짜 문제
  



  // 년도 계산으로 버튼 눌렀을 때 진행
  return (
    // Header 컴포넌트 생성필요
    <div>
      {/* header에 들어갈 내용 생성 필요 */}
      {/* 판단하에 현재 date값만 전달해줄 필요가 있다고 생각함 ==지금은 일단 newDate()값 기준,, */}
      <Header text={date}/> 
      {/* 데이터 정보전달 */}
      <DiaryList data={data}/>
    </div>
  )
}

export default Home