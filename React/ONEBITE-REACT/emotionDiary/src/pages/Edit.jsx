import { useNavigate, useParams } from "react-router-dom"
import Header from "../components/Header"
import Button from "../components/Button"
import Editor from "../components/Editor"
import { useContext } from "react"
import { DiaryDispatchContext, DiaryStateContext } from "../App"


const Edit = () => {
  const params = useParams()
  const nav = useNavigate()
  const data = useContext(DiaryStateContext)
  const {onUpdate, onDelete} = useContext(DiaryDispatchContext) //onDelete를 여기서 호출하는게 아니라 내부적으로 활용할 것
  // console.log(params) //params는 id값을 가진다.

  //params로 받았는데 일치하는 emotionId, emotionName, Date, diary 를 매칭해서 활용할 필요가 있지 않을까?
  //=> 매칭을 하려면..? => status가 editor에 존재

  const onClickDelete = () => {
    //정말로 삭제할까요?
    if (window.confirm("정말 삭제할까요?")) {
      onDelete(params.id) //params를 전해준다. => 확인
      nav('/') //삭제 완료 => 삭제되는 것을 볼 수 있음
    }
  }

  const onSubmit = (input) => {//타임스탬프 형식
    // onUpdate((input.createdDate).getTime(), input.emotionId, input.content, params.id)
    if (window.confirm('정말 수정할까요?')) {
      onUpdate((input.createdDate).getTime(), input.emotionId, input.content, params.id)
      nav('/', {replace : true})
    }
  }

  //params 기반으로 그냥 삭제 onDelete 실행해주면 됨
  return (
    <div>
      <Header text={"일기 수정하기"}
      leftChild={<Button text={"< 뒤로 가기"}
      onClick={() => nav(-1)}/>}
      rightChild={<Button text={"삭제하기"} type={"NEGATIVE"}
      onClick={onClickDelete}/>}></Header>
      <Editor
      data={data}
      params={params}
      onSubmit={onSubmit}/>
      {/* <p>{params.id}번 Edit입니다.</p> */}
    </div>
  )
}

export default Edit