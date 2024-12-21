import { useState } from 'react'
import closeBag from '../assets/mainImg/001.png'
import openBag from '../assets/mainImg/002.png'
import Info from '../components/Info'
import './Home.css'

const Home = () => {
  const [bagStatus, setBagStatus] = useState(closeBag) 
  const onClickBagChange = () => {
    // 가방의 유무에 따라서 openBag, closeBag로 바꿔야 함
    setBagStatus(bagStatus === closeBag ? openBag : closeBag)
  }

  return (
    <div className='Home'>
      <section className="title_section">
        <h1>Zoom What's In Your Bag?</h1>
        {/* <p>▼</p> */}
        {/* <p>Click Bag</p> */}
      </section>
      <section className="img_section">
        <img src={bagStatus} alt="close_bag" 
        onClick={onClickBagChange}/>
        <div className='img_info_section'>
          {bagStatus === openBag ? <Info /> : ''}
        </div>
      </section>
    </div>
  )
}

export default Home 