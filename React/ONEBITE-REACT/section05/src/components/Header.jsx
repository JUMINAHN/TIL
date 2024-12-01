// 우리만의 컴포넌트
// 컴포넌트는 대문자로 시작해야함 == 첫글자
// 모듈화를 위해 일반적으로 모듈끼리 나눠서 진행함
function Header() { //함수로 선언 == 함수 컴포넌트 : 일반적 대중적
  return ( //html tag return 
    <header>
      <h1>header</h1> 
      {/* 화면 어디에도 랜더링되지 않는 것을 볼 수 있음 */}
    </header>
  )
}

export default Header; //ES module system안에서 이게 기본적으로 내보내짐