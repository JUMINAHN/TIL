import { useState } from 'react'
import closeBag from '../assets/mainImg/001.png'
import openBag from '../assets/mainImg/002.png'
import Info from './Info'
import './Home.css'

const Home = () => {
  const [bagStatus, setBagStatus] = useState(closeBag) //일단 이것

  const onClickBagChange = () => {
    // 가방의 유무에 따라서 openBag, closeBag로 바꿔야 함
    setBagStatus(bagStatus === closeBag ? openBag : closeBag)
  }

  return (
    <div className='Home'>
      <section className="title_section">
        <h1>What's In My Bag?</h1>
      </section>
      <section className="img_section">
        {/* 클릭하면 open_bag로 변경 */}
        <img src={bagStatus} alt="close_bag" 
        onClick={onClickBagChange}/>
        {/* open_bag일때만 요소가 튀어나오게 해야함 => if문 ? */}
        {/* img위에 position으로 다시 */}
        <div className='img_info_section'>
          <Info />
        </div>
      </section>
    </div>
  )
}

export default Home 