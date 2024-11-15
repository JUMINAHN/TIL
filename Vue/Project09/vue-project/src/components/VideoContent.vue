<template>
  <!--content 자체를 누르면 이동 하는 것으로 -->
  <!--routerLink없이 이동 ? -->
  <!--해당 데이터 -->
  <div class="content">
    <!--id값을 받고 있으니까-->
    <!--detail에서 파라미터를 받아야 함-->
    <!--비디오 id 전달 -->
    <!--각각의 파라미터에서 id, videoid로 구성되어있음-->
    <RouterLink :to="{name : 'detail', params:{data:video.id.videoId}}"> <!--RouterLink정보-->
      <div class="card" > <!--여기자체에 router를 달기-->
        <img :src="video.snippet.thumbnails.high.url" class="card-img-top" alt="video1">
        <div class="card-body">
          <p class="card-text">title : {{ video.snippet.title }}</p>
        </div>
      </div>
    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
defineProps({
  video : Object //받았지?
})




</script>

<style scoped>

</style>