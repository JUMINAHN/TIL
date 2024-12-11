<template>  <!--todos : props를 가진다.-->
  <div>
    <p>{{ todo.work }}</p>
    <p>{{ todo.content }}</p>
    <p>{{ todo.is_completed }}</p>
    <p>{{ todo.created_at }}</p>
    <a href="#">상세보기</a>
    <!-- <p @click="clickDetail">상세보기</p> -->
    <hr>
  </div>
</template>

<script setup>
  import { useRouter } from 'vue-router';
  const router = useRouter()

  useRouter
  defineProps({
    todo : Object
  })
  
  const clickDetail = function() {
    //상세보기
    router.push({href : 'https://google.com/'})
  }

</script>

<style scoped>

</style>