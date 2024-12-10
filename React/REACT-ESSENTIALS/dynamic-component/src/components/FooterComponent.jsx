// FooterComponent.jsx
const FooterComponent = ({ componentName, title }) => {
  return (
    <footer>
      <h3>{title}</h3>
      <p>{componentName} 영역입니다. © 2024 내 웹사이트. 모든 권리 보유.</p>
    </footer>
  )
}

export default FooterComponent
