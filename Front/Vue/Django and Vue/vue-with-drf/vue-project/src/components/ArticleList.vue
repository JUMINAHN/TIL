<template>
  <div>
    <h3>Article List</h3>
    <ArticleListItem
    v-for="article in store.articles" 
    :key="article.id"
    :article="article"/>
  </div>
</template>

<script setup> //articles를 가져와서 articlelist 아이템이 반복되어야 함 => 하위 컴포넌트 반복 => props로 내려줘야 함
  import ArticleListItem from '@/components/ArticleListItem.vue'
  import { useCounterStore } from '@/stores/counter'
  const store = useCounterStore()
  
</script>
