const Controller = ({onClickCount}) => {
  //현재 button 여러개
  //state는 APP에서 총괄 => 따라서 state를 중앙에서 관리할 수 있도록 내부 선언
  const btns = [ //여러 btn 똑같은 내용을 반복적으로 활용
    {data : -1, text : '-1'},
    {data : -10, text : '-10'},
    {data : -100, text : '-100'},
    {data : 100, text : '+100'},
    {data : 10, text : '+10'},
    {data : 1, text : '+1'},
  ]

  //onClickCount를 받음
  //이걸 어떻게 활용할 것인가? => 그대로 사용 => 지금 onClickCount는 setValue 도와주는 애
  const onClickBtn = (data) => { //Btn을 누르면 onClickCount가 실행된다.
    // console.log(data, '디버깅용') //innerText는 값이 있음.. 
    //보면 value값이 없음
    //그런데 단순 onClickBtn()으로 제공하면 바로 호출이 되어버려서 
    
    //e.target => 동적일때 유용한데,, 
    onClickCount(data) //data를 전달해줌
    //결론적으로 이 친구가 SetCount에게 전달을 해주기 위한 친구
  }

  return (
    // 큰 묶음으로 하나 사용
    <div>
       {/*jsx연산자 임을 기억*/}
       {/* 새로운 요소로 하나씩 반환 => 그런데 지금은 button자체에 값을 넣는게 아니니까 forEach로 하면 안되나? */}
      {btns.map((btn) => ( //map을 객체로 반환할 필요가 없음 => 단순 데이터만 활용할 것
        <button
        // 그래서 지금 생각난 것은 onClick 눌리면 onClickBTN실행 == 오 이게 맞나..?
    
        onClick={() => onClickBtn(btn.data)}
        key={btn.data}> 
          {/* 실제 값을 넘겨주는 것 보류 */}
          {btn.text} 
          {/* btn의 텍스트만 활용 */}
        </button>
      ))}

    </div>
  )
}

export default Controller