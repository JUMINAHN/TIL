const NavbarComponent = ({ componentName, title }) => {
  return (
    <nav>
      <h1>{title}</h1>
      <p>{componentName} 컴포넌트입니다.</p>
      <ul>
        <li>홈</li>
        <li>소개</li>
        <li>서비스</li>
        <li>연락처</li>
      </ul>
    </nav>
  )
}

export default NavbarComponent