
<template>
  <div>
    <h3> 이름 : {{ myProp.name }}</h3>
    <p> 직함 : {{ myProp.title }}</p>
    <button @click="deleteCardFunc">명함 삭제</button>
  </div>
</template>

<script setup>
  defineProps({
    myProp : Object //object로 받음
  })
  const emit = defineEmits(['businessCard']) //businessCard를 인자로 넘긴다
  const deleteCardFunc = function() {//선언 defilEmits
    emit('businessCard')
  }
</script>

<style scoped>
  div {
    display: inline-block; /*div 나란히 정렬 가능!*/
    border: 1px solid gray;
    background-color: rgb(236, 233, 233);
    width: 40%;
    height:150px;
    margin: 30px;
  }
</style>
