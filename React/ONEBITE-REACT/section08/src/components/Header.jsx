import './Header.css';

const Header = () => {
  return (
    // 바로 CSS적용X
    <div className="Header">
      <h3>오늘은 📆</h3>
      {/* 해당 함수 newDate() == 데이트 객체 생성 => string으로? */}
      <h1>{new Date().toDateString()}</h1>
    </div>
  ) 
}

export default Header