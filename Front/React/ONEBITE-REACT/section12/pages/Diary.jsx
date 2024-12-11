import { useNavigate, useParams } from "react-router-dom"
import Header from "../src/components/Header"
import Button from "../src/components/Button"
import Viewer from "../src/components/Viewer"
import useDiary from "../src/hooks/useDiary"
import { getStringDate } from "../util/get-stringed-date"
import usePageTitle from "../src/hooks/usePageTitle"


const Diary = () => {
  //params 저장
  const params = useParams() //params 값
  const nav = useNavigate()
  usePageTitle(`${params.id}번 일기`)
  const currentDiaryItem = useDiary(params.id)
  if (!currentDiaryItem) {
    return <div>데이터 로딩중..!!</div>
  }
  console.log(currentDiaryItem) //최초 undefined 그리고 useEffect가 실행되어서 console.log로 받기

  const {createdDate, emotionId, content} = currentDiaryItem
  const title = getStringDate(new Date(createdDate))

  return (
    <div>
      <Header title={`${title} 기록`}
      leftChild={<Button text={"< 뒤로가기"}
      onClick={() => nav(-1)}/>}
      rightChild={<Button text={"수정하기"}
      onClick={() => nav(`/edit/${params.id}`)}/>}/>
    <Viewer 
    emotionId={emotionId}
    content={content}/>
    </div>
  ) 
}

export default Diary    