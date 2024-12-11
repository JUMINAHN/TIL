import { createRouter, createWebHistory } from 'vue-router'
import TodoView from '@/views/TodoView.vue'
import DetailView from '@/views/DetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'TodoView',
      component: TodoView
    },
    { //variable routing과 비슷하지만 => `:`만 쓴다.
      path: '/todo/:id', //todo/id => id가 아마 number일 것 같은데
      name: 'DetailView',
      component: DetailView
    },
  ]
})

export default router
