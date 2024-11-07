<template> <!-- 컴포넌트의 최상위 요소는 항상 한개로만 ! -->
  <div>
    <h2>가수 목록</h2>
    <SingerDetail />
  </div>
</template>

<script setup>
  import SingerDetail from '@/components/singers/SingerDetail.vue';
</script>

<style scoped>
  /*이렇게면 list랑 detail모두* */
  /* div {
    border: 1px solid black;
  } */
</style>