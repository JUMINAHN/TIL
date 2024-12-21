import InfoItem from "./InfoItem"
import './Info.css'
import { useEffect, useRef, useState } from "react"
import { useNavigate } from "react-router-dom"

// 일단 초기 세팅값 설계
const dummy = [
  {id : 1, category : 'profile', img : "🙂"},
  {id : 2, category : 'skill', img : "📚"},
  {id : 3, category : 'project', img : "🛣️" },
  {id : 4, category : 'mindSet', img : "🩵"},
  {id : 5, category : 'profile', img : "🙂"},
  {id : 6, category : 'skill', img : "📚"},
  {id : 7, category : 'project', img : "🛣️" },
  {id : 8, category : 'mindSet', img : "🩵"},
  {id : 9, category : 'profile', img : "🙂"},
  {id : 10, category : 'skill', img : "📚"},
  {id : 11, category : 'project', img : "🛣️" },
  {id : 12, category : 'mindSet', img : "🩵"}
  // {id : 4, category : 'strong', img : "💪" },
  // {id : 5, category : 'weak', img : "🚨"},
]

const Info = () => {
  const nav = useNavigate()
  // 멈추는 것
  const [isPaused, setIsPaused] = useState(false) // 멈춤은 false
  const [position, setPosition] = useState(0) //일단 초기값 0으로 설정
  

  // select Category, modal => 어떤 카테고리가 선택되었는지 state로 담고, 관련 model open
  // const [modalOpen, setModalOpen] = useState(false)
  // const [selectedCategory, setSelectedCategory] = useState(null)
  

  const itemWidth = 202
  useEffect(()=>{
    if (isPaused) return
    //그게 아니라면?
    // interval 관련해서
    const interval = setInterval(()=>{
    //setPoisition 관련된 설정을 진행할 것
    setPosition(prev => { //이전 position의 값을 불러와서
      const next = prev + 1 //1px 증가
      // 마지막 전에 처음으로 돌아가도록
      if (next >= dummy.length * itemWidth) {
        return 0
      }
      return next
    })
    }, 50) //더 부드럽게 간격 줄임
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
    transition: position === 0 ? 'none' : 'transform 0.5s linear'
    }



    // // modal 관련
    // const handleItemClick = (category) => {
    //   setSelectedCategory(category)
    //   setModalOpen(true)
    // }
  
    // const closeModal = () => {
    //   setModalOpen(false)
    //   setSelectedCategory(null)
    // }


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

      {/* {modalOpen && (
        <div className="modal-overlay" onClick={closeModal}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <h2>{selectedCategory}</h2>
            <div className="modal-body">
              {selectedCategory === 'profile' && (
                <div>프로필 내용...</div>
              )}  
            </div>
            <button onClick={closeModal}>닫기</button>
          </div>
        </div>
      )} */}
    </div>
  );
};

export default Info