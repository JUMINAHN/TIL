import Button from "../components/Button"
import Header from "../components/Header"
import Editor from './../components/Editor';
import { replace, useNavigate } from 'react-router-dom';
import { DiaryStateContext, DiaryDispatchContext} from './../App';
import { useContext } from 'react';

// Newpage에서 일단 dispatch랑 state를 받아야 함 => 왜?
// dispatch에 있는 create 활용해야 함
// data?는 일단.. keep

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