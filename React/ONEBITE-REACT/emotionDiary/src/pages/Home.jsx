import { useSearchParams } from "react-router-dom"
import { getEmotionImage } from "../util/get-motion-image"
import Button from "../components/Button"
import Header from "../components/Header"


const Home = () => {
  return (
    // Header 컴포넌트 생성필요
    <div>
      <Header text={"2024년 12월"}/> 
      <Button 
      onClick={() => {console.log('버튼클릭')}}
      text={"<"}
      type={"DEFAULT"}/>
      <Button 
      text={">"}
      type={"NEGATIVE"}/>
      <Button 

      text={"새 일기쓰기"}
      type={"POSITIVE"}/>
      <div>
        <img src={getEmotionImage(1)} alt="soHappy" />
        <img src={getEmotionImage(2)} alt="happy" />
        <img src={getEmotionImage(3)} alt="notBad" />
        <img src={getEmotionImage(4)} alt="bad" />
        <img src={getEmotionImage(5)} alt="terrible" />
      </div>
    </div>
  )
}

export default Home