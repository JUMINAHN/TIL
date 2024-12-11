<template>
  <header>
    <nav>
      <!--잘 작동함-->
      <RouterLink :to="{name : 'TodoView'}">할 일 목록</RouterLink>
      <!--임의-->
      |
      <RouterLink :to="{name : 'TodoView'}">회원가입</RouterLink>
      |
      <RouterLink :to="{name : 'TodoView'}">로그인</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
</style>
