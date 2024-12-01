// 부모가 자식에게 함수의 인수를 전달하듯이 원하는 값을 전달하는 것
// => props == properties


//매개 변수 자체를 받아옴
// const Button = (props) => { //자식에게 매개변수로 전달된다.
//   console.log(props) //자체를 출력 => 한개씩 받아옴 == property로 하나씩 전달
//   //여기서는 props로 받아오는 것?
//   //스타일 그자체를 받아오니까 style
//   //color가 없을때 자동으로 설정되도록 기본값을 설정한다.
//   return <button style={{color : props.color}}>{props.text} - {props.color.toUpperCase()}</button>
//   //props자체가 객체니까 그 안에있는 text를 사용하는 것
// }

//함수 선언부에서 바로 추출 가능 {text, color} = props를 안해도
//props는 객체 표기법으로 대부분들어오니까 구조분해할당으로 진행하면 됨


//이제 버튼 태그를 클맀했을 때 동작하도록 바꿔줄 것
const Button = ({text, color = 'blue', children}) => {
  console.log(text, color)
  const onClickButton = (e) => {
    console.log(e) //이벤트 객체 가능
    //syntehtic basic : 합성 이벤트 객체
    console.log(text, "click event 발동")
  }


  return (
    //버튼 자체에 onClick => function click 이벤트 발동
  <button  
    onClick={onClickButton} //click eventHandler
    //콜백함수를 전달하는 것 처럼 ()를 사용하지 않음

  // onClick={()=> {
  //   console.log('클릭 이벤트 발동', text)
  // }}
  style={{color : color}}>
    {text}-{color.toUpperCase()}
    {children}
    </button>
  )
}

//defaultProps는 종료 예정
// Button.defaultProps = { //defaul값 설정
//   color : "black"
// }


export default Button
//이거 export default안하면 전체나오는 것 아닌가? 굳이 해야하는 이유?