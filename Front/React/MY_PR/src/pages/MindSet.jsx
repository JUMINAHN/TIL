import { useEffect, useState } from 'react'
import './MindSet.css'

const MindSet = () => {
  const [resultWater, setResultWater] = useState(false)
  // drag 
  const [dragOn, setDragOn] = useState(false) //현재 드래그 상태
  const [dragOut, setDragOut] = useState(false) //드래그 놓기

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


  // drag, dragOver
  //eventHandler => e.target으로
  const onDragWater = (e) => {
    setDragOn(true)
  }

  
  const onDragOverWater = (e) => {
    e.preventDefault() //기본 동작 방지
    // console.log(e)
    setDragOn(false)
    setDragOut(true)
    setResultWater(true)

    setTimeout(()=>{
      setDragOut(false)
      setResultWater(false)
    }, 2000)
  }


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
      <section className='enhance_section'>
        <div className={`enhance_zone enhance_zone_${resultWater}`}>
          <div className='enhance_box' onDragOver={onDragOverWater}>
            {
              resultWater ? <p>🍎</p> : <p>🌱</p>
            }
            {resultWater ? 
            <p>오늘도 성장했어요</p> : <p>새싹에 물을 주세요</p>}
          </div>
        </div>
        <div className='enhance_heart'>
          <h1 onDrag={onDragWater}
          draggable="true"
          // 드래그가 가능하도록 설정해야함
          >💧</h1>
        </div>
      </section>
      <div className='result'> 
        {resultWater ? '오늘도 한 단계 성장했습니다.' : ''}
      </div>
    </div>
  )
}

export default MindSet