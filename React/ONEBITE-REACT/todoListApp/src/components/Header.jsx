import './Header.css'

const Header = () => {
  return (
    <div className="Header">
      <h4>오늘은 📆</h4>
      <h1>{new Date().toDateString()}</h1>
    </div>
  )
}

export default Header 