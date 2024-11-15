<template>
  <!--content 자체를 누르면 이동 하는 것으로 -->
  <!--routerLink없이 이동 ? -->
  <!--해당 데이터 -->
  <div class="content">
    <!--id값을 받고 있으니까-->
    <!--detail에서 파라미터를 받아야 함-->
    <!--비디오 id 전달 -->
    <!--각각의 파라미터에서 id, videoid로 구성되어있음-->
    <div class="card" > <!--여기자체에 router를 달기-->
      <img :src="video.snippet.thumbnails.high.url" class="card-img-top" alt="video1">
      <div class="card-body">
        <p class="card-text">{{ video.snippet.title }}</p>
      </div>
      <input type="submit" @click.prevent="finishWatch(video)" class="btn btn-primary" value="시청 완료" >
    </div>
  </div>
</template>

<script setup>
import { useYoutubeStore } from '@/stores/youtube';
import { RouterLink } from 'vue-router';
const store = useYoutubeStore()
defineProps({
  video : Object //video로 받아야 함
})

const finishWatch = function (video) {
  store.removeMyVideo(video) 
  console.log('삭제 완료', video) //check한게 아니라 순서대로 삭제되는 것 같음
  //해당 메서드 수정
}

</script>

<style scoped>

</style>