// Skill.jsx
import { useState } from 'react'
import { skills } from '../utils/get-skill-data'
import './Skill.css'
import skillbook from '../assets/skillImg/skillbook.jpg'
import SkillItem from './../components/SkillItem';

const Skill = () => {
  const perCardComponent = 3 // 3개씩 보여주기
  // const [displayPage, setDisplayPage] = useState([]) //배열리스트 보여줄 내용
  const [displayIdx, setDisplayIdx] = useState(0) //현재 idx

  const maxIdx = Math.max(Math.ceil(skills.length / perCardComponent) - 1)
  //displayIdx의 최대가 maxIdx

  const onClickLeft = () => {
    setDisplayIdx((prev) => prev === 0 ? maxIdx : prev - 1)
  }

  const onClickRight = () => {
    setDisplayIdx((next) => next === maxIdx ? 0 : next + 1)
  }

  //버튼 : 복습 성공
  const displayCard = skills.slice(displayIdx*perCardComponent, (displayIdx+1) * perCardComponent)
  // console.log(displayIdx) 
  // console.log(displayCard, 'check')

  // btn으로 좌/우 이동
return (
  <div className='Skill'>
    <section className='img_section'>
      <img src={skillbook} alt="" />
    </section>
    <section className='frame_section'>
      <button className='btn left_button' onClick={onClickLeft}>{"<"}</button>
      <div className='skill_wrap'>
        {
          displayCard.map((item) => 
            <div className="frame_wrap"
            key={item.title}>
              <SkillItem 
              {...item}/>
            </div>
          )
        }
      </div>
      <button className='btn right_button' onClick={onClickRight}>{">"}</button>
    </section>
  </div>
)
}

export default Skill
