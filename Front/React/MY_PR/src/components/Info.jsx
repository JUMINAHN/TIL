import InfoItem from "./InfoItem"
import language from "../assets/infoImg/langugae.jpg"
import mind from "../assets/infoImg/mind.jpg"
import profile from "../assets/infoImg/profile.jpg"
import project from "../assets/infoImg/project.png"
import strong from "../assets/infoImg/strong.avif"
import weak from "../assets/infoImg/weak.jpg"
import './Info.css'
import { useEffect, useRef, useState } from "react"
import { useNavigate } from "react-router-dom"

// 일단 초기 세팅값 설계
const dummy = [
  {id : 1, category : 'profile', img : "🙂"},
  {id : 2, category : 'skill', img : "📚"},
  {id : 3, category : 'project', img : "🛣️" },
  {id : 4, category : 'strong', img : "💪" },
  {id : 5, category : 'weak', img : "🚨"},
  {id : 6, category : 'mindSet', img : "🩵"}
]

const Info = () => {
  const nav = useNavigate()
  // 멈추는 것
  const [isPaused, setIsPaused] = useState(false) // 멈춤은 false
  const [position, setPosition] = useState(0) //일단 초기값 0으로 설정
  const itemWidth = 150

  useEffect(()=>{
    if (isPaused) return
    //그게 아니라면?
    // interval 관련해서
    const interval = setInterval(()=>{
    //setPoisition 관련된 설정을 진행할 것
    setPosition(prev => { //이전 position의 값을 불러와서
      const next = prev + 1 //1px 증가
      // 마지막 전에 처음으로 돌아가도록
      if (next >= (dummy.length * itemWidth)) {
        return 0
      }
      return next
    })
    }, 30) //더 부드럽게 간격 줄임
    return () => clearInterval(interval)
  },[isPaused])

  //더블 버퍼링 방지를 위함 item component 생성
  const items = [...dummy, ...dummy, ...dummy].map((item, index) => ({
    //객체 자체를 만드니까 => id값 새로만들 것
    ...item,
    id : `${item.id}-${index}` //id와 idx구분
  }))

  // slideStyle == > 단순 객체
  const slideStyle = { //관련해서 style객체를 만들어야 함
    //position에 따라서 translate 변경
    transform : `translateX(-${position}px)`, //transform : 자체가 이동하는 것
    transition : position === 0 ? 'none' : 'transform 0.3s ease' //transform은 이동속성에만 적용됨
  }

  const onClick = (category) => {
    nav(`/${category}`)
  }

  return (
    <div className="Info">
      <div 
        className="info_wrap"
        style={slideStyle}
        onMouseEnter={() => setIsPaused(true)}
        onMouseLeave={() => setIsPaused(false)}>
        {items.map((item) => (
          <InfoItem
            onClick={() => onClick(item.category)}
            key={item.id}
            {...item}
          />
        ))}
      </div>
    </div>
  );
};

export default Info