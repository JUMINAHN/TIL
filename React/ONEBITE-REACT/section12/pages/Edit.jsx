import { replace, useNavigate, useParams } from "react-router-dom"
import Header from './../src/components/Header'
import Button from "../src/components/Button"
import Editor from "../src/components/Editor"
import { DiaryDispatchContext, DiaryStateContext } from "../src/App"
import { useContext, useEffect, useState } from "react"



const Edit = () => {
  const params = useParams()
  // console.log(params)
  //params를 기준으로 모든 데이터를 받아올 수 있어야 함
  //app의 data에서 우리가 원하는것만 받아오며 됨
  const nav = useNavigate()
  const {onDelete, onUpdate} = useContext(DiaryDispatchContext)
  const data = useContext(DiaryStateContext) 
  // console.log(data)
  const [currentDiaryItem, setCurrentDiaryItem] = useState()

  //mount된 이후, 일기 데이터를 통해서 진행할 수 있음
  useEffect(()=>{ //getCurrentDiary가 하던기능 그대로 넣어줌
    const currentDiaryItem = data.find((item) => 
      String(item.id) === String(params.id))
      
      if (!currentDiaryItem) {
        window.alert('존재하지 않는 일기입니다.')
        // 홈페이지로 보내달라고 했는데 그대로 수정에만 진행됨
        nav('/', {replace : true})
      }
      setCurrentDiaryItem(currentDiaryItem) //값이 있으면 그냥 이 값 자체를 반환해주면 됨
      //이 값을 보관할 곳이 없기 떄문에 저장할 state 만들어줌
  }, [params.id, data])

  const onClickDelete = () => {
    if (
      window.confirm("일기를 정말 삭제할까요? 다시 복구되지 않아요")
    ) { //yes면 일기 삭제
      onDelete(params.id) //params에 있는 아이디로 전달
      nav('/', {replace : true})
    }
  }

  //여기서 동일하게 New에서 한 것처럼 진행
  const onSubmit = (input) => {
    if (window.confirm("일기를 정말 수정할까요?")) {
      onUpdate(params.id, input.createdDate.getTime(), input.emotionId, input.content)
      //newPage처럼 => 지금은 이제 onUPdate를 사용할 것
      nav('/', {replace:true})
    }
  }


  // // find method QQ?
  // const getCurrentDiaryItem = () => {

  // }

  // const currentDiaryItem = getCurrentDiaryItem() //현재 일기 아이디 아이템
  //바로 호출됨 => 어떠한 것도 mount 되지 않은 상태에서 호출되기 때문임
  //그러면 useEffect를 하라는 것
  // broweserRouter가 rendering되어야 nav에서 진행할 수 있음
  console.log(currentDiaryItem)

  return (
    <div>
      <Header 
        title={'일기 수정하기'}
        rightChild={<Button 
          text={"삭제하기"}
          onClick={onClickDelete}
          type={"NEGATIVE"}/>}
        leftChild={<Button 
          onClick={() => (nav(-1))}
          text={"< 뒤로가기"}/>}
      />
      {/* currentDiaryItem이 있을 때만 Editor를 렌더링 */}
      {currentDiaryItem && (
        <Editor 
          onSubmit={onSubmit}
          initData={{
            ...currentDiaryItem,
            createdDate: new Date(Number(currentDiaryItem.createdDate)) 
          }}
        />
      )}
    </div>
  )
}

export default Edit