import { replace, useNavigate, useParams } from "react-router-dom"
import Header from "../components/Header"
import Button from "../components/Button"
import Editor from "../components/Editor"
import { useContext, useEffect, useState } from "react"
import { DiaryDispatchContext, DiaryStateContext } from "../App"


const Edit = () => {
  const params = useParams()
  const nav = useNavigate()
  const {onUpdate, onDelete} = useContext(DiaryDispatchContext) //onDelete를 여기서 호출하는게 아니라 내부적으로 활용할 것
  const data = useContext(DiaryStateContext)
  const [currentDiaryItem, setCurrentDiaryItem] = useState()

  
  useEffect(()=>{
    const innerData = data.find((item) => String(item.id) === String(params.id))
    console.log(innerData, 'innerData?')
    if(!innerData) {
      //없다면
      window.alert('존재하지 않는 일기입니다.')
      nav('/', {replace : true}) //여기
    }
    setCurrentDiaryItem(innerData)
    //저장할 곳
  }, [data, params.id]) //data랑 params.id는 변경되니까

  const onClickDelete = () => {
    //정말로 삭제할까요?
    if (window.confirm("정말 삭제할까요?")) {
      onDelete(params.id) //params를 전해준다. => 확인
      nav('/', {replace : true}) //삭제 완료 => 삭제되는 것을 볼 수 있음
    }
  }


  const onSubmit = (input) => {//타임스탬프 형식
    if (window.confirm('정말 수정할까요?')) {
      onUpdate((input.createdDate).getTime(), input.emotionId, input.content, params.id)
      nav('/', {replace : true})
    }
  }
  console.log(currentDiaryItem, 'CurrentDiaryItem 들어갔니? == 안들어감')


  //params 기반으로 그냥 삭제 onDelete 실행해주면 됨
  return (
    <div>
      <Header text={"일기 수정하기"}
      leftChild={<Button text={"< 뒤로 가기"}
      onClick={() => nav(-1)}/>}
      rightChild={<Button text={"삭제하기"} type={"NEGATIVE"}
      onClick={onClickDelete}/>}></Header>
      <Editor
      data={currentDiaryItem}
      // params={params}
      onSubmit={onSubmit}/>
    </div>
  )
}

export default Edit