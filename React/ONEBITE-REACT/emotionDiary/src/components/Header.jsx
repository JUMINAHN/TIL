import Button from './Button'
import './Header.css'


// Q. props의 키 값을 기준으로 받아오는 것인지?
const Header = ({text, leftChild, rightChild}) => { 

  return (
    <div className='Header'> 
      <div className="header_left">
        {leftChild}
      </div>
      <div className="header_title">{text}</div>
      <div className="header_right">
        {rightChild}
      </div>
    </div>
  )
}

export default Header