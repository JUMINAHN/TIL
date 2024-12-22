import { useState } from 'react'
import closeBag from '../assets/mainImg/001.png'
import openBag from '../assets/mainImg/002.png'
import Info from '../components/Info'
import './Home.css'

const Home = () => {
  const [bagStatus, setBagStatus] = useState(closeBag) 
  // mouse가 들어가고 말고의 상태에 따른 => 동작 변화
  const [mouseEnter, setMouseEnter] = useState(false)

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
      <section className="img_section"
        onMouseEnter={() => setMouseEnter(true)}
        onMouseLeave={() => setMouseEnter(false)}>
        <img src={bagStatus} alt="close_bag" 
        onClick={onClickBagChange}/>
        <div className='img_info_section'>
          {bagStatus === openBag ? <Info /> : ''}
        </div>
      </section>
      <section className='sub_section'> 
        { 
          (bagStatus === openBag)
          && mouseEnter === true ? <p>마우스를 가방 밖으로 옮겨 보세요!</p> : <p>마우스를 가방 안으로 옮겨 클릭해 보세요!</p>
        }
      </section>
    </div>
  )
}

export default Home 