<template>
  <nav>
    <NavVar/>
  </nav>
  <div class="body">
    <RouterLink :to="{name : 'home'}">◁ 뒤로 가기</RouterLink>
    <RouterView />
  </div>
</template>

<script setup>
  import NavVar from '@/components/NavVar.vue';
  import { RouterLink } from 'vue-router';




</script>



<style >
  .body {
    margin : 20px;
  }
</style>
