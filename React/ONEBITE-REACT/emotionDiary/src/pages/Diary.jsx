import { useNavigate, useParams } from "react-router-dom"
import Button from "../components/Button"
import Header from "../components/Header"
import Viewer from './../components/Viewer';
import useDiary from "../hooks/useDiary"
import { useContext, useEffect, useState } from "react"
import { DiaryStateContext } from './../App';
import { changeFormatter } from "../util/get-matching-date";
import { getEmotionImage } from "../util/get-motion-image";


const Diary = () => {
  const nav = useNavigate()
  const [diaryDate, setDiaryDate] = useState()
  const params = useParams()
  const data = useContext(DiaryStateContext)
  const result = useDiary(data, params.id)
  //호출말고 일단 불러오는 것 사용

  useEffect(()=>{
    if (result) {
      // console.log('result' , result)
      setDiaryDate(result)
      // setDiaryDate({
      //   ...result,
      //   createdDate : new Date(Number(result.createdDate))
      // })
      // console.log(changeFormatter(diaryDate.createdDate))
      //데이터 => 못받아오는 이유 객체 new Date()? => 동일한데
    }
  }, [result])

 // 못받아오면 로딩중 => 
  if (!diaryDate) {
    return <div>...로딩중</div>
  }
  // console.log(diaryDate, 'diaryDate 받아와지는데 왜 HeaderText는 못받아오는가?')

  
  // console.log(diaryDate, 'hello')
  return (
    <div>
      {/* hederText 수정 => 일치값을 데이터 변환해줄 것 */}
      <Header text={`${changeFormatter(new Date(diaryDate.createdDate))}의 기록`}
      leftChild={<Button text={"< 뒤로가기"}
      onClick={() => nav(-1)}/>}
      rightChild={<Button text={"수정하기"}
      onClick={() => nav(`/edit/${params.id}`)}/>}/>
      <Viewer 
      diaryDate={diaryDate}/>
    </div>
  )
}

export default Diary