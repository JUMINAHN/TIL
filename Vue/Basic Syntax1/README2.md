
# Basic Syntax1 [실습]

날짜: 2024년 11월 4일

## Vue 경고 메시지 해결

vue.global.js:2260 [Vue warn]: Template compilation error: v-model can only be used on <input>, <textarea> and <select> elements.

```jsx
<option value="" disabled selected v-model="formData.residence">거주지를 선택하시오.</option>
```

⇒ option에 v-model을 적용해서 오류가 발생했습니다. select 요소에 v-model을 적용해야 합니다.

## 양방향 바인딩 이해

양방향 바인딩에 대한 이해가 아직 부족한 상태입니다. 다음은 올바른 양방향 바인딩 예시입니다:

```html
<body>
  <div id="app">
    <h1>설문조사</h1>
    <form @submit.prevent="submitForm">
      <!-- 폼 내용 -->
    </form>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
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

### 주요 변경 사항 및 설명:

1. `v-model` 사용: 모든 입력 필드에 `v-model`을 추가하여 입력 값과 `formData` 객체의 속성을 양방향으로 바인딩합니다[1].
2. `reactive` 사용: `ref` 대신 `reactive`를 사용하여 `formData` 객체 전체를 반응형으로 만듭니다[4].
3. `languages` 배열: 체크박스를 위해 `languages`를 빈 배열로 초기화합니다[1].
4. 셀렉트 박스: `residence` 셀렉트 박스에 `v-model`을 추가합니다[4].
5. 체크박스: 모든 체크박스에 동일한 `v-model="formData.languages"`를 사용합니다[1].
6. `submitForm` 함수: 폼 제출 시 전체 `formData` 객체를 콘솔에 출력합니다[2][3].

## languages 배열 사용 이유

1. **다중 선택 가능성**: 사용자가 여러 프로그래밍 언어를 선택할 수 있도록 합니다.
2. **데이터 그룹화**: 관련된 데이터를 효율적으로 관리합니다.
3. **반복 처리 용이성**: 배열은 반복문과 결합하여 데이터를 쉽게 처리할 수 있습니다.

## 객체 대신 배열을 사용하는 이유

배열은 순차적으로 데이터를 저장하며, 다중 선택을 관리하기에 적합한 구조입니다. 반면, 객체는 키-값 쌍으로 데이터를 저장하여 특정 키와 관련된 값을 저장할 때 주로 사용됩니다.

## ref 과도 사용 문제

`ref()`와 `reactive()`의 차이:

- `ref()`: 단일 값을 반응형으로 만들 때 사용
- `reactive()`: 객체나 배열과 같은 복잡한 데이터 구조를 반응형으로 만들 때 사용

현재 코드에서 모든 데이터를 `ref()`로 사용할 필요는 없습니다. 폼 데이터와 같이 여러 속성이 있는 경우에는 `reactive()`를 사용하여 객체 전체를 반응형으로 만드는 것이 더 효율적입니다.

## 기타 문제 해결

1. `foreach` 오류: `forEach`로 수정 (대소문자 주의)
2. 폼 제출 이벤트: `<form @submit.prevent="createCard">`로 수정
3. 값이 의도대로 나오지 않는 문제: `createCard` 함수 내에서 값 할당 로직 수정

## v-show와 style 선언 이유

1. `v-show="isCreatedCard"`: 카드 전체를 제어하기 위해 사용
2. `:style="{ backgroundColor: cardColor }"`: 카드의 배경색을 동적으로 변경하기 위해 사용
