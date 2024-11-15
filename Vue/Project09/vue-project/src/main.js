import '@/assets/main.css'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css' //bootstrap에서 navbar 가능


// https://velog.io/@eldh1128/Vue-BootStrap-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

app.use(pinia)
app.use(router)

app.mount('#app')
