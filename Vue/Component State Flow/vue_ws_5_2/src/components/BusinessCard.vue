<template>
  <div>
    <h2>보유 명함 목록</h2>
    <businessCardDetail 
      v-for="(businessCard, index) in businessCards"
      :key="businessCard.name"
      :my-prop = businessCard
    /> <!--businessCard를 my-prop로 바인딩하여 넘겨줌 >> myProp로 받으면 됨-->
    
  </div>  
</template>

<script setup>
  import {ref} from 'vue'
  import BusinessCardDetail from '@/components/businessCardDetail.vue';
  //이거 넘겨줄 것
  const businessCards = ref([ //businessCard 배열
    {name:'일론 머스크', title:'테슬라 테크노킹'},
    {name:'래리 엘리슨', title:'오라클 창업주'},
    {name:'빌 게이츠', title:'마이크로소프트 공동 창업주'},
    {name:'래리 페이지', title:'구글 공동 창업주'},
    {name:'세르게이 브린', title:'구글 공동 창업주'},
  ])
</script>

<style scoped>

</style>
