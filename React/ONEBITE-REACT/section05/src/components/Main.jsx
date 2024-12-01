import './Main.css' //그냥 파일의 경로만

const Main = () => {
  //JSX 주의 사항
  //1. 중괄호 내부에는 JS 표현식만 넣을 수 있다.
  //2. 숫자, 문자열, 배열 값만 랜더링 된다.
  //3. 모든 태그는 닫혀있어야 한다.
  //4. 최상위 태그는 반드시 하나여야 한다. == 없다면 빈태그로 
  const user = {
    name :  "이정한",
    isLogin : true,
  }

  //1. 직접 스타일 설정 
  if (user.isLogin) {
    // return <div style={{ 
    //   // 직접 style은 규칙이 망가질수도
    //   ///객체 전달
    //   backgroundColor:"red", //css처럼 쓰면 안됨
    //   borderBottom : "5px solid blue"
    // }}>로그아웃</div>
    //JS + Html을 같이 쓰고 있기 떄문에 clasSName을 사용
    return <div className='logout'>로그아웃</div>
  } else {
    return <div>로그인</div>
  }


  return ( //여기서 바로 {}? => 해당 태그 구조
    <>
    {/* {user.isLogin ? (<div>로그아웃</div>) : (<div>로그인</div>) } */}
    </>
  )
}

export default Main