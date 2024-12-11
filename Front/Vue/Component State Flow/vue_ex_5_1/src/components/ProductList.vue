<template>
  <li>{{ myProp.name }} - {{ myProp.price }}원</li>

  <!-- <div>   
  </div> -->
</template>

<script setup>
  //받는다
  defineProps({
    //하나씩 받음 => product
    myProp : Object //object형태로 
  })
</script>

<style scoped>

</style>