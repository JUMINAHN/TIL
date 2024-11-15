
<template>
  <h1>비디오 검색</h1>
  <!-- <RouterLink :to="{name : 'home'}">⇦ /뒤로가기</RouterLink> -->
  <div>  
    <form class="d-flex" role="search" @submit.prevent="searchVideo(search)">
      <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model="search">
      <!--여기에 검색어를 입력하면 ? youtube api로부터 json 데이터를 받아올 수 있음 -->
      <button class="btn btn-outline-success" type="submit">Search</button>
    </form>
  </div>
  <br>
  <!-- <p>당신이 찾은 검색어 : {{ store.q }}</p> -->
  <!--여기서는 searchVIew에서 찾은 내용을 보고 싶은 것-->

  <div v-if="videos && videos.length > 0"> <!--비디오가 있을때, 그리고 videos의 길이가 0보다 클떄-->
    <div class="row row-cols-1 row-cols-md-2 g-4">
      <!--여러개가 바인딩-->
      <VideoContent 
        v-for="video in videos"
        :key ="video.id"
        :video="video"
      />
    </div>
  </div>

  <br>
  <h2>추천 콘텐츠</h2>
  <div class="row row-cols-1 row-cols-md-2 g-4">
    <VideoContent 
      v-for="video in recommendedVideos"
      :key="video.id"
      :video="video"
    />
  </div>
</template>

<script setup>
//생성형 AI활용 : 여기에는 추천 콘테츠를 표시하는 것으로 변경
import VideoContent from '@/components/VideoContent.vue';
import { useYoutubeStore } from '@/stores/youtube';
import { computed, ref } from 'vue';
import { RouterLink } from 'vue-router';

// 임의의 추천 비디오 목록
const recommendedVideos = ref([ //임의의 추천 비디오 목록을 띄워준다. => 사용자가 비디오를 시청했을 때 또 표시
  {
    id: { videoId: 'rec1' },
    snippet: {
      title: '추천 비디오 1',
      thumbnails: { high: { url: 'https://example.com/thumb1.jpg' } }
    }
  },
  {
    id: { videoId: 'rec2' },
    snippet: {
      title: '추천 비디오 2',
      thumbnails: { high: { url: 'https://example.com/thumb2.jpg' } }
    }
  },
  // 더 많은 추천 비디오...
])


//store에 있는 내용 => video를 보고 싶은 것
const store = useYoutubeStore()
const search = ref(null) //이것을 백엔드로 보내줘야 함 => 이 친구 자체를 보내줄 것
//반복적 점검
const videos = computed(() => store.video) 
//store.video //search한 내용을 기반으로 

//getvideo 호출해야함
const searchVideo = function(search) {
  store.getVideo(search)
}

</script>

<style scope>
/* div 목록 정리해야 함 => 일단 동영상 정확하게 불러오는 방법 알아야 함 */

</style>
