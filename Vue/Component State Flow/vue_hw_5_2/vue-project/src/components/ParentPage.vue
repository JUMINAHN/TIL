<template>
  <div>
    <h1>부모 페이지입니다.</h1>
    <!--페이지 3개로 나누어 등록? :props 선언 그럼 지금 children을 활용한다는 것-->
    <!--props이름 : props값 -->

    <!--변수명 일단 바꾸기-->
    <!--단순 넘겨주기  :dynamic-props="children"  -->
    <!--이번에는 넘겨줄게 child임-->
    <Childpage 
    v-for="child in children" 
    :key="child.name"
    :dynamic-props="child" /> <!--이거 배열 반복해서 등록하기 -->
    <!--childpage에서 넘겨받기 가능-->
  </div>
</template>

<script setup>
  import {ref} from 'vue'
  import Childpage from '@/components/Childpage.vue';
  //children 배열을 작성한다.
  const children = ref([ //선언
    {name : "김하나", age:30},
    {name : "김두리", age:20},
    {name : "김서이", age:10},
  ])
</script>

<style scoped> /*원하는 것 처럼 전체가 적용되었지만, 의도치 않은 더 외부의 값까지 적용됨 */
  div {
  border: 1px solid grey;
  padding: 10px;
}
</style>