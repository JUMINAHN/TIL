<template> <!--detail component 만들어지기 전에 1번 게시글 줘! : mainpage랑 동일한 상황 : 장고에게 미리 요청받아서 채운 것처럼 -->
<!--화면이 그려지기 전에 응답받고 미리세팅-->
  <div>
    <h1>DETAIL</h1>
    <div v-if="article"> <!--값이 있을때 보여주겠다 : v-if dirretive -->
      <div>게시글 번호 : {{ article.id }}</div>
      <div>게시글 제목 : {{ article.title }}</div>
      <div>게시글 내용 : {{ article.content }}</div>
      <div>게시글 작성일 : {{ article.created_at }}</div>
      <div>게시글 수정일 : {{ article.updated_at }}</div>
    </div>
  </div>
</template>

<script setup>
  import { useCounterStore } from '@/stores/counter'
  import axios from 'axios' //store에서 보내지 않음 => why? : detail에서 rendering될 때 보내면 되니까
  import { onMounted, ref } from 'vue'
  import { useRoute } from 'vue-router' //router는 push 메서드 가진 객체
  
  const store = useCounterStore()
  const route = useRoute()
  const article = ref(null) //반응형 변수를 null로 설정 -> onmounted가 실행되면 => 채워준다 => dom은 화면에 채울 수 있다. => onMounted로 안하면 null이 채워지기 전에 화면에 그려보인다
  //detail 빈 페이지가 나올 수 있음 => 이걸 방지하기 위해서
  //Uncaught (in promise) TypeError: Cannot read properties of null (reading 'id') => 화면에 그릴려고 했는데 응답 오는 사이에 그림을 그려버린 것 => 아직 여전히 null이라는 것


  //onmounted의 역할 => detail view가 마운트되기전에 drf로 단일 게시글 조회를 요청 후 응답 데이터를 저장함
  onMounted(() => { //연결되고 돔에 연결되는게 맞다!
    axios({
      method : 'get',
      url : `${store.API_URL}/api/v1/articles/${route.params.id}` //라우터의 params => 그 정보에 article.id가 들어간다.
      //params에 id라는 객체가 들어가 있다. => route의 params의 id값
      // url : `${store.API_URL}/api/v1/article/${현재 디테일 게시글의 아이디}` //api의 url store
    })
    .then((res) => {
      console.log(res.data) //1번 객체를 넘겨주고 => 활용할 수 있음 => 위에서 출력하면 된다.
      //어딘가에 저장을 해야함
      article.value = res.data //null값을 채워준다.
    })
    .catch((err) => {
      console.log(err, '!')
    })
  })

</script>

<style>

</style>
