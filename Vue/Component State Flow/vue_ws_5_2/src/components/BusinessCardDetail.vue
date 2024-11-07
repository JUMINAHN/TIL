
<template>
  <div>
    <h3> 이름 : {{ myProp.name }}</h3>
    <p> 직함 : {{ myProp.title }}</p>
  </div>
</template>

<script setup>
  defineProps({
    myProp : Object //object로 받음
  })
</script>

<style scoped>
  div {
    display: inline-block; /*div 나란히 정렬 가능!*/
    border: 1px solid gray;
    background-color: rgb(236, 233, 233);
    width: 40%;
    height:fit-content;
    margin: 30px;
  }
</style>
