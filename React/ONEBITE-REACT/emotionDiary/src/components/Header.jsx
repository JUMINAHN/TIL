import Button from './Button'
import './Header.css'

// Header에 들어갈 공통적인 요소들 생각
// text 들어가고 왼쪽 오른쪽에 데이터가 들어가는 것 동일
// 그리고 border-bottom 에 값이 들어가는 것 동일
// header에 들어갈 text
// button자체가 onCLick 이벤트를 못받을텐데 이건 어떻게? 
const Header = ({text}) => { //title과 leftChild, rightChild 하나씩 있음
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