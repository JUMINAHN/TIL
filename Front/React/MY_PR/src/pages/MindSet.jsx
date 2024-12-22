import { useEffect, useState } from 'react'
import './MindSet.css'

const MindSet = () => {
  // typing
  const [nowTyping, setNowTyping] = useState('') //일단 빈 값
  const fullText = 'SSAFY에서 주어진 6개월 간 매일 매일 `성장`하는 것이 목표입니다.'
  //한개씩 쳐질 것 => 그게 setNowTyping안에 들어가게 되는 것
  //초마다?
  useEffect(()=>{
    // clearinterval적용
    let nowidx = 0
    const interval = setInterval(()=>{
      if (nowidx === fullText.length) {
        clearInterval(interval)
        return //fullText를 만족시키면 useEffect 종료~
      }
      // 한개씩 증가시키기 => text 값을
      nowidx++ 
      setNowTyping(fullText.slice(0, nowidx))
    },100) //초 한번씩?
    return () => clearInterval(interval) //interval종료
  },[])
  // console.log(nowTyping, 'check')

  return (
    <div className="MindSet">
      {/* <div>
        <p>{nowTyping}</p>
      </div> */}
      <section className='title_section'>
        <h1>{nowTyping}</h1>
        {/* <h1>SSAFY에서 주어진 6개월 간 매일 매일 `성장`하는 것이 목표입니다.</h1> */}
      </section>
      <section className='content_section'>
        <p>따라서 성장에 진심인 서로 부족한 점을 보완할 수 있는 분들과 함께 하고 싶습니다.</p>
        <p>속도는 느리지만, 최선을 다하겠습니다.</p>
        <p>감사합니다.</p>
      </section>
    </div>
  )
}

export default MindSet