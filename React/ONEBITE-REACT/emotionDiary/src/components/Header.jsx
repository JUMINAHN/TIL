import Button from './Button'
import './Header.css'

//일단 dateformate을 변경해야함
// const dateFormatter = (date) => { //Home에 있는 내용을 Header로 옮겨와서 문제 없음
//   const year = date.getFullYear()
//   const month = date.getMonth() + 1 //month는 +1을 해줘야 함
//   const day = date.getDate() //날짜는 getDate 
//   return `${year}년 ${month}월`
// }

// 특정 월의 첫번쨰 날짜, 마지막 날짜 구하기
// const getFirsLast = (date) => {
//   const year = date.getFullYear()
//   const month = date.getMonth() + 1
//   let firstDay = new Date(year, month-1, 1)
//   let nextMonth = new Date(year, month, 1) //다음 달의 첫번쨰 날짜
//   nextMonth.setDate(nextMonth.getDate()-1) //일자로 환산해서 -1시키고
//   let lastDay = nextMonth
//   return [firstDay, lastDay]
// }


// Q. props의 키 값을 기준으로 받아오는 것인지?
const Header = ({text, leftChild, rightChild}) => { 
  //형식 반환
  // const monthYear = dateFormatter(text)
  // //날짜 범위 추출
  // const dateLange = getFirsLast(text)



  // const onClickLastMonth = (text) => { //지금 date의 month -1 ..?
  //   //daetFormatter로 넘기면 되는데 여기서 어떻게 값을 하나 더 증가시킨..
  //   console.log(text)
  //   console.log(new Date(text))
  //   console.log(new Date(text).getMonth(), 'getMonth')
  //   console.log(new Date(text).toLocaleDateString(), 'getDateString')
  //   const lastMonth = new Date(text).getMonth() - 1 //NAN
  //   console.log(lastMonth)

  // }
  // const onClickNextMonth = (text) => { //지금 date의 month + 1
  //   const nextMonth = new Date(text).getMonth() + 1
  //   console.log(nextMonth)
  // }

  return (
    <div className='Header'> 
      <div className="header_left">
        {/* <Button text={"<"}
        onClick={() => onClickLastMonth}/> */}
        {leftChild}
        {/* 그럼 여기서 onClick이 되어야하는데 how? */}
      </div>
      <div className="header_title">{text}</div>
      <div className="header_right">
        {/* <Button text={">"}
        onClick={() => onClickNextMonth}/> */}
        {rightChild}
      </div>
    </div>
  )
}

export default Header