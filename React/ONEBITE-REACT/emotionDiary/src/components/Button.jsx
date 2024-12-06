import './Button.css'

//button도 타입이 있어야 함
//css마다 변경 되기도 하고, title도 가지기도 하고, text도 가지기도 하고
//각각 여기에 맞는 함수
const Button = ({text, type, onClick}) => {
  return (
    // 어떠한 타입인지에 따라서 클래스 네임 변경
    // 여기 확인 필요
    // <div>
    // 단순 리턴문은 가능
    <button onClick={onClick}
    className={`Button Button_${type}`}>{text}</button>
    // </div>
  
  )
}

export default Button