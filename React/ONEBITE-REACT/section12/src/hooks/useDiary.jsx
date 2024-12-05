import { useContext, useEffect, useState } from "react"
import { DiaryDispatchContext, DiaryStateContext } from "../App"
import { useNavigate } from "react-router-dom"

// 커스텀 훅을 사용함 => 그냥 use .. type을 묶어서 만들 수 없기 때문

const useDiary = (id) => { //params id 인수로 전달해서 diary값 호출
  const data = useContext(DiaryStateContext) 
  const [currentDiaryItem, setCurrentDiaryItem] = useState()
  const nav = useNavigate()

    //mount된 이후, 일기 데이터를 통해서 진행할 수 있음
    useEffect(()=>{ //getCurrentDiary가 하던기능 그대로 넣어줌
      const currentDiaryItem = data.find((item) => 
        String(item.id) === String(id))
        
        if (!currentDiaryItem) {
          window.alert('존재하지 않는 일기입니다.')
          // 홈페이지로 보내달라고 했는데 그대로 수정에만 진행됨
          nav('/', {replace : true})
        }
        setCurrentDiaryItem(currentDiaryItem) //값이 있으면 그냥 이 값 자체를 반환해주면 됨
        //이 값을 보관할 곳이 없기 떄문에 저장할 state 만들어줌
    }, [id, data])
  return currentDiaryItem
}

export default useDiary