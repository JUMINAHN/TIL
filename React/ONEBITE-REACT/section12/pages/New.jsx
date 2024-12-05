import { useNavigate } from 'react-router-dom';
import Button from '../src/components/Button';
import Editor from '../src/components/Editor';
import Header from './../src/components/Header';
import { useContext, useEffect } from 'react';
import { DiaryStateContext, DiaryDispatchContext } from './../src/App';
import usePageTitle from '../src/hooks/usePageTitle';

const New = () => {
  const nav = useNavigate()
  const {onCreate} = useContext(DiaryDispatchContext)
  usePageTitle("새 일기 쓰기")
  // useEffect(()=> { //신기
  //   const $title = document.getElementsByTagName("title")[0]
  //   //페이지 타이틀 태그
  //   //dom요소 저장하는 요소 만들떄 $로 만든다
  //   $title.innerText = "새 일기 쓰기"
  // }, [])

  const onSubmit = (input) => {
    onCreate(input.createdDate.getTime(), input.emotionId, input.content)
    nav('/', {replace:true}) //뒤로가기 방지
  }

  return (
    <div>
      <Header 
      title={"새 일기 쓰기"}
      leftChild={<Button
      onClick={() => nav(-1)} 
      text={"< 뒤로 가기"}/>}/>
      <Editor onSubmit={onSubmit}/>
    </div>
  )
}

export default New