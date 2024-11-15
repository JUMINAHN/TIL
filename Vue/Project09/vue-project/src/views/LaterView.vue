
<template>
  <!--뒤로가기 생성-->
  <h1>나중에 볼 동영상</h1>
  <!--저장된 동영상 리스트 -->
  <!--homeview와 동일하게 출력하면 될 듯-->
  <!--있고, 없고에 대한 표기 -->
  <div class="row row-cols-1 row-cols-md-2 g-4">
    <div v-if="checkVideo > 0">
      <SaveContent 
      v-for="video in videos"
      :key="video.id"
      :video="video"
      />
    </div>
    
    <div v-else>
      <p>등록된 컨텐츠가 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import SaveContent from '@/components/SaveContent.vue';
import { useYoutubeStore } from '@/stores/youtube';
import { computed } from 'vue';
import { RouterLink } from 'vue-router';
const store = useYoutubeStore() //store
//저장된 동영상이 맞게 되었는지 확인해보자
console.log(store.myVideo) //동영상 저장 성공 확인
const videos = store.myVideo
//이거 계산 수시로?
const checkVideo = computed(() => videos.length)



</script>

<style scope>

</style>
