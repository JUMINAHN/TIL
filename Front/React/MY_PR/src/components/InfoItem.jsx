import { useState } from 'react'
import './InfoItem.css'
// card 컴포넌트 : 1차 목표 -> 방향키로 움직이는 것
// card 컴포넌트 : 2차 목표 -> 단순 line형태가 아닌 원형 형태로 
// card 컴포넌트 : 3차 목표 -> 지구본 처럼 돌릴 수 있는 것

const InfoItem = ({category, img, onClick}) => {
  // console.log(onClick)
  return (
    <div className="InfoItem"> 
      <div className="card_container"
      onClick={onClick}>
        <h2>{category}</h2>
        <h1>{img}</h1>
      </div>
    </div>
  )
}

export default InfoItem