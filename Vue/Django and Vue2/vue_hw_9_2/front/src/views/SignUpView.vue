<template>
  <!--일단 형식만 만들고 추후 수정-->
  <div>
    <h1>회원 가입 페이지</h1>
    <form @submit.prevent="signUp">
      <div>
        <label for="username">username : </label>
        <input type="text" id="username" v-model.trim="username">
      </div>

      <div>
        <label for="password1">password: </label>
        <input type="text" id="password1" v-model.trim="password1">
      </div>

      <div>
        <label for="password2">password Confirmation : </label>
        <input type="text" id="password2" v-model.trim="password2">
      </div>

      <input type="submit" value="submit">
    </form>
  </div>
</template>

<script setup >
  import { ref } from 'vue';
  import { useArticleStore } from '@/stores/articles';
  const username = ref('')
  const password1 = ref('')
  const password2 = ref('')
  const store = useArticleStore()
  //양방향 바인딩 작동확인하기

  //맞게 작동되는 것 확인됨
  //회원가입할 때 => 받은 데이터를 서버로 전달할 것 == 이떄 서버와의 통신 : 비동기 axios쓴다.
  const signUp = function() {
    //signup을 할 것인데 => 서버에 어떤 내용을 보낼 것인가? ==> 사용자가 입력한 내용 ==> 그런데 이것을 묶음으로
    const payload = {
      username : username.value,
      password1 : password1.value,
      password2 : password2.value
    }
    //이 payload를 비동기로 보내줄 것 => 서버와 통신하려면 axios
    //따라서 스토어에 전달해야함
    store.signUp(payload)    
  }

</script>

<style scoped>

</style>