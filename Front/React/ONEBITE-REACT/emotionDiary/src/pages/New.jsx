import Button from "../components/Button"
import Header from "../components/Header"
import Editor from './../components/Editor';
import { replace, useNavigate } from 'react-router-dom';
import { DiaryStateContext, DiaryDispatchContext} from './../App';
import { useContext, useEffect } from 'react';
import usePageTitle from "../hooks/usePageTitle";


const New = () => {
  //랜더링되었을떄 title이 => 그것을 바꾸는 것 index.html
  // useEffect(()=>{
  //   //title 추출
  //   //반응형 title ==> $로 : DOm요소 저장
  //   const $title = document.getElementsByTagName("title") //TagName == title이라고 가지는 모든 태그 => 지금 head의 감정일기장
  //   $title.innerText = "새 일기 쓰기"
  // }, [])
  usePageTitle("새 일기 쓰기")

  const nav = useNavigate()
  const {onCreate} = useContext(DiaryDispatchContext) 
  
  const onSubmit = (input) => {
    onCreate((input.createdDate).getTime(), input.emotionId, input.content)
    nav("/", {replace:true})
  }
  //사용할 수 있도록 받았고,
  return (
    <div>
      <Header text={"새 일기 쓰기"}
      leftChild={<Button text={"< 뒤로가기"}
      onClick={() => nav(-1)}/>}/>
      <Editor 
      onSubmit={onSubmit}/>
    </div>
  )
}

export default New