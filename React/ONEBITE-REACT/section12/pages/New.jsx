import { useNavigate } from 'react-router-dom';
import Button from '../src/components/Button';
import Editor from '../src/components/Editor';
import Header from './../src/components/Header';
import { useContext } from 'react';
import { DiaryStateContext, DiaryDispatchContext } from './../src/App';


const New = () => {
  const nav = useNavigate()
  const {onCreate} = useContext(DiaryDispatchContext)

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