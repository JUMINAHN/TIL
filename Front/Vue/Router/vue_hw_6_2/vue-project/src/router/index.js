import MainPage from '@/components/MainPage.vue'
import OtherView from '@/views/OtherView.vue'
import SomeView from '@/views/SomeView.vue'
import { createRouter, createWebHistory } from 'vue-router'

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
    }

  ],
})

export default router
