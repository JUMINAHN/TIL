
# Basic Syntax1 [실습]
날짜: 2024년 11월 4일

# vue.global.js:2260 [Vue warn]: Template compilation error: v-model can only be used on <input>, <textarea> and <select> elements.
---

```jsx
<option value="" disabled selected v-model="formData.residence">거주지를 선택하시오.</option>
```

⇒ option에 입력해서 오류가 발생함

## 양방향 바인딩에 대해 이해가 아직 부족함

---

```html
<body>
  <div id="app">
    <h1>설문조사</h1>

    <form @submit.prevent="submitForm">
      <div>
        <label for="name">이름: </label>
        <input id="name" type="text" v-model="formData.name">
      </div>

      <div>
        <label for="email">이메일: </label>
        <input id="email" type="email" v-model="formData.email">
      </div>

      <div>
        <label for="age">나이: </label>
        <input id="age" type="number" v-model="formData.age">
      </div>

      <div>
        <label for="residence">거주지: </label>
        <!--select에 v-model을 넣어준다. -->
        <select id="residence" v-model="formData.residence">
          <option value="" disabled>거주지를 선택하시오.</option>
          <option>서울</option>
          <option>경기</option>
          <option>충청</option>
          <option>전라</option>
          <option>경상</option>
        </select>
      </div>

      <div>
      <!--귀찮지만 다 하나씩 부여해야 한다. -->
        <label>사용하는 언어: {{ formData.languages }}</label>
        <div>
          <input type="checkbox" id="python" value="Python" v-model="formData.languages">
          <label for="python">Python</label>
        </div>
        <div>
          <input type="checkbox" id="javascript" value="JavaScript" v-model="formData.languages">
          <label for="javascript">JavaScript</label>
        </div>
        <div>
          <input type="checkbox" id="csharp" value="C#" v-model="formData.languages">
          <label for="csharp">C#</label>
        </div>
        <div>
          <input type="checkbox" id="ruby" value="Ruby" v-model="formData.languages">
          <label for="ruby">Ruby</label>
        </div>
      </div>
      <input type="submit" value="제출">
    </form>
  </div>

  <script src="<https://unpkg.com/vue@3/dist/vue.global.js>"></script>
  <script>
    const { createApp, ref, reactive } = Vue

    const app = createApp({
      setup() {
        const formData = reactive({
          name: '',
          email: '',
          age: 0,
          residence: '',
          languages: []
        })

        function submitForm() {
          console.log(formData)
        }

        return {
          formData,
          submitForm
        }
      }
    })

    app.mount('#app')
  </script>
</body>

```

주요 변경 사항 및 설명:

1. `v-model` 사용: 모든 입력 필드에 `v-model`을 추가했습니다. 이를 통해 입력 값과 `formData` 객체의 속성이 양방향으로 바인딩됩니다[1].
2. `reactive` 사용: `ref` 대신 `reactive`를 사용하여 `formData` 객체를 생성했습니다. 이는 객체 전체를 반응형으로 만들기 위함입니다[4].
3. `languages` 배열: 체크박스를 위해 `languages`를 빈 배열로 초기화했습니다. 이렇게 하면 여러 언어를 선택할 수 있습니다[1].
4. 셀렉트 박스: `residence` 셀렉트 박스에도 `v-model`을 추가하여 선택된 값이 `formData.residence`에 바인딩되도록 했습니다[4].
5. 체크박스: 모든 체크박스에 동일한 `v-model="formData.languages"`를 사용했습니다. 이렇게 하면 선택된 모든 언어가 `languages` 배열에 추가됩니다[1].
6. `submitForm` 함수: 폼 제출 시 전체 `formData` 객체를 콘솔에 출력합니다.

이렇게 수정하면 모든 입력 필드가 `formData` 객체와 양방향으로 바인딩되며, 사용자가 입력한 데이터가 자동으로 `formData` 객체에 반영됩니다. 폼을 제출하면 `console.log(formData)`를 통해 모든 입력된 데이터를 확인할 수 있습니다[2][3].

## languages 배열로 설정한 이유

---

<aside>
💡

**다중 선택 가능성**: 사용자가 여러 프로그래밍 언어를 선택할 수 있도록 하기 
위해서

</aside>

- 배열은 여러 개의 데이터를 한 번에 저장하고 관리할 수 있는 데이터 구조
- 사용자가 Python, JavaScript, C# 등 `여러 언어를 선택`할 경우, 이 선택들을 배열로 저장하여 처리할 수 있다.

<aside>
💡

**데이터 그룹화**: 배열은 `관련된 데이터를 그룹화`하여 효율적으로 관리할 수 있다. 

</aside>

- 언어 선택과 같은 경우, 여러 선택지를 하나의 변수에 담아 서버로 전달하기 위해 배열을 사용하는 것이 일반적
- 예를 들어, 사용자가 Python과 JavaScript를 선택했다면, 서버에서는 이를 `['Python', 'JavaScript']`와 같은 배열로 처리

<aside>
💡

1. **반복 처리 용이성**: 배열은 반복문과 결합하여 데이터를 쉽게 처리할 수 있다.
</aside>

- 사용자가 선택한 언어들을 서버 측에서 반복문을 통해 하나씩 처리하거나 출력할 수 있다.

## 객체가 안되는 이유

---

**[데이터 구조의 차이]**

- 배열은 순차적으로 데이터를 저장하며, 각 요소는 인덱스를 통해 접근
    - 언어 선택과 같은 경우에는 순서보다는 **다중 선택**이 중요한데, 배열은 이러한 다중 선택을 관리하기에 적합한 구조
- 반면, 객체는 키-값 쌍으로 데이터를 저장
    - 객체는 주로 특정 키와 관련된 값을 저장할 때 사용

# 과도한 ref사용

---

- Vue.js에서 `ref()`와 `reactive()`는 **반응형 데이터**를 관리할 때 자주 사용되는 도구들

## **`ref()`와 `reactive()`의 차이**

---

- **`ref()`**: 단일 값(원시 값이나 객체)을 반응형으로 만들 때 사용
- 주로 **원시 값**(문자열, 숫자, 불리언 등)을 감싸서 반응형으로 처리할 때 유용
    - 예: `const name = ref('')`
    - 이 경우, `name.value`로 접근해야 합니다.

- **`reactive()`**: **객체나 배열과 같은 복잡한 데이터 구조를 반응형**으로 만들 때 사용
    - **객체의 속성 전체를 반응형으로 처리하며, 속성에 직접 접근.**
    - 예: `const formData = reactive({ name: '', email: '', age: 0 })`
    - 이 경우, `formData.name`처럼 바로 접근 가능합니다.

### **언제 `ref()`를 사용해야 할까?**

- **단일 값**을 다룰 때는 `ref()`가 적합합니다. 예를 들어, 단순한 카운터나 플래그 값을 관리할 때는 `ref()`로 감싸서 사용하는 것이 좋습니다.
- 하지만 복잡한 폼 데이터나 여러 개의 속성을 가진 객체라면, **`reactive()`*를 사용하는 것이 더 효율적입니다.

<aside>
💡

현재 코드에서 모든 데이터를 굳이 `ref()`로 남발할 필요는 없다.

폼 데이터와 같이 여러 속성이 있는 경우에는 **`reactive()`*를 사용하여 객체 전체를 반응형으로 만드는 것이 더 간단하고 효율적이다.

</aside>

## vue.global.js:2260 [Vue warn]: Unhandled error during execution of native event handler at <App>

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

## 서버에 폼이 제출되는 문제

```html
<form submit.prevent="createCard"> <!--해당 이벤트가 실행됨-->
```

⇒ 누락 `@`

## 값이 의도한대로 나오지 않은 문제

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

**GPT의 도움**

`cardTitle`, `cardContent`, 그리고 `cardColor`의 값이 제대로 반영되지 않기 때문

```jsx
<div class="card" :class="{cardColor:isCreatedCard}"> <!--여기에 isCreatedCard가 적용됨-->
  <!--true로 변경되면 vshow? -->
  <!--이게 참이면?-->
  <h2 v-show="isCreatedCard">{{cardTitle}}</h2> <!--true면 제목 : 제출하고나면 displaynone 해제 -->
  <p v-show="isCreatedCard">{{cardContent}}</p> <!--true면 내용-->
</div>
```

⇒ **`cardColor`**는 단순한 문자열이므로, 클래스가 아니라 **스타일 속성**으로 처리

⇒ **`v-show="isCreatedCard"` 동작 문제**:
- **`v-show="isCreatedCard"`**는 카드가 생성되었을 때만 내용을 보여주기 위한 조건입니다. 하지만 카드의 제목과 내용(**`cardTitle`**, **`cardContent`**)이 빈 값일 경우, 아무것도 보이지 않을 수 있습니다.

⇒ **카드 생성 후 입력 필드 초기화**:
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

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/26143310/eb368777-0827-4e3e-b4a2-b2e16d0d28e3/paste.txt