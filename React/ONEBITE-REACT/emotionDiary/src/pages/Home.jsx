import { useSearchParams } from "react-router-dom"
import { getEmotionImage } from "../util/get-motion-image"
import Button from "../components/Button"
import Header from "../components/Header"
import DiaryList from "../components/DiaryList"
import { useContext } from "react"
import { DiaryDispatchContext, DiaryStateContext } from "../App"

// 보면 header에서 text를 전달해줘야해서 실제적으로 여기서 진행할 것
// 그리고 diary의 date의 처음년도, 마지막년도를 알아야 filter를 통해 가져올 수 있음 
// 그럼 해당 데이터를 받아오고 => 해당 내용이 mount 되었을 때 년도 필터링해서 해당되는 데이터 반환
// data에 맞는 내용이 있을떄마다 => 날짜가 바뀔떄마다 function이 실행되어야 함
// 근데 한번만 mount되면 됨 왜냐면 12월 page에 올때마다 해당 함수를 mount 할 필요가 없기 때문에 => 연도가 바뀌면 모를까
// 새로고침마다 실행할 필요없음 

//다시 아니라고 생각한게 이게 배열로 12월도 있을수도 있고, 11월도 있을 수가 있음.. 
//그래서 state별로 동작을 진행해야하는데.. == 지금 117123125 이러한 형식으로 되어있어서 이것부터 고쳐야 함

// 특정 월의 첫번쨰 날짜, 마지막 날짜 구하기
const getFirsLast = () => {
  let firstDay = new Date(year, month-1, 1)
  let nextMonth = new Date(year, month, 1) //다음 달의 첫번쨰 날짜
  nextMonth.setDate(nextMonth.getDate()-1) //일자로 환산해서 -1시키고
  //Q. setDate ??
  let lastDay = nextMonth

  //해당 date가 범위에 있으면 반환 filter로 

}


// 일단 dateformate을 변경해야함
const dateFormatter = (date) => {
  const year = date.getFullYear()
  const month = date.getMoth() + 1 //month는 +1을 해줘야 함
  const day = date.getDate() //날짜는 getDate 

  //지금 반환하고 싶은 것은 year-month만 
  //다같이 반환도 가능 => 이런식으로 데이트를 반환
  return `${year}년 ${month}월`
}


const Home = () => {
  const data = useContext(DiaryStateContext)  
  console.log('home에서 data확인', data) //여기 자체도 값을 못받아옴 => 지금 data 일기 데이터 필터자체를 받아온 상황
  //지금 data가 배열이고, 객체 == 12월이 있을수도 있고 11월도 있을 수 있음 

  //일단 data한번 보면
  // console.log(data[0].createdDate) //1번쨰 date
  //년 월로 합쳐서 진행.. == 일단 header에서 많이 쓸 것 같긴 한데 ==> 일단 확인 pass

  // 년도 계산으로 버튼 눌렀을 때 진행
  return (
    // Header 컴포넌트 생성필요
    <div>
      {/* header에 들어갈 내용 생성 필요 */}
      <Header text={"2024년 12월"}/> 
      {/* 데이터 정보전달 */}
      <DiaryList data={data}/>
    </div>
  )
}

export default Home