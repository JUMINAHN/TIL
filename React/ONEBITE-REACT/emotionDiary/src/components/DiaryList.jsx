import Button from './Button'
import DiaryListItem from './DiaryListItem'
import './DiaryList.css'
import { useNavigate } from 'react-router-dom'
import { useState } from 'react'


// const changeDateFormatter = (date) => {
//   console.log(date)
//   const newDate = new Date(date)
//   const year = newDate.getFullYear()
//   const month = newDate.getMonth() + 1
//   const day = newDate.getDate()
//   return `${year}-${month}-${day}`
// }


// 강의에서는 number를 활용 => date가 아니라
// return Number(a.createdDate) - Number(b.createdDate)

// data, dateStatus => 변수명을 따로 받진 않음..
// const sortData = (data, dateStatus) => {
//   if (dateStatus === "oldest") {
//     return data.toSorted((a, b) =>
//        new Date(a.createdDate) - new Date(b.createdDate))
//     // // 더 작은 값이 먼저 온다.
//     // console.log(oldestDate, '오래된 순 : 정렬 값')
//     // // return oldestDate
//     // setSortDate(oldestDate) //이거 컴포넌트 내부로?
//   } else {
//     return data.toSorted((a, b) =>
//       new Date(b.createdDate) - new Date(a.createdDate))
//     // console.log(latestDate, '최신순 : 정렬값')
//     // // return latestDate
//     // setSortDate(latestDate) //이거 컴포넌트 내부로?
//   }
// }

const DiaryList = ({data}) => {
  const [dateStatus, setDateStatus] = useState("latest") //최신순 기준?

  // const [sortDate, setSortDate] = useState(new Date())  //이거도 status의 영향을 받기 떄문에 굳이 필요없었음
  // 아직 sesortDate 사용하진 않음
  // console.log('DiaryList', data) 
  // const formatData = data.map((item) => changeDateFormatter(item.createdDate))

  // console.log('클릭시마다 변경 확인', dateStatus) //oldest는 확인할 수 없나..? 
  //변경이 안되는건가?
  const onChangeStatus = (e) => {
    //e.target.value 확인 => onCHange의 경우 value도 넣어줘야 확인 가능
    // console.log(e.target.value)
    setDateStatus(e.target.value) // 값을 바꿔준다.
    //이떄 같이
    // sortData(data, dateStatus)
  }

  //그냥 클릭 버튼누를떄 필터링되는것과 동일하게 진행하면 되었었떤 문제,,
  //onchange가 실행되면서 같이 진행되는

  //클릭 자체 데이터가 state니까 유동적 변경
  // return 누락
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
      {/* select 결과에 따라서 진행됨 */}
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