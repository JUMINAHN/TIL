<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="createArticles">
      <div>
        <label for="title">제목</label>
        <input type="text" id="title" v-model="title">
      </div>

      <div>
        <label for="content">내용</label>
        <input type="text" id="content" v-model="content">
      </div>

      <!--이거 누르면 이동-->
      <input type="submit" value="create"> <!--button은 에러-->
    </form>
  </div>
</template>

<script setup>
  import { useArticleStore } from '@/stores/articles';
  import axios from 'axios'
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'  
  

  const title = ref('')
  const content = ref('')

  //생성하는 곳에서 createArticles를 사용할 것이니까
  const store = useArticleStore() //지금 뭐 딱히 사용할일은 없을 것 같긴함..
    //게시글 생성 요청 기능 작성
  const router = useRouter()

  //게시글 생성 => 해당 요소에서만 사용할거니까
  const createArticles = function() {
    axios({
      method : 'post', //링크는 똑같은덱 걍 포스트인것
      url : 'http://127.0.0.1:8000/api/v1/articles/',
      data : { //parameter값으로 입력받아서 넣기
        title : title.value, //title에 있는 value
        content : content.value
      }
    })
    .then((res) => {
      //생성하고 articlepage로 돌려줘야한다.
      console.log(res.data)
      router.push({name : 'home'}) //home으로!!
    })
    .catch((err) => {
      console.log(err)
    })
  }

</script>

<style lang="scss" scoped>

</style>