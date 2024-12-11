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
  
  // console.log(params) //params는 id값을 가진다.

  //params로 받았는데 일치하는 emotionId, emotionName, Date, diary 를 매칭해서 활용할 필요가 있지 않을까?
  //=> 매칭을 하려면..? => status가 editor에 존재
  //input값을 기반으로 매칭 => input => 근데 input값? => 들어있는가? : New에서 있었던 것..? => 그냥 data자체에서 매칭시켜야할 것 같은데
  //동일한 내용을 useEffect로 만든다
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
      //해당 nav는 컴포넌트가 렌더링이 되고 삭제버튼을 눌렀을떄 동작
    }
  }

  // const currentDiaryItem = findData() //이거 때문에


  const onSubmit = (input) => {//타임스탬프 형식
    // onUpdate((input.createdDate).getTime(), input.emotionId, input.content, params.id)
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
      {/* <p>{params.id}번 Edit입니다.</p> */}
    </div>
  )
}

export default Edit