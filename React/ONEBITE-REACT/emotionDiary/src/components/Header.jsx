import Button from './Button'
import './Header.css'

const Header = ({text}) => { 
  //text받아와서 진행..
  //왼쪽으로 갈때 date 감소
  //오른쪽 갈떄 date 증가

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