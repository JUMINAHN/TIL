<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <RouterLink 
    :to="{ name: 'DetailView' , params: {id : article.id}}">
    Detail</RouterLink> <!--이 부분이 디테일 뷰로 랜더링이 바뀌면 된다. -->
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

//detail은 동적파라미터가 있어야 함
  defineProps({
    article : Object
  })

</script>
