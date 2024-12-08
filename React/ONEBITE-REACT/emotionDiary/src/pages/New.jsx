import Button from "../components/Button"
import Header from "../components/Header"
import Editor from './../components/Editor';

const New = () => {
  return (
    <div>
      <Header text={"새 일기 쓰기"}
      leftChild={<Button text={"< 뒤로가기"}/>}/>
      <Editor />
    </div>
  )
}

export default New