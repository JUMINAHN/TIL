<template>
  <div>
    <h2>가수 이름</h2>
    <img src="@/assets/singer.jpg" alt="img">
    <p>가수 소개글</p>
  </div>
</template>

<script setup>

</script>

<style  scoped>
  img {
    /* border: 1px solid black; */
    border-radius: 50%;
    width : 200px;
    height: 200px;
  }
  div {
    border: 1px solid black; /*원하는 라인에*/
    /* width: 800px;
    height: 500px; */
    /* text-align: center; */
    margin: 1rem 3rem 1rem 3rem;
    display: flex;
    flex-direction:column;
    justify-content:center;
    align-items: center;

  }
</style>