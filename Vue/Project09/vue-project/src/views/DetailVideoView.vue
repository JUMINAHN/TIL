<template>
  <h1>상세 내용</h1>
  <!-- 카드의 너비를 100%로 설정하고 최대 너비를 지정하여 반응형으로 만듭니다 -->
  <div class="card" style="width: 100%; max-width: 1024px;">
    <!-- iframe src를 YouTube 임베드 URL로 변경 -->
    <!-- detail.id는 YouTube 동영상의 고유 ID여야 합니다 -->
    <iframe
      :src="'https://www.youtube.com/embed/' + detail.id.videoId"
      class="card-img-top"
      width="100%"
      height="600"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
    <div class="card-body">
      <!-- 기존 내용은 그대로 유지 -->
      <p class="card-text">{{detail.snippet.publishTime}}</p>
      <h5 class="card-title">{{detail.snippet.title}}</h5>
      <p class="card-text">{{detail.snippet.description}}</p>
      <!--routerlink가 아니라 store 버튼을 눌러야 할 것 같음 : 새로운 객체로 보내주는 것-->
      <input type="submit" @click.prevent="saveVideo(detail)" value="동영상 저장" class="btn btn-primary">
      
      <!-- <RouterLink :to=/"{name : 'later'}" class="btn btn-primary">동영상 저장</RouterLink> -->
    </div>
  </div>
</template>

<!--현재까진 일단 동영상 저장 유무가 없음-->
<script setup>
  import { useYoutubeStore } from '@/stores/youtube';
  import { RouterLink, useRoute, useRouter } from 'vue-router';
  //detail에서 파라미터를 받아야하는데 => data로 받을 것임 => 클릭 이벤트로 받은 것
  //클릭을 했음
  const store = useYoutubeStore()
  const route = useRoute()
  const router = useRouter()
  //route로 특정 파라미터 받아오는 것 잊지말기 => params => 내가 :data로 받아올 것이니까 data로 받아보자
  const videoData = route.params.data
  console.log(videoData) //videoId로 전달받음
  //직접 youtube에 요청을 보내서 비디오 상세 정보를 가져올 수 있음 => 새로운 요청
  //기존 자료에서 => 해당 아이디 값을 활용하기 위함 => 이게 더 쉬움
  //맞는지 확인 점검
  const detail = store.getDetail(videoData) //같으면 다시 반환
  
  //생성형 AI : 비디오를 시청한 것으로 표시
  store.markAsWatched(videoData)
  console.log(detail, '세부 내용의 값')

  //동영상 저장
  const saveVideo = function (detail) {
    //store에 배열에 보내서 동영상 저장 => detailPage에 있는 값이니까
    //객체 자체를 보내기 store
    //아직 값 안들어감
    //console.log('동영상 저장 성공!', detail)
    //Laterview에서 확인
    store.saveMyVideo(detail)
    //router.push({name : 'later'}) //동영상 저장 성공 확인
  }


  //특정
</script>

<style>

</style>