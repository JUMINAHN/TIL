<template>
  <div>
    <!-- <h1>일단 하위 </h1> -->
    <h3> {{index}}번 게시글</h3> <!--게시글 번호가 왜 안나옴?-->
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <hr>
  </div>
</template>

<script setup>
  defineProps({
    article: Object,
    index : Number
  })
</script>

<style scoped>

</style>