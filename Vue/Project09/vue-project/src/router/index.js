import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LaterView from '@/views/LaterView.vue'
import SearchView from '@/views/SearchView.vue'
import DetailVideoView from '@/views/DetailVideoView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
    {
      path: '/later',
      name: 'later',
      component: LaterView,
    },
    {
      path: '/:data?', //detailview
      name: 'detail',
      component: DetailVideoView,
    },
  ],
})

export default router
