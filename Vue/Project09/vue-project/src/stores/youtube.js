import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useYoutubeStore = defineStore('youtube', () => {
  //정보를 받아온 것을 여러군데에서 다룰 것, 먼저 정보를 가져와야 함
  const video = ref([]) //생성 
  const router = useRouter()
  const myVideo = ref([]) //나의 비디오

  //생성형 AI 활용 --> 시청한 영상 숨기기
  const watchedVideos = ref([])
  const markAsWatched = (videoId) => {
    if (!watchedVideos.value.includes(videoId)) {
      watchedVideos.value.push(videoId)
    }
  }

  //get으로 정보를 가져올 것 생성
  const getVideo = function(search) { //사용자가 input한 값
    //여기서 axios를 실행
    axios({
      method : 'get',
      //여기서 일부파라미터 변경할 것
      url : `https://www.googleapis.com/youtube/v3/search`, //정보가 맞게 나옴
      params : {
        //업로드시 제거
        key :'나의 API 키를 등록합니다.',
        part : 'snippet',
        type : 'video',
        q : search,//파라미터로 받은 것들 input으로 들어가짐
        // videoDefinition: 'high',  // 고화질 비디오만 검색
        maxResults: 15,
        // fields: 'items(id,snippet(thumbnails/maxres,thumbnails/high))'  // 고화질 썸네일 요청
      }
    }) //맞게 되는지만 확인해보자
    .then((res) => {
      console.log(res, 'check') //원하는 데이터가 출력되는 것으로 확인할 수 있음
      //data를 더 다양하게 받아야 함
      // video.value = res.data // res.data 자체를 출력하고 => 메인화면으로 돌아가는 것
      video.value = res.data.items
      console.log('비디오 params 받음', video.value)
      router.push({name : 'home'}) //홈으로 돌아가서 => 내용을 뿌려준다면?

    })
    .catch((err) => {
      console.log(err, 'why error?')
    })
  }

  const getDetail = function(videoId) {
    //getDetail로 받음 => parameter id 자체를 => string 값
    //배열 전체에서 확인
    return video.value.find(myVideo => {
      return myVideo.id.videoId === videoId
    })
  }

  //새로운 배열에 저장 => 나의 비디오에 저장하는 것
  const saveMyVideo = function (detail) {
    myVideo.value.push(detail) //객체 그 자체를 출력
    alert('저장에 성공했습니다!')
    console.log(myVideo) //동영상 리스트
  }

  //저장된 동영상 삭제
  const removeMyVideo = function (detail) {
    //일치하면 => 삭제
    const index = myVideo.value.findIndex((ele) => { //filter 특정 값 제거
      return ele.id.videoId === detail.id.videoId //이게 같을 경우
    })
    if (index !== -1) {
      //있는 것이라면
      myVideo.value.splice(index, 1)
      alert('삭제 완료')
    } else {
      alert('내부 속성값에 의하여 삭제할 수 없습니다.')
    }
  }

  return {removeMyVideo,getVideo, video, getDetail, myVideo, saveMyVideo, watchedVideos, markAsWatched}
}, {persist : true})
