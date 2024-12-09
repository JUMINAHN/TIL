import Button from "../components/Button"
import Header from "../components/Header"
import Editor from './../components/Editor';
import { replace, useNavigate } from 'react-router-dom';
import { DiaryStateContext, DiaryDispatchContext} from './../App';
import { useContext } from 'react';

const New = () => {
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