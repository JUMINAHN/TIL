// SkillItem.jsx
import { useState } from 'react'
import './SkillItem.css'

const SkillItem = ({ title, description, img}) => {
  return (
    <div className='SkillItem'>
      <section className='img_section'>
        <img src={img} alt="" />
      </section>
      {/* <section className='info_section'>
        <p>{title}</p>
        <p>{description}</p>
      </section> */}
    </div>
  )
}

export default SkillItem
