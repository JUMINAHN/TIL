import MainPage from '@/components/MainPage.vue'
import OtherView from '@/views/OtherView.vue'
import SomeView from '@/views/SomeView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import StudentViews from '@/views/StudentViews.vue'
import StudentDetailView from '@/views/StudentDetailView.vue'

  //studentViews에 .. => name을 기준으로 router ush 


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      //someView를 등록한다.
      path: '/', //첫 루트 페이지라서
      name: 'some',
      component: SomeView
    },
    {
      path: '/other',
      name : 'other',
      component : OtherView
    },
    {
      path:'/students',
      name : 'students',
      component : StudentViews
    },
    { //화면 상세 정보 페이지 화면 구성 작성
      path : '/students/:name', //여기 
      name : 'studentDetail',
      component : StudentDetailView,
      //중첩이 children
    }, 

  ],
})

export default router
