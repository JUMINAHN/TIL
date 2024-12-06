import Button from './Button'
import './Header.css'

const Header = ({text}) => { 
  return (
    <div className='Header'> 
      <div className="header_left">
        <Button text={"<"}/>
      </div>
      <div className="header_title">{text}</div>
      <div className="header_right">
        <Button text={">"}/>
      </div>
    </div>
  )
}

export default Header