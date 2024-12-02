//refactor

const Controller = ({onClickButton}) => {
  const btns = [//여러개의 버튼 필요
    //value에 쓰일 값, text로 쓰일 값
    {value : -100, text : "-100"},
    {value : -10, text : "-10"},
    {value : -1, text : "-1"},
    {value : 1, text : "1"},
    {value : 10, text : "10"},
    {value : 100, text : "100"}
  ]

  //버튼 자체가 6개로 만들어져야 함
  //바로 btns를 사용할 수 없음 => 왜냐하면 jsx관련 내용
  return(
    <div>
      {/* QQ.여기서 왜 map에 {}이것도 아니고 ({}) 이것도 아니고 ()로 만들어지나요? 각 속성에 접근해야해서 각 객체 하나로 만들기 위함인지 이 부분이 헷갈립니다.. 
      언제 ()만쓰고, {}만쓰고, ({})로쓰는지 헷갈리빈다*/}
      {btns.map((btn) => ( //btn 한개씩 돌아야하기 때문에
        <button 
        // QQ. 여기서 왜 key값을 설정하는지 모르겠습니다.
        key={btn.value}
        //value값으로 전단될 친구 onClickButton으로
        onClick={()=> {
          onClickButton(btn.value)
        }}>
          {btn.text}
        </button>
      ))}
    </div>
  )
}

export default Controller