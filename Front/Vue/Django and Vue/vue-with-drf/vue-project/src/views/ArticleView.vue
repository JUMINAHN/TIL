<template>
  <!--여기가 랜더링 되어야, list에 대한 내용이 랜더링 되어야 함-->
  <!--화면이 랜더링될때 전체 게시글 조회를 해야 articleList가 늦지 않고 완성될 것-->
  <!--처음에 들어가기전, 즉 화면에 mount 되기 전에 호출이 되어서 미리 스토어 배열을 채우고 시작****-->
  <div>
    <h1>Article Pages</h1>
    <RouterLink :to="{ name : 'CreateView' }">Create</RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
  import ArticleList from '@/components/ArticleList.vue'
  import { useCounterStore } from '@/stores/counter'
  import { onMounted } from 'vue' //콜백함수를 받는다.
  import { RouterLink } from 'vue-router'
  
  const store = useCounterStore() 
  //라이프 사이클 훅 필요 => 항상 최신 요청을 위함

  //어디 함수의 인자로 넣어버리면 안됨 => 정해져있음, 컨트롤하는 애들 아님X
  //호출처럼 그냥 쓰면 된다
  onMounted(() => {
    //mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출 == 미리 해야함
    store.getArticles()//getArticles를 미리해야한다.
  })
</script>

<style>

</style>
