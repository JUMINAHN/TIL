# Basic Syntax1 [실습]

날짜: 2024년 11월 4일

### 참고 자료

---

[SB-Labs Vue.js Start!](https://codelabs-vue.web.app/s05)

# 객체 리터럴

---

<aside>
💡

객체 리터럴 이란?

</aside>

- 중괄호 `{}` 를 사용해 객체를 만드는 간단한 방법.
- 물건을 담는 상자라고 생각하면 된다.
- 이 상자 안에 여러 가지 정보를 넣을 수 있다.

| 개념 | 설명 | 예시 |
| --- | --- | --- |
| 객체 리터럴 | 중괄호 `{}` 로 만든 정보 상자 | `{ 이름: '철수', 나이: 10 }` |
| 속성 (키) | 상자 안의 정보 이름 | `이름`, `나이` |
| 값 | 각 정보의 내용 | `'철수'`, `10` |

## ⚠️ 객체 리터럴과 함수 호출을 결합한 형태

---

1. `hello`: 이것은 **함수의 이름**
2. `({ })`: 이 부분은 **빈 객체를 함수의 인자로 전달하는 것**

```jsx
function hello({ name = '익명', age = 20 }) { //객체 자체 => 함수 설정
  console.log(`안녕하세요, ${name}님! ${age}살이시군요.`);
}

// 함수 호출 예시
hello({}); // 출력: 안녕하세요, 익명님! 20살이시군요.
hello({ name: '철수' }); // 출력: 안녕하세요, 철수님! 20살이시군요.
hello({ age: 25 }); // 출력: 안녕하세요, 익명님! 25살이시군요.
hello({ name: '영희', age: 22 }); // 출력: 안녕하세요, 영희님! 22살이시군요.

```

- 요약하면, `hello({ })` 는 빈 객체를 인자로 받는 `hello` 함수를 호출하는 것

### ⚠️ 조금 더 쉽게 이해하기

---

<aside>
💡

**객체를 함수의 인자로 전달하는 이유**

</aside>

1. **여러 정보를 한 번**에 전달
2. 유연성을 높이기 위해: **필요한 정보만 선택적으로 전달**
3. 코드 가독성을 높이기 위해: 어떤 정보를 전달하는지 명확하게 알 수 있다.

```jsx
// 일반적인 함수
function greet(name, age, city) {
  console.log(`안녕하세요, ${name}님! ${age}살이시고 ${city}에 사시는군요.`);
}
greet('철수', 25, '서울');  // 안녕하세요, 철수님! 25살이시고 서울에 사시는군요.

// 객체를 인자로 받는 함수
function greetObject({ name = '익명', age = '??', city = '어딘가' }) {
  console.log(`안녕하세요, ${name}님! ${age}살이시고 ${city}에 사시는군요.`);
}

greetObject({ name: '영희', city: '부산' });  // 안녕하세요, 영희님! ??살이시고 부산에 사시는군요.
greetObject({ age: 30 });  // 안녕하세요, 익명님! 30살이시고 어딘가에 사시는군요.

```

## 객체 리터럴과 생성자 함수의 개념 이해하기

---

- 객체 리터럴 : 가장 간단한 객체 생성 방법, 중괄호 `{}` 를 사용 ⇒  **객체 리터럴은 간단한 단일 객체**

```jsx
const person = { //
  name: '철수',
  age: 25,
  sayHello: function() {
    console.log('안녕하세요!');
  }
};

```

- 생성자 함수 : 비슷한 객체를 여러 개 만들 때 사용 ⇒ 비슷한 객체를 여러 개 만들 때 편리
    - 함수 이름은 대문자로 시작
    - `new` 키워드와 함께 사용

예시:

```jsx
function Person(name, age) {
  this.name = name;
  this.age = age;
  this.sayHello = function() {
    console.log('안녕하세요!');
  };
}

const person1 = new Person('철수', 25);
const person2 = new Person('영희', 23);

```

| 특징 | 객체 리터럴 | 생성자 함수 |
| --- | --- | --- |
| 생성 방법 | `{}` 사용 | `new` 키워드와 함수 사용 |
| 용도 | 단일 객체 생성 | 여러 유사한 객체 생성 |
| 코드 재사용 | 낮음 | 높음 |
| 예시 | `const obj = { key: value }` | `const obj = new Constructor()` |

## 왜 사용하나요?

---

1. 관련된 정보를 하나로 묶기 위해
2. 코드를 깔끔하게 정리하기 위해
3. 정보를 쉽게 전달하고 사용하기 위해

실생활 예시로 이해해봅시다:

```jsx
let 학생 = {
  이름: '영희',
  나이: 9,
  좋아하는과목: '미술'
};

```

이것은 마치 '영희'라는 학생의 정보를 적은 카드와 같습니다. 이 카드(객체)에는 영희의 이름, 나이, 좋아하는 과목이 적혀 있습니다.

이렇게 객체 리터럴을 사용하면:

1. 영희의 정보를 한 눈에 볼 수 있어요.
2. 필요할 때 쉽게 정보를 꺼내 쓸 수 있어요. (예: `학생.이름`)
3. 새로운 정보를 쉽게 추가할 수 있어요. (예: `학생.학년 = 3;`)

객체 리터럴은 정보를 깔끔하게 정리하고 쉽게 사용할 수 있게 해주는 편리한 도구입니다. 마치 여러분의 필통에 연필, 지우개, 자를 넣어두는 것처럼, 관련된 정보를 하나의 '상자'에 모아두는 거예요.

# 객체 타입에 접근하기 위한 for ⇒ `for ... in`

---

→ 단순 for … in 을 하면 키 값만 출력하게 되는 오류가 있으니 유의할 것

```jsx
 //obj는 in객체 사용
for (const data in datas) { //이렇게 하면 단순 키값만 추출이 된다.
   console.log(data)
}
```

## *Proxy(Array) {0: 'Python', 1: 'JavaScript', 2: 'Ruby'}*

---

- 이 결과는 Proxy 객체로 감싸진 배열
- 겉보기에는 객체처럼 보이지만, 실제로는 배열의 특성을 가지고 있다.
1. Proxy 객체:
    - Proxy는 JavaScript의 기능으로, 다른 객체나 배열의 기본 동작을 사용자 정의 동작으로 **재정의**할 수 있게 해준다.
    - 여기서 Proxy : 배열의 동작을 수정하거나 모니터링할 수 있게 한.
2. 배열의 특성:
    - 내부적으로는 **여전히 배열 ⇒ 숫자 인덱스를 사용하여 요소에 접근**할 수 있다.
    - `length` 속성을 가지며, 배열 메서드(예: push, pop, forEach 등)를 사용할 수 있다.

# Reactive()객체와 ref 객체의 차이

---

- `reactive()`는 객체 전체를 반응형으로 만든다.
- `ref`는 단일 값을 반응형으로 만들며, `.value`로 접근해야 한다.

`reactive()` 사용 예:

```jsx
const state = reactive({ count: 0 });
console.log(state.count); // 0
state.count++; // 직접 접근 가능

```

**=> 객체의 구조를 그대로 유지하면서 내부적으로 반응성을 추가**

⇒  Proxy를 사용하여 객체의 모든 속성에 대한 접근을 가로챈다

⇒ 단 구조분해 할당시 반응성을 잃을 수 있다.

```jsx
const state = reactive({ count: 0 });
const { count } = state; // 반응성 손실

// count 변수는 이제 일반 숫자일 뿐, 반응형이 아님
count++; // 이 변경은 반응형 시스템에 감지되지 않음
```

```jsx
const state = reactive({ count: 0 });
// state.count로 접근하여 반응성 유지
```

`ref` 사용 예:

```jsx
const count = ref(0);
console.log(count.value); // 0
count.value++; // .value로 접근해야 함

```

**⇒ 값을 객체로 감싸고, 이 객체에 `value` 속성을 추가**

# forEach 메서드

---

```jsx
array.forEach(item => console.log(item));

```

- `forEach`는 배열의 각 요소에 대해 주어진 함수를 실행.
- `item => console.log(item)`은 화살표 함수로, 각 요소(`item`)를 콘솔에 출력.
- 이 코드는 배열의 모든 요소를 순회하며 각각을 콘솔에 출력

### ⚠️ 조금 더 이해하기

---

1. `forEach` 메서드:
    - 배열의 각 요소에 대해 특정 작업을 수행
    - 배열의 처음부터 끝까지 모든 요소를 순회
2. 화살표 함수:
    - 함수를 간단하게 작성하는 새로운 방법
    - `=>` 기호를 사용하여 정의

예시를 통해 설명하겠습니다:

```jsx
// 일반적인 배열
const fruits = ['사과', '바나나', '오렌지'];

// forEach를 사용하지 않은 방법
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

// forEach를 사용한 방법 (일반 함수)
fruits.forEach(function(fruit) { //나누는 것 => 요소 하나 하나씩 출력한다고 
    console.log(fruit); // 생각
});

// forEach를 사용한 방법 (화살표 함수)
fruits.forEach(fruit => console.log(fruit));

```

설명:

1. `forEach`는 배열의 각 요소에 대해 주어진 함수를 실행합니다.
2. 화살표 함수 `fruit => console.log(fruit)`는 다음과 같습니다:
    - `fruit`는 함수의 매개변수입니다 (각 배열 요소).
    - `=>` 뒤에 오는 부분은 함수의 본문입니다.
    - 이 경우, 각 `fruit`를 콘솔에 출력합니다.

이 코드는 배열의 모든 요소('사과', '바나나', '오렌지')를 순서대로 콘솔에 출력합니다.

`forEach`와 화살표 함수를 사용하면 코드를 더 간결하고 읽기 쉽게 만들 수 있습니다.

Citations:
[1] [https://robiul.dev/foreach-method-in-javascript-a-comprehensive-guide](https://robiul.dev/foreach-method-in-javascript-a-comprehensive-guide)
[2] [https://ibaslogic.com/javascript-foreach/](https://ibaslogic.com/javascript-foreach/)
[3] [https://www.freecodecamp.org/news/javascript-arrow-functions-in-depth/](https://www.freecodecamp.org/news/javascript-arrow-functions-in-depth/)
[4] [https://www.w3schools.com/jsref/jsref_foreach.asp](https://www.w3schools.com/jsref/jsref_foreach.asp)
[5] [https://www.w3schools.com/js/js_arrow_function.asp](https://www.w3schools.com/js/js_arrow_function.asp)

# ⚠️ 객체와 배열을 구분할 수 있는 메서드

---

```jsx
Array.isArray(데이터); // 배열이면 true, 아니면 false 반환

```

# 바인딩과 V-model의 역할

---

## 바인딩의 의미

---

<aside>
💡

바인딩은 Vue에서 `데이터와 DOM 요소를 연결`하는 것을 의미
즉, JavaScript의 데이터와 HTML 요소를 서로 연결하여 동기화시키는 것

</aside>

## v-model의 역할

---

<aside>
💡

v-model은 양방향 바인딩을 위한 디렉티브
⇒ 이는 폼 입력 요소나 컴포넌트에 사용되어 데이터의 **입력과 출력을 동시에 처리**

</aside>

[단방향 바인딩] ⇒ p태그의 class가 되는 ⇒ `colorClass`

```html
<p :class="colorClass">입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.</p>
```

 → **`:class`** 바인딩은 JavaScript의 **`classList.add()`**와 유사하지만, 더 강력하고 유연

[양방향 바인딩] 사용자가 입력한 `input`의 값이 `colorClass`변수에 할당되고,
                            동시에 colorClass의 값이 변경되면 input값도 업데이트 됨

```html
<input type="text" v-model="colorClass">

```

- input에서 colorClass의 값을 채워주고, 그 값이 p 태그의 class에 바인딩되어 스타일을 변경하는 것
- v-model은 **이벤트 리스너와 값 바인딩을 모두 처리하는 편리한 디렉티브**라고 볼 수 있다.

```html
  <div id="app">
    <!--class라는 속성에 바인딩 : colorClass라는 것-->
    <!--colorClass라는 class가 add된 것 -->
    <p :class="colorClass">입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.</p> <!--color가 적용됨-->
    <p>색상 목록</p>
    <ul>
      <li>red</li>
      <li>blue</li>
      <li>orange</li>
      <li>green</li>
    </ul>
    <hr>
    <p>색상 목록중 하나를 입력 해 보세요.</p>
    <!--input에 들어가는 값, 즉 value를 colorClass 속성값을 채우는 것 -->
    <input type="text" v-model="colorClass"> <!--colorClass에 담길 내용을 입력받고-->
    <!--v-model자체에 값을 입력하게 되는 것 -->
    <!--자체적으로 input값을 가지게 되는 것-->
    <!--colorClass에 있는 내용을 저 위의 p:class에 넣어준다고 이해함 -->
  </div>
```

**⇒ 한줄 요약 : v-model의 colorClass가 `키`, 그리고 input.value가 `값` 이라고 생각하면 편하다**

# 양방향 바인딩 오류 ⇒ 값이 나오지 않음 
: vue.global.js:2260 [Vue warn]: Property "colorClass" was accessed during render but is not defined on instance.

---

```jsx
  <div id="app">
    <p>입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.</p>
    <p>색상 목록</p>
    <ul>
      <li>red</li>
      <li>blue</li>
      <li>orange</li>
      <li>green</li>
    </ul>
    <hr>
    <p>색상 목록중 하나를 입력 해 보세요 : {{inputText2}}</p> <!--여기의 값: 입력창-->
    <input type="text" v-model="inputText2">
    <!-- <input type="text"> -->
  </div>
```

```jsx

    /*
      - Vue3 CDN을 사용한다.
      1. 새로운 app instance를 생성하여 아이디가 app인 container에 mount 하시오. 
      2. 사용자가 입력한 값이 colorClass 변수에 할당 될 수 있도록 양방향 바인딩 directive를 사용하시오. => 양방향 바인딩 directive
      3. colorClass 변수의 값이 첫 번째 p 태그의 class가 될 수 있도록 단방향 바인딩 directive를 사용하시오.
    */

    //양방향 바인딩 ==> directive
    const {createApp, ref} = Vue
    const newApp = createApp({
      setup() {
        const colorClass = ref('')  //const 빈값 넣고
      }
    })
    newApp.mount('#app')
```

### 출력값은 나오나 색상이 바뀌지 않음

---

- 이전에 return 값과 변수명을 잘못선언해서 문제가 되었음

<aside>
💡

**수정 사항**

</aside>

```jsx
<body>
  <div id="app">
    <p>입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.</p>
    <p>색상 목록</p>
    <ul>
      <li>red</li>
      <li>blue</li>
      <li>orange</li>
      <li>green</li>
    </ul>
    <hr>
    <!--p Tag의 클래스가 될 수 있도록?-->
    <!--단반향 바인딩-->
    <!--단반향 바인딩 방법-->
    <p :class="colorClass">색상 목록중 하나를 입력 해 보세요 : {{colorClass}}</p> <!--여기의 값: 입력창-->

    <input type="text" v-model="colorClass"> <!--값을 잘못 입력-->
    <!--colorclass 속성값을 입력했을텐데?-->
    <!--v-model의 역할-->
    <!-- <input type="text"> -->
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    /*
      - Vue3 CDN을 사용한다.
      1. 새로운 app instance를 생성하여 아이디가 app인 container에 mount 하시오. 
      2. 사용자가 입력한 값이 colorClass 변수에 할당 될 수 있도록 양방향 바인딩 directive를 사용하시오. => 양방향 바인딩 directive
      3. colorClass 변수의 값이 첫 번째 p 태그의 class가 될 수 있도록 단방향 바인딩 directive를 사용하시오.
    */

    //양방향 바인딩 ==> directive
    const {createApp, ref} = Vue
    const newApp = createApp({
      setup() {
        const colorClass = ref('')  //const 빈값 넣고 -> 여기선 단순 colorClass? 작동하는데 뭐지
        return{
          colorClass
        }
      }

    })
    newApp.mount('#app')
  </script>
```

# Vue에서 사용하는 Style 객체 이해

---

```jsx
style = {
  color: colorType,
  'font-family': fontType
}

```

- CSS 속성(키)과 그 값을 정의
- `color`와 `font-family`가 CSS 속성이고, `colorType`과 `fontType`은 각각의 값

## ⚠️ class와 Style의 차이

---

<aside>
💡

- c**lass 바인딩은 `미리 정의`된 CSS 클래스를 동적으로 적용**
- **style 바인딩은 `인라인 스타일`을 동적으로 적용**
</aside>

**[class 바인딩]!!**

```html
<p :class="{ active: isActive, 'text-danger': hasError }">

```

여기서 `active`와 `text-danger`는 클래스 이름이고, `isActive`와 `hasError`는 **불리언 값**

⇒ **class 명 / True&False**

**[style 바인딩]!!**

```html
<p :style="{ color: activeColor, fontSize: fontSize + 'px' }">

```

- 여기서 `color`와 `fontSize`는 CSS 속성이고, `activeColor`와 `fontSize`는 해당 속성의 값
- **css 속성 자체를 동적으로 설정 ⇒ 속성 / 속성값**
    - 미리 정의 된 CSS 클래스를 동적으로 적용

# vue.global.js:2260 [Vue warn]: Property "toggleDecorate" was accessed during render but is not defined on instance.
at <App>

---

- render error는 리턴값이 없다는 것

```jsx
  <div id="app">
    <h1 :class="colorCrimson">Heading</h1>
    <!--class자체에 decorate가 들어가있는지 확인-->
    <p :class="{'text-decorate' : isDecorate}">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nemo, ipsum.</p>
    <button @click="toggleDecorate">Toggle Text Style</button>
  </div>
```

```jsx
    const { createApp,ref } = Vue
    const app = createApp({ //이거의 기능이 뭔지? Q. 이 함수가 뭔지
      setup() {
        const colorCrimson = ref('text-crimson') //문자열 text-crimson
        //h1 클래스 속성 값에 바인딩 하여 폰트 컬러를 변경한다. => class 자체 => 값을 넣었으니 해당 클래스명을 전해주는 것
        const isDecorate = ref(false) //false를 가진다
        //p속성에 바인딩하여 -> text_decorate를 적용한다
        //class의 true / false를 기억해보면 : 특정 {class명 : true/false} -> 객체 모양으로 되어있다
        //Q. 이렇게 되는 이유??
        const toggleDecorate = function() { //여기는 event가 없으니까 선언해줘야 함
          if (isDecorate.value == false) {
            isDecorate.value = true
          } else {
            isDecorate.value = false
          }
        }

        return {
          colorCrimson,
          isDecorate,
        }
      }
    })
    app.mount('#app')
```

여기서 `active`와 `text-danger`는 클래스 이름이고, `isActive`와 `hasError`는 **불리언 값**

⇒ **class 명 / True&False**

## button 태그가 아니라 form 태그에 작성해야하는 이유

---

<aside>
💡

**따라서, form의 기본 제출 동작을 완전히 제어하고 싶다면 form 태그에 @submit.prevent를 사용하는 것이 더 적절**

</aside>

**[form 태그에 submit.prevent를 적용하는 경우]**

```html
<form @submit.prevent="changeStyle"> <!--form tage자체에 preventDefault를 해줌-->
  <!-- form 내용 -->
  <button type="submit">변경!</button>
</form>

```

- form 전체의 제출 이벤트를 가로채고 방지
- form 내의 모든 submit 타입 버튼이나 Enter 키 입력으로 인한 제출을 모두 방지

**[button에 submit.prevent를 적용하는 경우]**

```html
<form>
  <!-- form 내용 -->
  <button @click.prevent="changeStyle">변경!</button>
  <!-- button에 적용 : 버튼 클릭시에만 이벤트 방지 -->
</form>

```

- 해당 버튼 클릭 시에만 이벤트를 방지한다.
- 다른 submit 버튼이나 Enter 키로 인한 form 제출은 여전히 발생할 수 있다.
- 실습 진행중 느꼈던 어려움 : console.log(자체가 찍히지 않았던 문제>
    
    # console.log 자체가 찍히지 않는 문제
    → 값을 새로 할당해야하는 문제
    
    ---
    
    [html]
    
    ```jsx
      <div id="app">
        <!--style 값을 준다.-->
        <p :style="styleObject">Let's change the font style!</p> <!--참인것 실행, 아니면 미실행?-->
        <hr> <!--단반향 적용-->
        <p >색상 목록</p> 
        <ul>
          <li>red</li>
          <li>blue</li>
        </ul>
    
        <p>글꼴 목록</p>
        <ul>
          <li>fantasy</li>
          <li>cursive</li>
          <li>Impact</li>
        </ul>
        <hr>
    
        <form > <!--form 자체에-->
          <label for="color">색 입력 :</label> <!--여기에 입력함-->
          <input type="text" id="color" v-model="colorType"> <!--여기에 데이터 값을 넣을 것 : 양방향 -->
          <br>
          <label for="font">글꼴 입력 : </label> <!--여기 input -->
          <input type="text" id="font" v-model="fontType"> <!--이러한 클래스를 넣어주는 것 : 양방향 바인딩 -->
          <br>
          <button @submit.prevent="changeStyle">변경!</button>
    
        </form>
      </div>
    ```
    
    [js]
    
    ```jsx
    /*
          - Vue3 CDN을 사용한다.
          1. 새로운 app instance를 생성하여 아이디가 app인 container에 mount 하시오.
          2. 사용자가 입력한 색상 명이 colorType 변수에 할당 될 수 있도록 양방향 바인딩 directive를 사용하시오.
          3. 사용자가 입력한 글꼴 명이 fontType 변수에 할당 될 수 있도록 양방향 바인딩 directive를 사용하시오.
          */
         const {createApp, ref} = Vue
         const newApp = createApp({
           setup(){
             const colorType = ref('') // 입력한 내용 바인딩 될 것
             const fontType = ref('')
    
          //4. 첫 번째 p 태그의 style에 적용할 stlyeObject 변수를 만들고, 단방향 바인딩 directive를 사용하여 연결하시오.
          //5. 값을 모두 입력 한 후, enter를 입력하거나, `변경!` 버튼을 클릭하면, changeStyle 함수가 실행되도록 이벤트 핸들러 directive를 사용하시오.
            const styleObject = ref({}) //단방향 driective => v-bind와 v-on을 같이 사용한다
            //changeStyle => enter 
            //여기에 값이 오니까
    
            //eventTarget에 적혀있는 value의 값을 받을 것 === QQQQ . class인가요?
            const changeStyle = function(event) {
              //각각의 vlaue를 보내준다.
              styleObject.value = { //뭐일단 이렇게 만든다
                color : colorType.value, //color => 값이 있으면 참 없으면 거짓인 것처럼 되는게 스타일?
                'font-family' : fontType.value  //font-family
              }
            }
              return {
                styleObject,
                changeStyle,
                }
              }
            })
            // - 단, enter를 입력 할 때도, 버튼을 클릭 할 때도, form 태그의 기본 이벤트 동작은 중단 시켜야 한다.
            // - changeStyle 함수 내부에서 사용자가 입력한 colorType, fontType 값을 적절한 각각 'color', 'font-family' 키에 할당한 객체를 만든다.
           
    
      newApp.mount('#app')
    ```
    
    <aside>
    💡
    
    **수정 사항 ⇒ 내용 참고**
    
    </aside>
    
    문제를 해결하기 위해 몇 가지 수정이 필요해 보입니다. 다음과 같이 코드를 수정해보세요:
    
    1. `form` 태그에 `@submit.prevent` 디렉티브를 추가하여 기본 제출 동작을 방지합니다.
    2. `changeStyle` 함수를 수정하여 `styleObject`를 업데이트하고 입력 필드를 초기화합니다.
    3. `colorType`과 `fontType`을 `setup` 함수에서 반환하여 템플릿에서 사용할 수 있게 합니다.
    
    수정된 코드는 다음과 같습니다:
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      <div id="app">
        <p :style="styleObject">Let's change the font style!</p>
        <hr>
        <p>색상 목록</p>
        <ul>
          <li>red</li>
          <li>blue</li>
        </ul>
    
        <p>글꼴 목록</p>
        <ul>
          <li>fantasy</li>
          <li>cursive</li>
          <li>Impact</li>
        </ul>
        <hr>
    
        <form @submit.prevent="changeStyle">
          <label for="color">색 입력 :</label>
          <input type="text" id="color" v-model="colorType">
          <br>
          <label for="font">글꼴 입력 : </label>
          <input type="text" id="font" v-model="fontType">
          <br>
          <button type="submit">변경!</button>
        </form>
      </div>
    
      <script src="<https://unpkg.com/vue@3/dist/vue.global.js>"></script>
      <script>
        const { createApp, ref } = Vue
        const newApp = createApp({
          setup() {
            const colorType = ref('')
            const fontType = ref('')
            const styleObject = ref({})
    
            const changeStyle = function() {
              styleObject.value = {
                color: colorType.value,
                'font-family': fontType.value
              }
              // 입력 필드 초기화
              colorType.value = ''
              fontType.value = ''
            }
    
            return {
              styleObject,
              changeStyle,
              colorType,
              fontType
            }
          }
        })
    
        newApp.mount('#app')
      </script>
    </body>
    </html>
    
    ```
    
    주요 변경 사항:
    
    1. `<form>` 태그에 `@submit.prevent="changeStyle"`를 추가하여 기본 제출 동작을 방지하고 `changeStyle` 함수를 호출합니다.
    2. `changeStyle` 함수에서 `event` 매개변수를 제거하고, `styleObject`를 직접 업데이트합니다.
    3. `changeStyle` 함수 내에서 `colorType`과 `fontType`을 빈 문자열로 초기화합니다.
    4. `setup` 함수에서 `colorType`과 `fontType`을 반환하여 템플릿에서 사용할 수 있게 합니다.
    
    이제 폼을 제출하면 (엔터를 누르거나 "변경!" 버튼을 클릭) `changeStyle` 함수가 실행되어 스타일이 변경되고 입력 필드가 초기화될 것입니다.
    

## V-model이란?

---

<aside>
💡

 **v-model은 `바인딩과 이벤트 처리`를 결합한 디렉티브**

</aside>

| 특징 | 설명 | 예시 |
| --- | --- | --- |
| **양방향 바인딩** | 데이터와 UI 요소 간 양방향 동기화 | `<input v-model="message">` |
| **데이터 바인딩** | Vue 인스턴스의 데이터를 입력 요소에 바인딩 | `message` 데이터가 **input에 표시됨** |
| **이벤트 처리** | **입력 요소의 변경을 감지하여** 
데이터 업데이트 | 사용자 입력 시 `message` 자동 업데이트 |
| 간편한 사용 | v-bind와 v-on을 별도로 
지정할 필요 없음 | v-model 하나로 양방향 바인딩 구현 |
| 다양한 입력 요소 지원 | 여러 HTML 입력 요소에 사용 
가능 | input, textarea, select, checkbox 등 |
| 수식어 제공 | 추가 기능을 위한 수식어 
사용 가능 | `v-model.lazy`, `v-model.number`, `v-model.trim` |
| 컴포넌트 사용 | 사용자 정의 컴포넌트에도 
적용 가능 | `<custom-input v-model="searchText">` |

## function event 와 function을 이해하기

---

⇒ **v-model로 바인딩을 했기 때문에 추가적인 event 및 동작방지**가 필요없음

| 항목 | 설명 | 예시 |
| --- | --- | --- |
| `changeStyle` 함수 | **이벤트 객체 불필요, `v-model`로 이미 값 바인딩** | `const changeStyle = function() { ... }` |
| `styleObject.value` | **`ref`로 생성된 반응형 변수 
접근 방법** | `styleObject.value = { color: '...', 'font-family': '...' }` |
| 객체로 스타일 지정 | CSS 속성-값 쌍을 자바스크립트 객체로 표현 | `{ color: colorType.value, 'font-family': fontType.value }` |
| Vue의 스타일 바인딩 | 자바스크립트 객체를 CSS 스타일로 변환 | `:style="styleObject"` |
| 스타일 적용 결과 | Vue가 객체를 인라인 스타일로 변환 | `<p style="color: red; font-family: Arial;">...</p>` |

## 객체로 값을 넣는 이유

---

`styleObject.value`에 객체를 할당하는 이유는 다음과 같습니다:

- HTML 요소의 스타일은 **CSS 속성-값 쌍의 집합!!**
    - 이를 자바스크립트에서 표현할 때 객체 형태가 가장 적합
- Vue의 `:style` 바인딩은 자바스크립트 객체를 CSS 스타일로 변환
    - 각 객체의 키는 CSS 속성명이 되고, 값은 해당 속성의 값이 된다.

```html
<p style="color: red; font-family: Arial;">Let's change the font style!</p>
```

- Vue는 `styleObject.value`의 변경을 감지한다.
- 감지된 변경사항에 따라 Vue는 관련 컴포넌트를 다시 렌더링한다.
- 렌더링 과정에서 Vue는 `styleObject`의 내용을 해당 HTML 요소의 인라인 스타일로 적용

# Vue.js의 클래스 바인딩

---

- Vue.js에서 클래스를 동적으로 바인딩할 때 `{클래스명: 조건}` 형태의 객체를 사용하는 것은 Vue의 특징

```jsx
<p :class="{ 'text-decorate': isDecorate }">
```

⇒ 이 코드는 `isDecorate`가 `true`일 때만 `text-decorate` 클래스를 적용

# 이벤트 핸들러와 event 매개변수

---

- `@click="toggleDecorate"`와 같은 이벤트 핸들러에서는 `event` 객체가 자동으로 전달해준다
    - 따라서 함수 정의에서 `event` 매개변수를 명시적으로 선언하지 않아도 된다.
    - Vue.js에서 `@click`은 `v-on:click`의 축약형이며, 클릭 이벤트를 처리하는 이벤트 핸들러

### click과 v-on:click

---

<aside>
💡

- 기본적으로 이벤트 매개변수를 명시적으로 전달하지 않아도 된다.
- **Vue는 `자동`으로 네이티브 DOM `이벤트 객체를 첫 번째 인자`로 메서드에 전달**
</aside>

- `@click`은 `v-on:click`의 축약형
- 둘 다 동일한 기능을 수행하며, `요소에 클릭 이벤트 리스너를 추가`

**[이벤트 객체 사용]**

<aside>
💡

이렇게 `$event`를 사용하면 이벤트 처리의 유연성을 높이고, 코드의 의도를 더 명확하게 표현할 수 있다. 특히 추가 인자를 전달하거나 인라인 핸들러에서 이벤트 객체에 접근해야 할 때 유용
**⇒ `이벤트 제어`**

</aside>

- 메서드 내에서 이벤트 객체를 사용하려면, 메서드 정의에 매개변수를 추가하면 된다.

```jsx
methods: {
  handleClick(event) {
    console.log(event); // 이벤트 객체에 접근 가능
  }
}
```

- Vue 컴포넌트에서는 **`methods`** 옵션을 사용하여 메서드를 정의
- **`handleClick`**은 메서드의 이름
- **`event`** 매개변수는 클릭 이벤트 객체를 받는다.
- 이 메서드 내에서 **`event`** 객체를 사용하여 이벤트 정보에 접근

**[명시적으로 이벤트 객체 전달]**

- `$event`를 사용하여 명시적으로 이벤트 객체를 전달할 수 있다.

```html
<button @click="handleClick($event)">클릭</button>

```

⇒ 명시적으로 전달하는 이유들??

1. 메서드에 추가 인자 전달:
이벤트 핸들러 메서드에 사용자 정의 인자와 함께 **이벤트 객체를 전달하고 싶을 때** 사용
    
    ⇒ `이벤트` 가 발생한 `컨텍스트`에 대한 추가 정보 전달 가능 ex) x가 클릭됨, 위치 y
    

```html
<button @click="handleClick('Hello', $event)">클릭</button>

```

```jsx
methods: {
  handleClick(message, event) {
    console.log(message, event);
  }
}

```

1. 인라인 핸들러에서 이벤트 객체 사용:
템플릿에서 **직접 이벤트 객체에 접근**해야 할 때 유용하다.

```html
<button @click="console.log($event.target)">클릭</button>

```

⇒ 폼의 기본 동작을 막기, 이벤트 전파 제어, 이벤트 처리

**[추가 인자와 함께 사용]**

- 다른 인자와 함께 이벤트 객체를 전달할 수 있다.

```html
<button @click="handleClick('hello', $event)">클릭</button>

```

**[인라인 핸들러]**

- 간단한 작업의 경우 인라인으로 직접 처리할 수 있다[5].

```html
<button @click="count++">증가</button>

```

# 참/거짓에 따라 특정 클래스 속성이 나타나도록

---

<aside>
💡

**Vue의 반응성 시스템과 결합하여, 데이터 변경에 따라 UI를 자동으로 업데이트할 수 있게 해준다.
⇒ `선언적 프로그래밍 방식`으로, "어떤 상태일 때 어떤 클래스를 적용한다"라고 선언하는 것과 같다.**

</aside>

```jsx
  <div id="app">
    <!--class추가한다-->
    <!--지금 일단 반영 안됨-->
    <h1 :class="colorCrimson">Heading</h1> <!--text바인딩하여 폰트 컬러 변경-->

    <!--isDecorate가 true이면 color 값이 나오도록 해야함 => textDecorate-->
    <!--참/거짓에 따라 text-decorate 클래스 선택자를 적용한다-->
    <!--isActive파트보고 : 이게 참이면 나오도록 한다 
        키 : 속성 / 값-->
    <p :class="{'text-decorate': isDecorate}">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nemo, ipsum.</p>
    
    <!--toggleDecorate 실행-->
    <!-- 이벤트 활성화 : 어떤 함수를 부를 것인지?? -->
    <button @click="toggleDecorate">Toggle Text Style</button> <!-- @click="toggleDecorate"-->
  </div>
```

| 개념 | 설명 | 예시 |
| --- | --- | --- |
| **클래스 바인딩** | Vue에서 동적으로 클래스를 적용하는 방법 | `:class="{'text-decorate': isDecorate}"` |
| **객체 구문** | **클래스 바인딩에 사용되는 구문** | `{'클래스명': 조건}` |
| 이벤트 핸들링 | 사용자 상호작용에 반응하는 방법 | `@click="toggleDecorate"`  |
- `{'text-decorate': isDecorate} :`
    - 'text-decorate'는 적용할 클래스 이름
    - isDecorate는 이 클래스를 적용할지 결정하는 조건(boolean 값)
- `@click="toggleDecorate"`는 버튼 클릭 시 toggleDecorate 메서드를 실행
- toggleDecorate 메서드는 isDecorate 값을 토글(true ↔ false)할 것으로 예상

| 개념 | 비유 | 설명 | 예시 |
| --- | --- | --- | --- |
| **클래스 바인딩** | 스마트 옷장 | 상황에 따라 **자동으로 옷(클래스)을 선택**하고 입힘 | `:class="{ active: isActive }"` |
| **`객체 구문`** | 옷장의 **규칙 설정** | 어떤 상황에 어떤 옷을 입을지 정의 | `{ 'text-danger': hasError }` |
| **조건부 클래스** | 날씨 센서 | 특정 조건(날씨)에 따라 옷(클래스)을 선택 | `{ 'winter-coat': temperature < 0 }` |
| **다중 클래스 바인딩** | **여러 센서 조합** | **여러 조건을 고려**해 옷(클래스) 조합 결정 | `{ active: isActive, 'text-danger': hasError }` |
| **배열 구문** | 옷 세트 선택 | **미리 정의된 여러 옷(클래스) 세트 중** 선택 | `:class="[activeClass, errorClass]"` |
| 컴포넌트와 클래스 바인딩 | 기본 옷에 액세서리 추가 | 기존 스타일에 새로운 스타일 추가 | `<MyComponent class="extra-style" />` |

## 클래스를 객체에 전달하는 방식, 리스트에 전달하는 방식
⇒ 이유?

---

| 특성 | 객체 방식 | 리스트 방식 |
| --- | --- | --- |
| 구문 | `:class="{ active: isActive, 'text-danger': hasError }"` | `:class="[activeClass, errorClass]"` |
| 주요 용도 | **조건부 클래스 적용** | **여러 클래스 단순 나열** |
| 장점 | - **`개별` 클래스 토글 가능
- `조건`에 따른 동적 적용** | - 간단한 클래스 나열
- 동적/정적 클래스 혼합 용이 |
| 사용 시나리오 | - 특정 조건에 따른 클래스 적용
- **여러 독립적 조건 처리** | - **무조건 적용할 여러 클래스**
- 동적으로 결정되는 클래스명 |
| 예시 상황 | 사용자 상호작용에 따른 UI 변경 | 테마 또는 스타일 세트 적용 |
| 유연성 | 높음 (조건부 로직) | 중간 (단순 나열) |
| 가독성 | 조건이 많을 경우 복잡해질 수 있음 | **간단하고 직관적** |
| 조합 사용 | `:class="[{ active: isActive }, errorClass]"` |  |

### vue.js에서 객체를 나누어 적용하고 별도로 적용할 수 있게 하는 이유

---

### 별도로 적용할 수 있게 하는 이유:

- 유연성: 컴포넌트의 다양한 측면을 독립적으로 관리할 수 있다.
- 재사용성: 특정 기능을 다른 컴포넌트에서 쉽게 재사용할 수 있다.
- 테스트 용이성: 각 부분을 독립적으로 테스트할 수 있다.

### 객체에 기능이나 함수를 적용할 수 있는 이유:

- 캡슐화: 데이터와 그 데이터를 조작하는 메서드를 함께 묶어 관리할 수 있다.
- 반응성: Vue의 반응성 시스템과 통합되어 데이터 변경 시 자동으로 UI를 업데이트한다.
- 컨텍스트 유지: 'this'를 통해 컴포넌트의 다른 속성에 쉽게 접근할 수 있다.

```jsx
export default {
  data() {
    return {
      count: 0
    }
  },
  methods: {
    increment() {
      this.count++
    }
  },
  computed: {
    doubleCount() {
      return this.count * 2
    }
  }
}

```
