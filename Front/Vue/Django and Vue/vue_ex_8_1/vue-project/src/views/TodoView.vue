<template>
<main>
  <h1>할 일 목록</h1>
  <!--정리말고 그냥 일단 뿌려준다-->
  <p>{{ store.todoData }}</p>

</main>
</template>

<script setup>
  import { useTodoStore } from '@/stores/todoStore'
  import { ref, onMounted } from 'vue' //값을 넣으니까 호출됨
    
  const store = useTodoStore()
  //onmount는 function이 아님
  onMounted(() => { // callback 함수
    store.getTodos() //todos를 가져오면 위에서 사용 가능 => data가져오기
  })

  //화면에 mount된다는게 -> onMounted 된 것을 의미
  //onmount하고, store에 있는 getTods를 호출

</script>

<style>

</style>
