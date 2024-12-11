<template>
  <div>
    
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articles'
const store = useArticleStore()

onMounted(() => {
  store.getArticles() //이때 axios가 정확하게 수행되는지 확인할 것
  //여기서 진행한다.

  // axios({
  //   method:'get', //받아오는거니까
  //   url: ''
  // })
  // .then()
  // .catch()
})
</script>

<style lang="scss" scoped>

</style>