<template>
  <div> <!--여기서 사용 가능-->
    <!--자식 데이터 prop받음-->
    <h3>자식 페이지입니다.</h3>
    <p>{{ dynamicProps.name }}</p>
    <p>{{ dynamicProps.age }}</p>
  </div>
</template>

<script setup>
  defineProps({
  'dynamicProps' : Object 
  }) //받아오기 => 객체로 받아와야 함
</script>

<style scoped> /*원하는 것 처럼 전체가 적용되었지만, 의도치 않은 더 외부의 값까지 적용됨 */
  div {
  border: 1px solid grey;
  margin: 10px 3px;
  }
</style>