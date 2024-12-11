<template>
  <div>
    <h1>할 일 상세</h1>
    <div v-if="todo">
      <p>할 일 번호 : {{ todo.id }}</p>
      <p>할 일 제목 : {{ todo.work }}</p>
      <p>할 일 내용 : {{ todo.content }}</p>
      <p>할 일 상태 : {{ todo.is_completed }}</p>
      <p>할 일 생성일 : {{ todo.created_at }}</p>
    </div>
  </div>
</template>

<script setup>
//mount될떄 api 서버로 요청을 보낸다.
//store 정보가져오기 => todoListitem에서 받아야 하는것 아닌가/
  
  import { useTodoStore } from '@/stores/todoStore'
  import axios from 'axios'
  import { onMounted, ref } from 'vue'
  import { useRoute } from 'vue-router' 
  //useRoute기능?
  const route = useRoute()
  const todo = ref(null)
  const store = useTodoStore()
  //axios 를 통해 화면에 나타낸다 => onMount
  //파라미터 데이터 상세페이지 => 
  onMounted(() => {
    axios({
    //data를 받아와야 함
    method : 'get',
    //여기 route.params.id 부분 이해
    url : `${store.BASE_URL}/api/v1/todos/${route.params.id}`
  })
  .then((res) => {
    console.log(res.data)
    todo.value = res.data
    //이 받은 데이터를 출력하기

  })
  .catch((err) => {
    console.log(err, 'why?')
    })
  })
  
</script>

<style scoped>

</style>