// Skill.jsx
import { useState } from 'react'
import './Skill.css'
import SkillItem from './../components/SkillItem'
import { skills } from '../utils/get-skill-data'

const Skill = () => {
  const skillGroups = {
    framework: skills.slice(0, 3),
    design: skills.slice(3, 6),
    collab: skills.slice(6, 9)
  }

  return (
    <div className="skill-container">
      <div className="skill-sections">
        <div className="skill-section">
          <h2>Framework</h2>
          <div className="skill-box">
            {skillGroups.framework.map((skill, index) => (
              <SkillItem 
                key={skill.title} 
                {...skill}
                style={{
                  animationDelay: `${index * -3}s`,
                  left: `${20 + (index * 35)}%`,
                  top: `${30 + (Math.sin(index) * 15)}%`
                }}
              />
            ))}
          </div>
        </div>

        <div className="skill-section">
          <h2>Design Tools</h2>
          <div className="skill-box">
            {skillGroups.design.map((skill, index) => (
              <SkillItem 
                key={skill.title} 
                {...skill}
                style={{
                  animationDelay: `${index * -3}s`,
                  left: `${20 + (index * 35)}%`,
                  top: `${30 + (Math.sin(index) * 15)}%`
                }}
              />
            ))}
          </div>
        </div>

        <div className="skill-section">
          <h2>Collaboration Tools</h2>
          <div className="skill-box">
            {skillGroups.collab.map((skill, index) => (
              <SkillItem 
                key={skill.title} 
                {...skill}
                style={{
                  animationDelay: `${index * -3}s`,
                  left: `${20 + (index * 35)}%`,
                  top: `${30 + (Math.sin(index) * 15)}%`
                }}
              />
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}

export default Skill
