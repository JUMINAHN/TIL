
<template>
  <h1>HOME</h1>
  <div class="row row-cols-1 row-cols-md-2 g-4">
    <!--여러개가 바인딩-->
    <!--여기서 videocontent-->
    <!--본 영상으로 필터링해주고-->
    <VideoContent 
      v-for="video in filteredVideos" 
      :key ="video.id"
      :video="video"
    />
  </div>
</template>

<script setup>
//생성형 AI 활용 => 본 내용 필터링 
import VideoContent from '@/components/VideoContent.vue';
import { useYoutubeStore } from '@/stores/youtube';
import { computed, ref } from 'vue';
import { RouterLink } from 'vue-router';


const store = useYoutubeStore()
const search = ref(null) //이것을 백엔드로 보내줘야 함 => 이 친구 자체를 보내줄 것
const videos = store.video //search한 내용을 기반으로 
const filteredVideos = computed(() => {
  return store.video.filter(video => !store.watchedVideos.includes(video.id.videoId))
})

</script>

<style scope>
/* div 목록 정리해야 함 => 일단 동영상 정확하게 불러오는 방법 알아야 함 */

</style>
