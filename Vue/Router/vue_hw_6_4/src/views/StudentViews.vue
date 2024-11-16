<template>
  <div>
    <h1>학생 상세 정보 목록 입니다.</h1>
    <!--router.push라는게 StudentView에서 StudentDSetail로 가는 것-->
    <template v-for="student in studentName" :key="student.name"> <!--name을 설정-->
      <p @click="goDetail(student.name)">{{student.name}} 학생 정보 보기</p> <!--여기에 a link를 연결한다.-->
      <!--이거 인자를 왜받아야 함 ??? -->
    </template>
  </div>
</template>

<script setup>
  import {ref} from 'vue'
  import { useRouter } from 'vue-router';
  
  //학생정보 객체를 여기다 만드는 것인지? => view에서 보여줄것이니까..? QQ
  const studentName = ref([
    {name : '김하나'},
    {name : '김두리'},
    {name : '김서이'},
  ])

  const router = useRouter() //route=> 이부분의 파라미터가 필요함
  // const studentId = ref(router.params.name)
  // console.log(studentId) //parameter로 불러오는 것 => 파라미터를 부르는 것
  // //근데 값이 없는 듯??

  const goDetail = function(name) {
    //파라미터가 없다? 
    router.push({name : 'studentDetail', params : {name : name}}) //studentName을 파라미터로 받는데..
  }

</script>

<style lang="scss" scoped>

</style>