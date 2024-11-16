<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MainPage from '@/components/MainPage.vue';
import { useRouter } from 'vue-router';

</script>

<template>
  <header>
    <div class="wrapper">
      <MainPage /> <!--router 연습하기 -->
      <nav>
        <RouterLink :to="{name : 'some'}">Some</RouterLink>
        |
        <RouterLink :to="{name : 'other'}">Other</RouterLink>
        |
        <RouterLink :to="{name : 'students'}">Students</RouterLink>

      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
