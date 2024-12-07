import Button from './Button'
import './Header.css'

// 일단 dateformate을 변경해야함
const dateFormatter = (date) => { //Home에 있는 내용을 Header로 옮겨와서 문제 없음
  const year = date.getFullYear()
  const month = date.getMonth() + 1 //month는 +1을 해줘야 함
  const day = date.getDate() //날짜는 getDate 

  //지금 반환하고 싶은 것은 year-month만 
  //다같이 반환도 가능 => 이런식으로 데이트를 반환
  return `${year}년 ${month}월`
}

// 특정 월의 첫번쨰 날짜, 마지막 날짜 구하기
const getFirsLast = (date) => {
  //date를 받아와서 year, month 추출
  const year = date.getFullYear()
  const month = date.getMonth() + 1

  let firstDay = new Date(year, month-1, 1)
  let nextMonth = new Date(year, month, 1) //다음 달의 첫번쨰 날짜
  nextMonth.setDate(nextMonth.getDate()-1) //일자로 환산해서 -1시키고
  //Q. setDate의 의미??
  let lastDay = nextMonth
  //해당 date가 범위에 있으면 반환 filter로 
  return [firstDay, lastDay]
}


// Q. props의 키 값을 기준으로 받아오는 것인지?
const Header = ({text}) => { 
  const monthYear = dateFormatter(text) // 오타 문제 => Header와 관련된 날짜 문제
  //text받아와서 진행..
  //text에 현재의 date를 받아왔는지에 대해 확인해보기
  console.log('날짜 값을 받아왔습니다 : ', text)
  //왼쪽으로 갈때 date 감소
  //오른쪽 갈떄 date 증가

  //근데 중요한 것은 이렇게 해도 state가 선언되어 있지 않기 때문에 동작 랜더링이 되지 않을 것..
  //clickEvent로 달력 날짜 조정 => 지금 근데 lastMonth에서 조정을 해야하는데 Home에서 날짜 formatt을 변환하는 것은 아닌 것 같음 
  //근데 이것자체가 filter를 했을떄의 전제,,
  const onClickLastMonth = (text) => { //지금 date의 month -1 ..?
    //daetFormatter로 넘기면 되는데 여기서 어떻게 값을 하나 더 증가시킨..
    const lastMonth = new Date(text).addMonth(-1)

  }
  const onClickNextMonth = (text) => { //지금 date의 month + 1
    const nextMonth = new Date(text).addMonth(1)
  }

  return (
    <div className='Header'> 
      <div className="header_left">
        <Button text={"<"}
        onClick={onClickLastMonth}/>
      </div>
      <div className="header_title">{`${monthYear}의 일기`}</div>
      <div className="header_right">
        <Button text={">"}
        onClick={onClickNextMonth}/>
      </div>
    </div>
  )
}

export default Header