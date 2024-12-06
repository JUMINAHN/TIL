import { useSearchParams } from "react-router-dom"
import { getEmotionImage } from "../util/get-motion-image"
//asset에서 쓸거는 import하기
// import emotion1 from '../assets/emotion1.png'
// import emotion2 from '../assets/emotion2.png'
// import emotion3 from '../assets/emotion3.png'
// import emotion4 from '../assets/emotion4.png'
// import emotion5 from '../assets/emotion5.png'
// 이미지 파일을 계속 사용할 것인데 따로 분리한다. == util로!!!!



//emotion 관련 image 불러와야 함
//파라미터 외
const Home = () => {
  //params로 받을 친구
  const [searchParams, setSearchParams] = useSearchParams()
  const id = searchParams.get('value')
  console.log(id, '파라미터 아이디 : qeuryString')
  console.log('getEmotion') //값이 1만 나옴
  
  //특정 key를 가져오는 메서드
  // setSearch.get('value')
  // console.log(search, 'set으로 받아온 이후')

  //일단은 이미지 최적화 가능 여부 확인 => public과 assets 유무인데
  //assets에 사용됨 => build로 확인해보기
  return (
    <div>
      <div>
        <h1>assets으로</h1>
        <img src={getEmotionImage(1)} alt="" />
        <img src={getEmotionImage(2)} alt="" />
        <img src={getEmotionImage(3)} alt="" />
        <img src={getEmotionImage(4)} alt="" />
        <img src={getEmotionImage(5)} alt="" />
        {/* <img src={emotion2} alt="" />
        <img src={emotion3} alt="" />
        <img src={emotion4} alt="" />
        <img src={emotion5} alt="" /> */}
      </div>
      <br />

      {/* 현재 npm run preview 환경에서 테스트 중인데 public 파일은 뜨지도 않음 */}
      {/* <div>
        <h1>public으로</h1>
        <img src="/public/emotion1.png" alt="" />
        <img src="/public/emotion2.png" alt="" />
        <img src="/public/emotion3.png" alt="" />
        <img src="/public/emotion4.png" alt="" />
        <img src="/public/emotion5.png" alt="" />
      </div> */}

    </div>
  )
}

export default Home