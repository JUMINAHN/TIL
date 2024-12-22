// Skill.jsx
import { useState } from 'react'
import { skills } from '../utils/get-skill-data'
import './Skill.css'
import SkillItem from './../components/SkillItem';

const Skill = () => {
  const frame = skills.slice(0,3)
  const design = skills.slice(3,6)
  const tool = skills.slice(6,9)


return (
  <div className='Skill'>
    <section className='frame_section'>
      {
        frame.map((item) => 
          <div className="frame_wrap"
          key={item.title}>
            <SkillItem 
            {...item}/>
          </div>
        )
      }
    </section>
    <section className='design_section'>
      {
        design.map((item) => 
          <div className="design_wrap"
          key={item.title}>
            <SkillItem 
            {...item}/>
          </div>
        )
      }
    </section>
    <section className='tool_section'>
      {
        tool.map((item) => 
          <div className="tool_wrap"
          key={item.title}>
            <SkillItem 
            {...item}/>
          </div>
        )
      }
    </section>
  </div>
)
}

export default Skill
