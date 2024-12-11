<template>
<main>
  <h1>할 일 목록</h1> <!--todoList에 todos props를 전달한다. -->
  <!-- <p>{{ store.todos }}</p>  -->
  <TodoList 
  :todos="store.todos"/> <!--list자체를 전달함-->
  <!-- <TodoList 
    v-for="todos in store.todos"
    :key ="todos.id"
    :todos="todos"
  /> props로 전달 -->
</main>
</template>

<script setup>
import { onMounted } from 'vue'
import {useTodoStore} from "@/stores/todoStore.js";
import TodoList from '@/components/TodoList.vue';

const store = useTodoStore()
onMounted(() => {
  store.getTodos() //이거 응답값
})
console.log(store.todos, 'todoView에서 확인')
</script>

<style>

</style>
