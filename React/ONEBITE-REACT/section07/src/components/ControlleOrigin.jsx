const Controller = ({onClickButton}) => {
  //여기서 button안에 value 발동
  return(
    <div>
      <button
      onClick={()=>{
        onClickButton(-1)
        //-1을 인수로 전달
      }}>-1</button>
      <button
      onClick={()=>{
        onClickButton(-10)
        //-1을 인수로 전달
      }}>-10</button>
      <button
      onClick={()=>{
        onClickButton(-100)
        //-1을 인수로 전달
      }}>-100</button>
      <button
      onClick={()=>{
        onClickButton(100)
        //-1을 인수로 전달
      }}>+100</button>
      <button
      onClick={()=>{
        onClickButton(10)
        //-1을 인수로 전달
      }}>+10</button>
      <button
      onClick={()=>{
        onClickButton(1)
        //-1을 인수로 전달
      }}>+1</button>
    </div>
  )
}

export default Controller