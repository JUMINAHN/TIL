import emotion1 from '../assets/emotion1.png'
import emotion2 from '../assets/emotion2.png'
import emotion3 from '../assets/emotion3.png'
import emotion4 from '../assets/emotion4.png'
import emotion5 from '../assets/emotion5.png'


//강의 내용
export function getEmotionImage (emotionId) {//emotion 관련 id를 받아와서 필터링
  switch (emotionId) {
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


//이게 배열이 아닌데? 
//근데 생각해보면 emotion을 배열로 만들어줘야 함
//어떠한 emotionName, emotionId
// const emotions = [
//   {
//     id : 1,
//     emotionId : emotion1,
//     emotionName : '완전 좋음'
//   },
//   {
//     id : 2,
//     emotionId : emotion2,
//     emotionName : '좋음'
//   },
//   {
//     id : 3,
//     emotionId : emotion3,
//     emotionName : '그럭 저럭'
//   },
//   {
//     id : 4,
//     emotionId : emotion4,
//     emotionName : '나쁨'
//   },
//   {
//     id : 5,
//     emotionId : emotion5,
//     emotionName : '최악'
//   },
// ]

// export const getEmotion = (id) => {
//   console.log('받아온 emotionId값', id)
//   //특정 emotion번호가 들어오면 그걸 가져오게 하는 것
//   //거기에 맞게 return? => 그니까 1이 들어오면 1에 매칭 시켜줘야 함
//   //지금 여기에 맞게 1이면 => emotion1을 반환해줘야함
//   //그럼 일단 내생각에 filter로 일치된 내용이나 find로 반호나해줘야하는데 => 거기서 감정을 맞게 찾는 것
//   const emotion = emotions.find((item) => String(id) === String(item.id)) //id를 받아와야함
//   //찾은 emotion => 반환
//   console.log(emotion, '내부에서 emotion 값 추출')
//   return emotion //emotion 객체 전달
// }

