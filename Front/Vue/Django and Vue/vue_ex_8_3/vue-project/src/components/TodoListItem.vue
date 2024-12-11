<template>
  <div>
    <p>{{ todo.work}}</p>
    <p>{{ todo.content}}</p>
    <p>{{ todo.is_completed}}</p>
    <p>{{ todo.created_at}}</p>
    <!--pk?-->
    <!--상세보기 페이지 작성-->
    <RouterLink :to="{name : 'DetailView', params: {id : todo.id}}">상세보기</RouterLink> <!--PK값을 같이 전달한다.-->
  </div>
  <hr/>
</template>

<script setup>
import { defineProps } from 'vue'
import { RouterLink, useRouter } from 'vue-router'

defineProps({
  todo: Object
})
</script>
