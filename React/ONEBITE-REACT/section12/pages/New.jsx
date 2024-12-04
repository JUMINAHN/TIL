import Button from '../src/components/Button';
import Editor from '../src/components/Editor';
import Header from './../src/components/Header';


const New = () => {
  return (
    <div>
      <Header 
      title={"새 일기 쓰기"}
      leftChild={<Button 
      text={"< 뒤로 가기"}/>}/>
      <Editor />
    </div>
  )
}

export default New