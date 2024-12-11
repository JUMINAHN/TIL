<template>
  <!--router Link를 작성한다 : app.vue-->
  <h1>router 연습하기</h1>
  <RouterLink :to="{name : 'some'}">Some</RouterLink>
  |
  <RouterLink :to="{name : 'other'}">Other</RouterLink>

  <RouterView /> <!--왜 이게 some이 나올까 자동으로?-->
  <!--<RouterView /> --> <!--router View-->
</template>

<script setup>
  import MainPage from '@/components/MainPage.vue';
</script>


<style scoped>

</style>
