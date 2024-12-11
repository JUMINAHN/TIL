<template> <!--formTag-->
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <!--공백을 장고에게 보내면 안됨 : trim을 해준다. -->
      <div>
        <label for="title"> 제목 : </label> <!--id로 연결-->
        <input type="text" id="title" v-model.trim="title">
      </div>

      <div>
        <label for="content"> 내용 : </label>
        <textarea name="" id="content" cols="30" rows="10" v-model.trim="content"></textarea>
      </div>

      <input type="submit">
    </form>
  </div>
</template>

<script setup>
  import { useCounterStore } from '@/stores/counter'
  import axios from 'axios'
  import { ref } from 'vue'
  import { useRouter } from 'vue-router' //push,replace를 가진 친구  
  
  //실시간 저장 => 잘 담아서 어떠한 axios 요청에 보내줘야 함 => 실시간 == 양방향 바인드

  const title = ref('') //초기값 null => 빈문자열 차이 => 나중에 추가를 할 때 다름(null안됨)
  const content = ref('')
  const store = useCounterStore()
  const router = useRouter()

  //함수에 담아서 요청을 보낸다
  //drf로 게시글 생성 요청을 보내는 함수 --로직
  //submit이 발생했을 때 
  const createArticle = function() {
    axios({
      method:'post', //생성
      url : `${store.API_URL}/api/v1/articles/`,
      data : {
        title : title.value, //양방향바인딩으로 채워줄 것
        content : content.value //실시간으로 채워질 것 => v-model
      }
    })
    .then((res) => {
      console.log('작성 성공')
      router.push({name : 'ArticleView'}) //redirect시켜주자
    })
    .catch((err) => {
      console.log(err)
    })
  }

</script>

<style>

</style>
