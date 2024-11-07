
<template>
  <div>
    <header>명함 관리 페이지</header>
    <article>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</article>
    <main>
      <BusinessCard />
    </main>
    <footer>
      <div>
        © 2023 My Business Cards
      </div>
    </footer>
  </div>
</template>

<script setup>
  import BusinessCard from '@/components/BusinessCard.vue';
</script>

<style scoped>
  div {
    text-align: center;
  }

  main {
    padding-top: 30px;
  }

  header {
    display: inline-block;
    height : 50px;
    width: 400px;
    padding : 80px 0;
    text-align: center;
    font-size: xx-large;
    color : white;
    background-color:rgb(44, 153, 231);
  }

  footer > div{
    /* display: block; */
    background-color: rgb(204, 195, 195);
    position : fixed;
    width: 120%; /*width를 다니까 바로 문제 해결 */
    /*이유는 무엇? */
    /*왼쪽 여백이 발생하는 이유?*/
    bottom : 0;
  }

</style>
