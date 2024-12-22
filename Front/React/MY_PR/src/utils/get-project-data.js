// git도 동일?
import compare from '/src/assets/projectImg/compare.gif'
import main from '/src/assets/projectImg/main.gif'
import moveComponent from '/src/assets/projectImg/moveComponent.gif'
import recommend from '/src/assets/projectImg/recommend.gif'

export const projects = [
  {
    title : '초기 로딩 화면',
    gif : main,
    descriptions : '[ setTimeOut 기능을 통한 페이지네이션 기능 구현 및 데이터 onMounted ]'
  },
  {
    title : '반응형 모션 구현',
    gif : moveComponent,
    descriptions : '[ css & animation & keyframes를 활용한 반응형 애니메이션 구현 ]'
  },
  {
    title : '예적금 상품 비교',
    gif : compare,
    descriptions : '[ v-model로 사용자 입력 데이터 matching system 구현 ]'
  },
  {
    title : '맞춤형 예적금 상품 추천',
    gif : recommend,
    descriptions : '[ chart.js를 활용한, 사용자 맞춤형 상품 내역 가시화 ]' 
  },
]