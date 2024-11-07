<template>
  <div>
    <ParentPage />
  </div>
</template>

<script setup>
  import ParentPage from '@/components/ParentPage.vue';
</script>



<style scoped> /*원하는 것 처럼 전체가 적용되었지만, 의도치 않은 더 외부의 값까지 적용됨 */
  div {
  border: 1px solid grey;
  padding: 10px;
}
</style>