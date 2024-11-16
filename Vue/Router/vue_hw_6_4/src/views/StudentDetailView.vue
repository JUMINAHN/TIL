<template>
  <div>
    <h1>학생 상세 정보 페이지입니다.</h1>
    <!--학생 정보 보기-->
    <!-- <template v-for="" >
      <p>{{}} 학생 정보 보기</p> -->
      <p>이름 : {{ studentId }}</p>
  </div>
  </template>


<script setup>
  // 학생정보를 가져올 수 있었음 => $으로
  // route로 
  import {ref} from 'vue'
  import { useRoute } from 'vue-router'
  const route = useRoute() //route=> 이부분의 파라미터가 필요함
  const studentId = ref(route.params.name)
  console.log(studentId) //parameter로 불러오는 것 => 파라미터를 부르는 것

</script>

<style lang="scss" scoped>

</style>