import { replace, useNavigate, useParams } from "react-router-dom"
import Header from './../src/components/Header'
import Button from "../src/components/Button"
import Editor from "../src/components/Editor"
import { DiaryDispatchContext, DiaryStateContext } from "../src/App"
import { useContext, useEffect, useState } from "react"
import useDiary from "../src/hooks/useDiary"
import usePageTitle from "../src/hooks/usePageTitle"



const Edit = () => {
  const params = useParams()
  // console.log(params)
  //params를 기준으로 모든 데이터를 받아올 수 있어야 함
  //app의 data에서 우리가 원하는것만 받아오며 됨
  const nav = useNavigate()
  const {onDelete, onUpdate} = useContext(DiaryDispatchContext)
  // console.log(data)
  const currentDiaryItem = useDiary(params.id)
  usePageTitle(`${params.id}번 일기 수정`)

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