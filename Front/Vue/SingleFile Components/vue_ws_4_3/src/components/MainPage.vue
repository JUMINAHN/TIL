<template>
  <div>
    <h1>가수 정보 페이지에 오신 것을 환영합니다.</h1>
    <p>여러 분이 좋아하는 가수와 아티스트에 대한 정보를 탐색해보세요.</p>
    <img src="/src/assets/microphone.jpg" alt="img">
    <SingerList />
  </div>
</template>

<script setup>
import SingerList from '@/components/SingerList.vue';

</script>

<style scoped>
  div {
    /* display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center; */
    text-align: center;
    /* border: 1px solid black; */
  }
  img {
    width: 200px;
  }

</style>