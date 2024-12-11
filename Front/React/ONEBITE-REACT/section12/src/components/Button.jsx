import './Button.css'

//부모 컴포넌트 props에 따라서 다 다르게 동작하도록 만들어주기
// type은 각 버튼마다 색깔이 다르니까 => text 글자, type 색깔, onClick 어디에 onCLick 이벤트를 걸건지
// type별로 다르게 => butoonTag의 className 'Button'에서 변경
const Button = ({text, type, onClick}) => {
  return (
    <button onClick={onClick}
    className={`Button Button_${type}`}>{text}</button>
    // Button에 타입 명시
  )
}

export default Button