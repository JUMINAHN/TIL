//Edit 페이지 수정

import { useEffect, useState } from "react"

// diarydata, params.id

const useDiary = (data, id) => {
  const [currentDiaryItem, setCurrentDiaryItem] = useState()
    useEffect(()=>{
      const innerData = data.find((item) => String(item.id) === String(id))
      // console.log(innerData, 'innerData?')
      if(!innerData) {
        //없다면
        window.alert('존재하지 않는 일기입니다.')
        nav('/', {replace : true}) //여기
      }
      setCurrentDiaryItem(innerData)
      //저장할 곳
    }, [data, id]) //data랑 params.id는 변경되니까

  return currentDiaryItem  
}

export default useDiary