import { useSearchParams } from "react-router-dom"
import { getEmotionImage } from "../util/get-motion-image"
import Button from "../components/Button"
import Header from "../components/Header"
import DiaryList from "../components/DiaryList"
import { useContext } from "react"

//home에서도 사용가능한지 확인해볼까? == useState 호출이 안되는데

const Home = () => {
  //const {onCreate} = useContext(useStateContext)  
  return (
    // Header 컴포넌트 생성필요
    <div>
      <Header text={"2024년 12월"}/> 
      <DiaryList />
      {/* <div>
        <img src={getEmotionImage(1)} alt="soHappy" />
        <img src={getEmotionImage(2)} alt="happy" />
        <img src={getEmotionImage(3)} alt="notBad" />
        <img src={getEmotionImage(4)} alt="bad" />
        <img src={getEmotionImage(5)} alt="terrible" />
      </div> */}
    </div>
  )
}

export default Home