import { useState } from 'react'
import closeBag from '../assets/mainImg/001.png'
import openBag from '../assets/mainImg/002.png'
import Info from '../components/Info'
import './Home.css'

const Home = () => {
  const [bagStatus, setBagStatus] = useState(closeBag) //일단 이것

  //일단 저장해야할 데이터
  // 1. profile : 인적사항(간단한 인적사항)
  // 2. project에 임하는 마인드
  // 3. 비전공자로써 가지고 있는 강점
  // 4. 반면의 약점
  // 5. 실제 프로젝트?
  // 6. 개발 경력 및 사용 언어



  

  const onClickBagChange = () => {
    // 가방의 유무에 따라서 openBag, closeBag로 바꿔야 함
    setBagStatus(bagStatus === closeBag ? openBag : closeBag)
  }

  return (
    <div className='Home'>
      <section className="title_section">
        <h1>Zoom What's In Your Bag?</h1>
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