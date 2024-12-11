<template>
  <div>
    <button @click="moveLink">게시글 생성</button> <!--link-->
    <!--이거 linkto로 ?-->
    <ArticleListItem
    v-for="(article, index) in store.articles"
    :key="article.title"
    :article="article"
    :index="index + 1"
    />
  </div>
</template>

<script setup>
  
  import { onMounted, ref } from 'vue'
  import { useArticleStore } from '@/stores/articles'
  import ArticleListItem from '@/components/ArticleListItem.vue'
  import { useRouter } from 'vue-router'
  
const router = useRouter() //router로 위치 옮기기 push
const store = useArticleStore()
//articles의 데이터가 필요한 것
//그냥 store에서 받아와서 그냥 뿌려줌

const moveLink = function(){
  router.push({path : 'create' }) //create가 있는 곳으로 이동 
}


onMounted(() => { //게시글 정보 자체를 랜더링 해야한다. 
  store.getArticles() //정보를 받아서 하위 컴포넌트에 내려줘야 한다. => store에서 데이터 저장 진행했음 => 데이터를 받아올 것
  //여기서 뭐 따로 받진 않음 => no return
})

const data = store.articles
console.log(data, '확인') //빈배열 => 마운트 받고 진행되니까 안됨
</script>

<style scoped>

</style>