import emotion1 from './../src/assets/emotion1.png'
import emotion2 from './../src/assets/emotion2.png'
import emotion3 from './../src/assets/emotion3.png'
import emotion4 from './../src/assets/emotion4.png'
import emotion5 from './../src/assets/emotion5.png'


//번호를 기준으로 반환하는 함수
export function getEmotionImage(emotionId) {
  switch(emotionId) {
    case 1:
      return emotion1
    case 2:
      return emotion2
    case 3:
      return emotion3
    case 4:
      return emotion4
    case 5:
      return emotion5         
    default:
      return null    
  }
}