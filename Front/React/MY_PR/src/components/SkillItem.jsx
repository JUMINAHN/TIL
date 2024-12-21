// SkillItem.jsx
import { useState } from 'react'
import './SkillItem.css'

const SkillItem = ({ title, description, img, style }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <div className="floating-item" style={style} onClick={() => setIsOpen(true)}>
        <img src={img} alt={title} />
      </div>

      {isOpen && (
        <div className="modal-overlay" onClick={() => setIsOpen(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <img src={img} alt={title} />
            <h3>{title}</h3>
            <p>{description}</p>
            <button className="close-btn" onClick={() => setIsOpen(false)}>
              닫기
            </button>
          </div>
        </div>
      )}
    </>
  )
}

export default SkillItem
