//edit

export const changeFormatter = (date) => { 
  // input으로 입력되는 친구도 똑같은 문자열이기 때문에 날짜로 다시 변환
    // console.log(date)
    const year = date.getFullYear()
    const month = date.getMonth() + 1
    const day = date.getDate()
    //근데 단순히 작성하면 2024-12-8 => 우리가 원하는 00-00이 아님
    if (month < 10 && day < 10) {
      return `${year}-0${month}-0${day}`
    } else if (month < 10) {
      return `${year}-0${month}-${day}`
    } else if (day < 10) {
      return `${year}-${month}-0${day}`
    } else {
      return `${year}-${month}-${day}`
    }
  } 