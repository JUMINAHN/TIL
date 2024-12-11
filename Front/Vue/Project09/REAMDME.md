# [실습] 관통 과제

날짜: 2024년 11월 15일

# ⚠️ API 공식 문서 이해가 어려움

---

⇒ 해당 참고문을 보고 문제를 품,, 셀프로 읽는데 어려움을 느껴서 해당 부분 보완 필요

# API키를 제대로 받아오지 못하는 문제

---

```jsx
    axios({
      method : 'get',
      //여기서 일부파라미터 변경할 것
      url : `https://www.googleapis.com/youtube/v3/search`,
      data : { 
        key :'',
        part : 'snippet',
        type : 'video',
        q : search//파라미터로 받은 것들 input으로 들어가짐
      }
```

⇒ params를 data로 입력한 오류

## 화질이 너무 안좋게 나옴

---

![image.png](image.png)

⇒ 해상도 높게 설정하는 방법

```jsx
const getVideo = function(search) {
  axios({
    method: 'get',
    url: 'https://www.googleapis.com/youtube/v3/search',
    params: {
      key: 'YOUR_API_KEY',
      part: 'snippet',
      type: 'video',
      q: search,
      videoDefinition: 'high',  // 고화질 비디오만 검색
      maxResults: 10
    }
  })
}
```

⇒ video content의 문제

```jsx
<img :src="video.snippet.thumbnails.high.url" class="card-img-top" alt="video1">
```

⇒ `default` 로 처음에 값을 설정해서 화질이 안좋게 나옴

# ⚠️ Paramas 매개변수를 받지 못하는 문제 발생

---

```jsx
    <RouterLink :to="{name : 'detail'}"> <!--RouterLink정보-->
      <div class="card" > <!--여기자체에 router를 달기-->
        <img :src="video.snippet.thumbnails.default.url" class="card-img-top" alt="video1">
        <div class="card-body">
          <p class="card-text">title : {{ video.snippet.title }}</p>
        </div>
      </div>
    </RouterLink>
```

⇒ 단순 detail값만 받고 있는 문제 때문

Q. 궁금한게 여기서 왜 params를 `video.id.videoId로 받아야`  하는지? ⇒ id값은 내가 설정했지만 videoId..?

# Detail Page 이해하기

---

1. route와 파라미터
    - `useRoute()`는 현재 라우트 정보를 가져오는 Vue Router의 함수예요.
    - 이 **route 객체를 통해 URL의 파라미터를 읽을 수 있어요.**
2. 파라미터 접근 방법
    - `route.params`를 통해 **URL의 파라미터에 접근**할 수 있어요.
    - 예를 들어, URL이 '/detail/123'이고 라우트가 '/detail/:data'로 정의되어 있다면, `route.params.data`는 '123'이 됩니다.
3. 왜 바로 뽑아올 수 없나요?
    - 파라미터는 URL을 통해 전달되기 때문에, 페이지가 로드될 때 사용할 수 있어요.
    - 하지만 다른 방식(예: 클릭 이벤트)으로 데이터를 전달하려면, 추가적인 작업이 필요해요.
4. 클릭 이벤트와 파라미터
    - 클릭 이벤트로 데이터를 전달하려면, 라우터 네비게이션 시 데이터를 함께 보내야 해요.
    - 예: `router.push({ name: 'detail', params: { data: videoId } })`
5. 해결 방안
    - **클릭 시 데이터를 라우터로 전달하고, DetailPage에서 그 데이터를 사용**하세요.
    - 또는 클릭한 비디오의 ID를 URL 파라미터로 사용하고, 그 ID로 스토어에서 데이터를 찾으세요.

## params: { data: videoId }

---

- **`params`**는 라**우트에 전달할 파라미터를 정의**합니다.
- **`data`**는 **파라미터의 이름**입니다. 라우터 설정의 경로와 일치해야 합니다 (예: '/detail/:data').
- **`videoId`는 실제로 전달하려는 값**입니다. 보통 클릭한 비디오의 고유 ID가 됩니다

### 파라미터 받기 전이라 search에 해당 값 출력

---

`Missing required param "data”`

→ v-if로 문제를 해결하려했으나 약간의 오류

```jsx
const store = useYoutubeStore()
const search = ref(null) //이것을 백엔드로 보내줘야 함 => 이 친구 자체를 보내줄 것
const videos = store.video //search한 내용을 기반으로 

```

⇒ `search` 기준으로 넣으면 : input값에 1개라도 들어가면 이상한 중복 오류가 발생

![image.png](image%201.png)

 

⇒ videos를 넣으면 똑같은 params 오류

```jsx
// 변경 후
{
  path: '/search/:data?', //? 값 부여
  name: 'search',
  component: SearchView
}
```

1. **`?`**는 "있어도 되고 없어도 돼"라는 뜻
2. 이전에는 **`/search`** 주소로 갈 때 반드시 뭔가를 붙여야 했다.
3. 이제는 **`/search`**만으로도 갈 수 있고, **`/search/무언가`**로도 갈 수 있다.
4. 그래서 처음 페이지를 열 때 아무것도 없어도 오류가 나지 않는다.

### Detail 페이지 출력 문제

---

```jsx
import { useYoutubeStore } from '@/stores/youtube';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

  //파라미터로 사용할 수 있음 => index로 받음?
  //파라미터를 어떻게 받는가?
  //route => 파라미터 아이디로 
  const store = useYoutubeStore()
  const route = useRoute()
  //파라미터가 없다
  const videoId = route.params.id
  //이거 받아서 띄울 수 있어야 함
  const video = videoId
  console.log(video, '.')

  //특정
```

⇒ 원하는 값의 출력 문제

⇒ `Detial의 특징은`  route로 파라미터 값을 받아올 수 있음

# Object object로 출력되는 문제

---

```
    <RouterLink :to="{name : 'detail', params:{data:video.id}}"> <!--RouterLink정보-->

```

<aside>
💡

**수정 사항**

</aside>

```jsx
RouterLink :to="{name : 'detail', params:{data:video.id.videoId}}"> <!--RouterLink정보-->
```

⇒ YouTube Data API의 응답 구조 때문

```jsx
javascript{
  kind: "youtube#searchResult",
  etag: "...",
  id: {
    kind: "youtube#video",
    videoId: "실제 비디오 ID"
  },
  snippet: {
    *// 비디오 정보 (제목, 설명 등)*
  }
}
```

⇒ 구조 이해

## ⚠️ getDetail 구문 오류

---

- 의도 getDetail로 id값을 뽑아와서 같은지 확인하고, 반환해서 해당 부분을 다룰려고 했음

```jsx
  const getDetail = function(videoId) {
    //getDetail로 받음 => parameter id 자체를 => string 값
    //배열 전체에서 확인
    video.value.find((myVideo) => {
      //참이면 정보 => 아이디 반환 = 같음을 반환
      return videoId == myVideo //같은지 확인
    })
    return video//아니면 배열 반환
  }
```

⇒ 주어진 **`videoId`**와 일치하는 비디오 객체를 찾아 반환하려는 의도

<aside>
💡

**수정 사항**

</aside>

```jsx
  const getDetail = function(videoId) {
    //getDetail로 받음 => parameter id 자체를 => string 값
    //배열 전체에서 확인
    return video.value.find(myVideo => {
      return myVideo.id.videoId === videoId
    })
  }

```

⇒ 객체들 중 하나 하나 내부 값을 비교해야하니까 ⇒ 원래는 console.log로 찍어서 더 deep하게 봐야 함

1. 외부 함수의 `return`: ⇒ getDetail값을 받아서 활용해야하기 때문
    
    ```jsx
    const getDetail = function(videoId) {
      return ...
    }
    
    ```
    
    이 `return`은 `getDetail` 함수의 결과를 반환합니다. 이 함수가 찾은 비디오 객체를 반환하기 위해 필요합니다.
    
2. 내부 화살표 함수의 `return`:
    
    ```jsx
    return myVideo.id.videoId === videoId
    
    ```
    
    이 `return`은 `find` 메서드에 전달된 화살표 함수 내부에 있습니다. 이 `return`은 각 `myVideo` 객체에 대해 조건이 참인지 거짓인지를 반환합니다.
    

```jsx
const getDetail = function(videoId) {
  return video.value.find(myVideo => myVideo.id.videoId === videoId)
}
// 더 깔끔하게
```

# Iframe 출력 오류

---

```jsx
<template>
  <h1>상세 내용</h1>
  <div>
    <iframe
    :width="1024"
    :height="600"
    :src="detail.snippet.thumbnails.high.url"
    class="card-img-top"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen/>
    <div class="card" style="width: 32rem;">
    <!-- <img :src="detail.snippet.thumbnails.high.url" class="card-img-top" alt="..."> -->
    <div class="card-body">
      <p class="card-text">{{detail.snippet.publishTime}}</p>
      <h5 class="card-title">{{detail.snippet.title}}</h5>
      <p class="card-text">{{detail.snippet.description}}</p>

      <RouterLink :to="{name : 'later'}"  class="btn btn-primary">동영상 저장</RouterLink>
    </div>
    </div>
  </div>
</template>
```

[iframe 삽입에 대한 YouTube Player API 참조 문서  |  YouTube IFrame Player API  |  Google for Developers](https://developers.google.com/youtube/iframe_api_reference?hl=ko)

<aside>
💡

**수정 사항**

</aside>

```jsx
<template>
  <h1>상세 내용</h1>
  <!-- 카드의 너비를 100%로 설정하고 최대 너비를 지정하여 반응형으로 만듭니다 -->
  <div class="card" style="width: 100%; max-width: 1024px;">
    <!-- iframe src를 YouTube 임베드 URL로 변경 -->
    <!-- detail.id는 YouTube 동영상의 고유 ID여야 합니다 -->
    <iframe
      :src="'https://www.youtube.com/embed/' + detail.id.videoId"
      class="card-img-top"
      width="100%" <!-- 너비를 100%로 설정하여 카드에 맞춤 -->
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
      <RouterLink :to="{name : 'later'}" class="btn btn-primary">동영상 저장</RouterLink>
    </div>
  </div>
</template>
```

### 참고 사항

---

- YouTube API는 여러 종류의 ID(채널ID, 재생목록ID, 비디오ID 등)를 다루기 때문에, 이를 구분하기 위해 이런 구조를 사용
- **`detail.id.videoId`**는 API 응답에서 실제 동영상 ID를 가져오는 표준 경로

```jsx
<!-- 올바른 사용법 -->*
:src="'https://www.youtube.com/embed/' + detail.id.videoId"

*<!-- 잘못된 사용법 -->*
:src="'https://www.youtube.com/embed/' + detail.id"  // 작동하지 않을 수 있음`
```

# 배열 자체에서 삭제되나 원하는 값이 삭제되지 않음

---

[savecontent]

```jsx
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
```

⇒ 삭제 메서드 자체는 문제가 없어 보임

[youtube.js] ⇒ store

```jsx
  //저장된 동영상 삭제
  const removeMyVideo = function (detail) {
    //일치하면 => 삭제
    myVideo.value.filter((ele) => { //filter 특정 값 제거
      if(ele.id.videoId === detail.id.videoId) { //같지 않아서?
        console.log(ele, '삭제 video')
        console.log(ele.id , '삭제 video id')
        console.log(ele.id.videoId , '삭제 video id')
        myVideo.value.splice(ele, 1)
        return myVideo //1개 삭제
        //왜 원하는 값이 삭제가 되지 않을까?
      } else {
        alert('삭제가 실패했습니다.') //그냥 전체 배열 자체를 반환
        //삭제가 실패했는데 삭제가 된다?
      }
    })
  }
```

<aside>
💡

**수정 사항**

</aside>

```jsx
const removeMyVideo = function (detail) {
  const index = myVideo.value.findIndex(ele => ele.id.videoId === detail.id.videoId);

  if (index !== -1) {
    myVideo.value.splice(index, 1);
    console.log(`비디오 ID ${detail.id.videoId}가 삭제되었습니다.`);
  } else {
    alert('삭제할 비디오를 찾을 수 없습니다.');
  }
}

```

1. `findIndex` 메소드를 사용하여 삭제하려는 비디오의 인덱스를 찾습니다.
2. 만약 비디오를 찾았다면 (`index !== -1`), `splice` 메소드를 사용하여 해당 인덱스의 요소를 제거합니다.
3. 비디오를 찾지 못했다면 알림을 표시합니다.

이 접근 방식의 장점은 다음과 같습니다:

1. **`filter`는 새로운 배열을 생성하므로, 원본 배열을 직접 수정하지 않습니다. 반면 `splice`는 원본 배열을 직접 수정합니다.**
2. `findIndex`와 `splice`를 사용하면 원하는 요소를 정확히 찾아 제거할 수 있습니다.
3. 조건문을 사용하여 비디오가 존재하는 경우와 존재하지 않는 경우를 명확히 구분합니다.

이 방식을 사용하면 원하는 비디오를 정확히 삭제할 수 있으며, 삭제 성공 여부도 명확히 알 수 있습니다.

## 콜백함수

---

`findIndex()`, `filter()`, `find()` 메소드는 모두 배열을 탐색하는 데 사용되지만 각각 다른 목적과 특성을 가지고 있습니다. 각 메소드의 특징과 적절한 사용 상황을 설명해 드리겠습니다:

## findIndex()

- 조건을 만족하는 첫 번째 요소의 인덱스를 반환합니다.
- 조건을 만족하는 요소가 없으면 -1을 반환합니다.
- **배열에서 특정 요소의 위치를 찾을 때 유용합니다.**

```jsx
const fruits = ["apple", "banana", "orange", "grape"];
const index = fruits.findIndex((fruit) => fruit === "orange");
console.log(index); // 2

```

## filter()

- 조건을 만족하는 모든 요소를 포함하는 새로운 배열을 반환합니다.
- **원본 배열을 변경하지 않습니다.**
- 여러 요소를 찾거나 조건에 맞는 요소들의 부분집합을 만들 때 유용합니다.

```jsx
const numbers = [1, 2, 3, 4, 5];
const evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers); // [2, 4]

```

## find()

- **조건을 만족하는 첫 번째 요소의 값을 반환합니다.**
- 조건을 만족하는 요소가 없으면 **undefined를 반환합니다**
- 특정 조건을 만족하는 **단일 요소를** 찾을 때 유용합니다.

```jsx
const users = [{ id: 1, name: "John" }, { id: 2, name: "Jane" }];
const user = users.find(user => user.id === 2);
console.log(user); // { id: 2, name: "Jane" }

```

## 성능 비교

1. **`findIndex()`와 `find()`는 조건을 만족하는 요소를 찾자마자 탐색을 중단하므로, 대규모 배열에서 단일 요소를 찾을 때 더 효율적**입니다.
2. `filter()`는 항상 전체 배열을 순회하므로, 모든 조건에 맞는 요소를 찾아야 할 때 유용하지만 **단일 요소 검색에는 덜 효율적**일 수 있습니다.
3. 벤치마크 테스트 결과, 대규모 배열에서 `find()`가 `filter()`보다 훨씬 빠른 성능을 보였습니다[4].

## 사용 가이드라인

- 요소의 인덱스가 필요할 때: `findIndex()`
- **조건을 만족하는 모든 요소가 필요할 때: `filter()`**
- 조건을 만족하는 첫 번째 요소의 값만 필요할 때: `find()`
- **대규모 배열에서 단일 요소를 빠르게 찾아야 할 때: `find()` 또는 `findIndex()`**
- 배열의 요소가 조건을 만족하는지 여부만 확인할 때: `some()` (추가 팁)[6]
