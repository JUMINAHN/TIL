<template> <!--todos : props를 가진다.-->
  <div>
    <!-- {{ todos }} -->
    <TodoListItem 
      v-for="todo in todos"
      :key="todo.id"
      :todo="todo"
    /> 
    <!-- props로 내려받은 할일 개체수만큼 반복 -->
  </div>
</template>

<script setup>
  import TodoListItem from '@/components/TodoListItem.vue'
  defineProps({
    todos : Array //Array로 받는 것을 볼 수 있음
  })
  //todos 잘받아왔는가?
  // console.log(todos, 'todolist')
  // console.log(todos[0], 'todolist 일부 추출')

</script>

<style lang="scss" scoped>

</style>