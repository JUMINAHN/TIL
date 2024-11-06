# d

날짜: 2024년 11월 4일

# vue.global.js:2260 [Vue warn]: Unhandled error during execution of native event handler at <App>

---

⇒ Uncaught TypeError: now_data.foreach is not a function

```jsx
          //obj는 in객체 사용
for (const data in datas) { //이렇게 하면 단순 키값만 추출이 된다.
   if (Array.isArray(datas[data])) {
       now_data = datas[data]
       now_data.foreach((now) => {
        console.log(now)
       })
 } else {
     console.log(datas[data])
      }
 }
```

# 서버에 폼이 제출되는 문제

---

```
    <form submit.prevent="createCard"> <!--해당 이벤트가 실행됨-->

```

⇒ 누락 `@`

# 값이 의도한대로 나오지 않은 문제

---

```jsx
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        //양방향 바인딩
        const inputTitle = ref('')
        const inputContent = ref('')
        const inputColor = ref('')
        //카드 관련 
        const cardTitle = inputTitle.value //해당 값
        const cardContent = inputContent.value
        const cardColor = inputColor.value //각각의 값을 할당

        //순서대로 만들어진 제목, 내용, 배경색 
        //각 변수는 상기 값을 활용하여 할당한다??
        const isCreatedCard = ref(false) //카드 생성 여부 -> class속성 card를 지닌 div에 적용된다
        const createCard = function() {
          //호출되면 true로 변경된다 => true로 변경되면 화면에 출력된다 => v-show
          if (isCreatedCard.value == false) {
            isCreatedCard.value = true 
            //true이면 화면에 출력
          } else {
            isCreatedCard.value = false
          }
          inputTitle.value = ''
          inputContent.value = ''
          inputColor.value = ''
        }

        return {
          inputTitle,
          inputContent,
          inputColor,
          isCreatedCard,
          cardTitle,
          cardContent,
          cardColor,
          createCard
        }
      }
    })

    app.mount('#app')
```

<aside>
💡

**GPT의 도움**

</aside>

 `cardTitle`, `cardContent`, 그리고 `cardColor`의 값이 제대로 반영되지 않기 때문

```jsx
    <div class="card" :class="{cardColor:isCreatedCard}"> <!--여기에 isCreatedCard가 적용됨-->
      <!--true로 변경되면 vshow? -->
      <!--이게 참이면?-->
      <h2 v-show="isCreatedCard">{{cardTitle}}</h2> <!--true면 제목 : 제출하고나면 displaynone 해제 -->
      <p v-show="isCreatedCard">{{cardContent}}</p> <!--true면 내용-->
    </div>
  </div>

```

⇒ **`cardColor`**는 단순한 문자열이므로, 클래스가 아니라 **스타일 속성**으로 처리

⇒ **`v-show="isCreatedCard"` 동작 문제**:

- **`v-show="isCreatedCard"`**는 카드가 생성되었을 때만 내용을 보여주기 위한 조건입니다. 하지만 카드의 제목과 내용(**`cardTitle`**, **`cardContent`**)이 빈 값일 경우, 아무것도 보이지 않을 수 있습니다.

**⇒ 카드 생성 후 입력 필드 초기화**:

- 카드가 생성된 후 입력 필드를 비우는 로직은 제대로 동작하고 있지만, 그 전에 값이 제대로 할당되지 않으면 화면에 아무것도 나타나지 않습니다.

### 문제점

1. **`cardTitle`, `cardContent`, `cardColor`의 초기화 방식**:
    - 현재 코드에서는 `inputTitle.value`, `inputContent.value`, 그리고 `inputColor.value`를 **초기화 시점에** 각각 `cardTitle`, `cardContent`, 그리고 `cardColor`에 할당하고 있습니다.
    - 하지만 Vue의 반응형 시스템에서, 이러한 방식은 **초기 값만** 할당될 뿐, 이후에 `inputTitle`, `inputContent`, `inputColor`가 변경되더라도 **자동으로 업데이트되지 않습니다**. 즉, 양방향 바인딩이 제대로 이루어지지 않는 상황입니다.

```jsx
        // 카드 관련 변수
        const cardTitle = ref('')
        const cardContent = ref('')
        const cardColor = ref('')

        //순서대로 만들어진 제목, 내용, 배경색 
        //각 변수는 상기 값을 활용하여 할당한다??
        const isCreatedCard = ref(false) //카드 생성 여부 -> class속성 card를 지닌 div에 적용된다
        const createCard = function() {
          //호출되면 true로 변경된다 => true로 변경되면 화면에 출력된다 => v-show
          //이떄 입력된 값 할당
          cardTitle.value = inputTitle.value
          cardContent.value = inputContent.value
          cardColor.value = inputColor.value

          inputTitle.value = ''
          inputContent.value = ''
          inputColor.value = ''

          if (isCreatedCard.value == false) {
            isCreatedCard.value = true 
            //true이면 화면에 출력
          } else {
            isCreatedCard.value = false
          }
        }
```

## 왜 v-show를 div 자체에 선언해야하고, style을 선언해야하는가?

---

1. **왜 `v-show="isCreatedCard"`를 `<div class="card">`에 선언해야 하는가?**
    - **카드 전체를 제어**하기 위해서
    - `v-show`는 `isCreatedCard`가 `true`일 때만 해당 `<div>`와 그 안의 내용을 **보이게** 하고, `false`일 때는 **숨긴다**.
2. **왜 `:style="{ backgroundColor: cardColor }"`를 선언해야 하는가?**
    - **카드의 배경색을 동적으로 변경**하기 위해서
    - 사용자가 선택한 색상이 `cardColor`에 저장되고, 이를 카드의 배경색으로 적용하려면 **인라인 스타일**로 설정해야 한다.

| 항목 | 이유 |
| --- | --- |
| **v-show="isCreatedCard"** | 카드가 생성되었을 때만 카드 전체를 보이게 하기 위해 |
| **:style="{ backgroundColor: cardColor }"** | 사용자가 선택한 배경색을 카드에 동적으로 적용하기 위해 |
|  |  |