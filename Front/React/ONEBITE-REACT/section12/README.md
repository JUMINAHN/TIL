# [React] Inflearn 감정 일기장 PJT

날짜: 2024년 12월 4일

# [궁금한 점]

---

## 1. Router 관련 Vue와 React

- Vue의 index.js와 React Router의 기능은 유사합니다.
- React에서는 react-router-dom 라이브러리를 설치하여 라우팅 기능을 추가합니다.
- Vue Router는 Vue.js의 공식 라우터이지만, React Router는 별도의 라이브러리입니다.

## 2. Vue의 view, React의 pages

- Vue의 View 컴포넌트와 React의 pages 폴더는 비슷한 역할을 합니다.
- 둘 다 라우트에 매칭되는 컴포넌트를 정의합니다. React에서는 주로 pages 폴더를 사용하여 라우트 컴포넌트를 구성합니다.

## 3. React의 Link 컴포넌트와 Vue의 router-link와 유사점

- React의 Link 컴포넌트와 Vue의 router-link은 유사한 역할을 합니다.
- a 태그를 사용하지 않는 이유는 페이지 전체를 새로고침하지 않고 SPA의 장점을 유지하기 위함입니다.
- React에서는 `컴포넌트를 더 작은 단위로 나누는 경향이 있어, 라우팅 관련 기능들이 분리`되어 있습니다. 이는 재사용성과 유지보수성을 높이지만, 때로는 반복적인 코드를 작성해야 할 수 있습니다.

## 4. React Hooks

- (use로 시작하는 함수들)는 함수형 컴포넌트에서 상태 관리와 생명주기 기능을 사용할 수 있게 해주는 기능입니다.
- Vue는 주로 문자열 보간법({{ }})을 사용하고, React는 JSX 내에서 JavaScript 표현식을 {}로 감싸 사용합니다.

### 4-1. React Hooks 종류 및 기능

| Hook 이름 | 주요 기능 | 사용 예시 | 장점 |
| --- | --- | --- | --- |
| useState | 상태 관리 | `const [count, setCount] = useState(0)` | 간단한 상태 생성 및 업데이트 |
| useEffect | 생명주기 관리 | `useEffect(() => { ... }, [dependency])` | 렌더링 후 실행, 
**사이드 이펙트 처리** |
| useContext | 전역 상태 관리 | `const value = useContext(MyContext)` | 깊은 **컴포넌트 트리**에서 
데이터 전달 |
| useRef | DOM 참조/값 저장 | `const inputRef = useRef(null)` | 변경해도 렌더링 트리거 안함 |
| useReducer | 복잡한 상태 관리 | `const [state, dispatch] = useReducer(reducer, initialState)` | **상태 로직 중앙집중화** |
| useMemo | 메모이제이션 | `const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b])` | **성능 최적화** |
| useCallback | 함수 메모이제이션 | `const memoizedCallback = useCallback(() => { doSomething(a, b) }, [a, b])` | **불필요한 렌더링 방지** |

### 4-2. Hooks 사용 이유

1. 코드 간결성
2. 로직 재사용성
3. 함수형 프로그래밍 지향
4. 상태 관리 용이
5. 성능 최적화

## 5. ?value=hello

- 쿼리 파라미터를 나타냅니다. **'value'라는 키에 'hello'라는 값이 할당**된 것입니다.
- 쿼리스트링(또는 searchString)을 Home 컴포넌트에서 처리하는 것은 설계 선택의 문제입니다. 메인 페이지에서 검색 기능을 제공하는 경우처럼, 특정 컴포넌트에서 쿼리 파라미터를 처리하는 것이 적절할 수 있습니다.
- 네이버 메인 페이지의 검색 기능처럼, 사용자 인터페이스의 요구사항에 따라 쿼리 파라미터 처리 위치가 결정됩니다.

# [오류] border : none의 오류 + 상위 - 하위 css

---

CSS의 계단식 적용(Cascading) 원리에 따라 `하위 클래스의 스타일이 상위 클래스의 스타일을 덮어쓰는 것`은 맞습니다. 그러나 `브라우저의 기본 스타일이나 포커스 상태의 스타일이 더 높은 우선순위`를 가질 수 있어 이를 무시하기 위해서는 위와 같은 추가적인 속성들이 필요할 수 있습니다.

[수정 전]

```jsx
const Button = ({text, type, onClick}) => {
  return (
    <button onClick={onClick}
    className={`Button_${type}`}>{text}</button>
    // Button에 타입 명시
  )
}

export default Button
```

<aside>
💡

수정 후

</aside>

```jsx
import './Button.css'

//부모 컴포넌트 props에 따라서 다 다르게 동작하도록 만들어주기
// type은 각 버튼마다 색깔이 다르니까 => text 글자, type 색깔, onClick 어디에 onCLick 이벤트를 걸건지
// type별로 다르게 => butoonTag의 className 'Button'에서 변경
const Button = ({text, type, onClick}) => {
  return (
    <button onClick={onClick}
    className={`Button Button_${type}`}>{text}</button>
    // Button에 타입 명시
  )
}

export default Button
```

`className={`Button Button_${type}`}`와 같이 작성하는 이유는 다음과 같습니다:

1. 기본 스타일 적용: 'Button' 클래스는 **모든 버튼에 공통으로 적용될 기본 스타일을 정의합니다**.
2. 타입별 스타일 추가: `Button_${type}`는 버튼의 특정 타입(예: POSITIVE, NEGATIVE)에 따른 **추가 스타일을 적용합니다[5].**
3. CSS 특이도(Specificity) 활용: 이 방식은 CSS 특이도를 효과적으로 사용합니다. 'Button' 클래스의 스타일은 모든 버튼에 적용되고, `Button_${type}` 클래스는 **더 높은 특이도를 가져 타입별 스타일을 오버라이드할 수 있습니다**.
4. 유지보수성 향상: 공통 스타일과 특정 스타일을 분리함으로써 코드의 유지보수가 용이해집니다.
5. 재사용성: 이 구조를 사용하면 다양한 타입의 버튼을 쉽게 생성하고 관리할 수 있습니다.

이렇게 함으로써 버튼의 기본 스타일과 타입별 스타일을 효과적으로 관리하고 적용할 수 있습니다.

# [CSS 궁금증]

---

```jsx
.Header {
  display: flex;
  align-items: center;
  /* align-items는 열 기준으로 */
  padding : 20px 0px;
  border-bottom: 1px solid rgb(226, 226, 226);
}

.Header > div {
  display: flex;
}

.Header .header_center {
  width: 50%;
  font-size: 25px;
  justify-content: center;
  /* 자식들이 배치하는 것을 가운데 : justify-content : 이안에선 어떻게? */
} 

.Header .header_left {
  width: 25%;
  justify-content: flex-start;
}

.Header .header_right {
  width: 25%;
  justify-content: flex-end;
} 
```

1. `align-items: center;`
    - 이는 flex container의 교차축(cross axis)을 기준으로 항목들을 정렬합니다.
    - 여기서는 수직 방향으로 중앙 정렬됩니다.
2. `.Header > div { display: flex; }`
    - 이 스타일은 .Header의 직계 자식 div에 적용됩니다.
    - 버튼만 있더라도, 이 div를 flex container로 만들어 내부 요소(버튼)의 배치를 제어할 수 있게 합니다.
3. `.Header .header_center`
    - **이는 .Header 내부의 .header_center 클래스를 가진 요소를 선택합니다.**
    - 반드시 직계 자식일 필요는 없으며, .Header 내의 모든 .header_center에 적용됩니다.
4. `justify-content: center;`
    - flex container의 주축(main axis)을 따라 내용을 정렬합니다.
    - 여기서는 수평 방향으로 중앙 정렬됩니다.

추가 설명:

- **`justify-content`는 flex container 내부의 항목들을 주축을 따라 정렬합니다.**
- `flex-start`는 시작점에, `center`는 중앙에, `flex-end`는 끝점에 정렬합니다.
- 이 속성들은 flex container에 적용되어 그 안의 자식 요소들의 배치를 제어합니다.

## div 내부에 btn : justify-content 동작?

---

```
[Header 전체 레이아웃]
┌───────────────────────────────────────────┐
│ [Left]         [Center Title]      [Right]│
│┌─────┐                             ┌─────┐│
││[Btn]│        "Page Title"         │[Btn]││
│└─────┘                             └─────┘│
└───────────────────────────────────────────┘

[Left Area - justify-content: flex-start]
┌─────────┐
│ [Button]│
└─────────┘

[Right Area - justify-content: flex-end]
┌─────────┐
│         [Button]│
└─────────┘

```

`justify-content`는 flex container 내부의 flex items를 주축(main axis)을 따라 정렬합니다[1]. 각 영역(Left, Center, Right)이 flex container이고, 버튼은 그 안의 flex item입니다[6].

- Left Area: `justify-content: flex-start`로 설정되어 버튼이 왼쪽에 정렬됩니다.
- Right Area: `justify-content: flex-end`로 설정되어 버튼이 오른쪽에 정렬됩니다.
- Center Area: 텍스트만 있으므로 `justify-content: center`로 중앙 정렬됩니다.

이렇게 `justify-content`는 각 영역 내에서 버튼(또는 내용)의 수평 위치를 제어합니다.

## header_center만 본다면?

---

```
[header_center - justify-content: center]
┌───────────────────────────┐
│        "Page Title"       │
└───────────────────────────┘

```

header_center div의 경우:

1. div 자체가 flex container입니다.
2. 내부에는 텍스트 콘텐츠("Page Title")만 있습니다.
3. justify-content: center;가 적용되어 있습니다.

이 경우, 텍스트 콘텐츠는 flex item으로 취급되어 div의 중앙에 위치하게 됩니다. 텍스트가 여러 단어로 구성되어 있더라도, 이 `텍스트 블록 전체가 중앙에 정렬`됩니다.

버튼이 들어있는 leftChild와 rightChild의 경우와는 다르게, header_center에는 버튼이 아닌 텍스트만 있습니다. 그래서 이 텍스트가 flex item의 역할을 하여 justify-content: center;에 의해 중앙 정렬되는 것입니다[.

# [에러] Provider 미작성으로 인한 에러

---

## **1. Context 렌더링 오류**

```
Warning: Rendering <Context> directly is not supported and will be removed in a future major release. Did you mean to render <Context.Consumer> instead?

```

이 오류는 Context를 직접 렌더링하려고 시도했을 때 발생합니다. Context.Consumer를 사용해야 합니다.

## 2. **Context Consumer** 사용 오류

```
Warning: A context consumer was rendered with multiple children, or a child that isn't a function. A context consumer expects a single child that is a function.

```

Context Consumer는 단일 함수 자식만을 허용합니다. 여러 자식 요소를 가지고 있거나, 함수가 아닌 자식을 가지고 있어 발생한 오류입니다.

## 3. **렌더링** 함수 오류

```
Uncaught TypeError: render2 is not a function

```

**Context Consumer**에 전달된 렌더링 함수가 올바르지 않거나 누락되었습니다.

## 4. 에러 경계 권장 사항

```
Consider adding an error boundary to your tree to customize error handling behavior.

```

React는 에러 처리를 위해 에러 경계(Error Boundary) 사용을 권장하고 있습니다.

이 오류들은 주로 Context API의 잘못된 사용이나 렌더링 함수의 문제로 인해 발생했습니다. App.jsx 파일의 52번째 줄 근처를 중점적으로 검토하고, Context의 올바른 사용법을 적용하면 해결할 수 있을 것입니다.

# [프로젝트 구조에 대한 궁금증]

---

## 1. @font-face

- 웹 폰트를 정의하고 로드하는 CSS 규칙입니다. 사용자의 `시스템에 설치되지 않은 폰트`를 웹 페이지에서 사용할 수 있게 해줍니다.

## 2. public과 assets 폴더

- 모두 정적 파일을 저장하는 데 사용됩니다. **public 폴더의 파일은 빌드 시 그대로 복사**되며, assets 폴더의 파일은 일반적으로 번들링 과정을 거칩니다.

## 3. app.css / index.css

- 특정 컴포넌트나 `앱전체의 스타일을 정의`하는 데 사용되고, `index.css는 전역 스타일`이나 리셋 스타일을 정의하는 데 주로 사용됩니다.

## 4. CSS - html

- 문서의 루트 요소
- 모든 다른 요소는 이 안에 포함됩니다. `body는 html의 자식 요소로`, 웹 페이지의 주요 콘텐츠를 포함합니다.

## 5. white-space

- CSS 속성은 `요소 내의 공백 처리 방법`을 지정합니다. 예를 들어, 줄 바꿈이나 공백 처리 방식을 제어할 수 있습니다.

## 6. className에 중괄호 {}를 사용하는 이유

- JSX 내에서 JavaScript 표현식을 삽입하기 위해서입니다.
- 여기서는 문자열 템플릿을 사용하여 `동적으로 클래스 이름을 생성`하고 있습니다.

## 7. DiaryItem 컴포넌트에서 div로 나누는 이유

- 각 섹션(이미지, 정보, 버튼)을 논리적으로 구분하고 스타일링을 쉽게 하기 위함입니다.
- 이는 컴포넌트의 구조와 스타일링 요구사항에 따라 다르게 적용될 수 있습니다. 버튼을 div 안에 넣는 것은 레이아웃 조정이나 추가적인 스타일링을 위한 것일 수 있습니다.

### 7-1. div내부의 button, 그리고 일반 button만 있을때의 차이

1. div 안에 div를 만드는 것과 바로 div를 만드는 것의 차이:

이것은 마치 상자 안에 작은 상자를 넣는 것과 비슷합니다.

큰 상자만 사용할 때:

```
┌─────────────────┐
│                 │
│     내용물      │
│                 │
└─────────────────┘

```

상자 안에 작은 상자를 넣을 때:

```
┌─────────────────┐
│ ┌───────────┐   │
│ │  내용물   │   │
│ └───────────┘   │
└─────────────────┘

```

1. div 안에 button을 넣는 것과 button만 넣는 것의 차이:

이것은 마치 버튼을 그냥 놓는 것과 버튼을 상자 안에 넣는 것의 차이와 같습니다.

버튼만 있을 때:

```
   ┌───────┐
   │ 버튼  │
   └───────┘

```

div 안에 버튼을 넣을 때:

```
┌─────────────────┐
│   ┌───────┐     │
│   │ 버튼  │     │
│   └───────┘     │
└─────────────────┘

```

div 안에 버튼을 넣으면:

1. **버튼 주변에 여유 공간을 만들 수 있어요.**
2. **버튼의 위치를 더 쉽게 조절할 수 있어요.**
3. 버튼 주변에 다른 요소들을 추가하기 쉬워져요.

이렇게 하면 웹 페이지를 더 예쁘고 정돈되게 만들 수 있답니다!

# [궁금한점] Home.jsx

---

## 1. getMonthlyData 함수를 Home 컴포넌트 밖에서 정의하는 이유

---

- 성능 최적화: 컴포넌트 외부에 정의하면 **리렌더링 시 함수가 재생성되지 않습니다.**
- 재사용성: 다른 컴포넌트에서도 사용할 수 있습니다.
- 가독성: 컴포넌트 로직과 분리되어 코드가 더 깔끔해집니다.

```jsx
const getMonthlyData = (pivotDate, data) => { //오늘 날짜, 일기 데이터(날짜)
  
  const beginTime = new Date(
    pivotDate.getFullYear(),
    pivotDate.getMonth(),
    1, //1일 기준
    0,
    0,
    0
  ).getTime() //timestamp

  const endTime = new Date(
    pivotDate.getFullYear(),
    pivotDate.getMonth() + 1, //다음달
    0, //0으로 설정했을때(0일) => 마지막 날로 된다.
    23,
    59,
    59
  ).getTime()
  // 생성 날짜 범으; 확인
  // console.log(beginTime, 'beginTime');
  // console.log(endTime, 'endTime');

  //Q?여기 보면 filter에 또 
  return data.filter((item) => beginTime <= item.createdData && item.createdData <= endTime)
  
  //하기와 뭔차이 QQ?? 
  // const filteredData = data.filter((item) => {
  //   console.log(item.createdDate, 'item.createdDate');
  //   return beginTime <= item.createdDate && item.createdDate <= endTime;
  // });
  // console.log(filteredData, 'filteredData');
  // return filteredData;
}

// 일기 내용을 data로 받아와야 함
// 달력에 맞는 값 출력을 위해서
const Home = () => {
```

## 2. filter 메소드 사용 차이

---

- 두 방식은 기능적으로 동일합니다. 주석 처리된 버전은 디버깅을 위해 로그를 추가한 것입니다. 간단한 경우 한 줄로 작성하는 것이 더 간결합니다.

```jsx
  return data.filter((item) => beginTime <= item.createdData && item.createdData <= endTime)
  
  //하기와 뭔차이 QQ?? 
  const filteredData = data.filter((item) => {
     console.log(item.createdDate, 'item.createdDate');
     return beginTime <= item.createdDate && item.createdDate <= endTime;
  });
  console.log(filteredData, 'filteredData');
  return filteredData;
```

### 2-1. {}와 ()의 차이

---

1. `() =>` 단일 표현식 반환:

```jsx
(item) => beginTime <= item.createdData && item.createdData <= endTime

```

- 한 줄로 된 표현식은 자동으로 반환됩니다
- return 문이 필요 없습니다
- **간단한 연산**에 적합합니다

1. `() => {}` 함수 블록:

```jsx
(item) => {
    console.log(item.createdDate);
    return beginTime <= item.createdDate && item.createdDate <= endTime;
}

```

- 여러 줄의 코드를 실행할 수 있습니다
- 명시적으로 `return`이 필요합니다
- 디버깅이나 추가 로직이 필요할 때 사용합니다

**즉, 단순 반환만 필요한 경우는 `()` 를 사용하고, 추가 로직이나 디버깅이 필요한 경우 `{}` 를 사용합니다.**

# 3. monthlyData 계산

---

- getMonthlyData 함수를 사용하여 현재 선택된 월(pivotDate)에 해당하는 일기 데이터만 필터링합니다.

## 4. 월 증가/감소 시 년도 자동 변경

---

```jsx
  const onIncreaseMonth = () => {
    //새로운 값을 줘야하니까 => 근데 기준이 지금 가지고 있는 년 기준
    // Q. 어떻게 월이 바뀌고 년도 자동으로 바뀜?
    setPivotDate(new Date(pivotDate.getFullYear(), pivotDate.getMonth() + 1))
  }

  const onDecreaseMonth = () => {
    setPivotDate(new Date(pivotDate.getFullYear(), pivotDate.getMonth() - 1))
  }
```

- JavaScript의 Date `객체가 자동으로 처리`합니다. 예를 들어, 12월에서 1을 더하면 다음 해 1월로 자동 변경됩니다. 주의: 코드에서 'createdData'를 'createdDate'로 수정해야 할 수 있습니다. 데이터 구조에 맞는 정확한 속성 이름을 사용해야 합니다.

### 4-1. JS의 Date 객체 사용법과 자동 날짜 계산

---

### Date 객체의 주요 메서드

| 메서드 | 설명 | 예시 |
| --- | --- | --- |
| get**FullYear()** | 연도 반환 | `date.getFullYear()` → 2024 |
| getMonth() | 월 반환 (0-11) | `date.getMonth()` → 11 (12월) |
| getDate() | 일 반환 (1-31) | `date.getDate()` → 4 |
| **getTime()** | **타임스탬프 반환** | `date.getTime()` → 1733317318000 |

### 날짜 자동 계산 예시

```jsx
// 12월에서 1월로 자동 변경
const date = new Date(2024, 11, 1) // 2024년 12월 1일
const nextMonth = new Date(2024, 12, 1) // 2025년 1월 1일

// 1월에서 12월로 자동 변경
const date2 = new Date(2024, 0, 1) // 2024년 1월 1일
const prevMonth = new Date(2024, -1, 1) // 2023년 12월 1일

```

### 날짜 자동 변환 원리

**JavaScript의 Date 객체는 월이나 일이 범위를 벗어나면 자동으로 조정합니다:**

- 월이 12를 초과하면 → 연도가 증가
- 월이 0 미만이면 → 연도가 감소
- 일이 해당 월의 마지막 날을 초과하면 → 다음 달로 자동 이동

이러한 특성 때문에 `pivotDate.getMonth() + 1` 또는 `pivotDate.getMonth() - 1`과 같은 연산이 자연스럽게 연도 변경까지 처리할 수 있습니다.

### 4-2. 타임스탬프에서 날짜 반환

---

### 기본 변환 방법

```jsx
const timestamp = 1733317318000;
const date = new Date(timestamp);

// 년/월/일 형식
date.toLocaleDateString()  // "2024. 12. 4."

// 개별 값 추출
const year = date.getFullYear()    // 2024
const month = date.getMonth() + 1  // 12 (0부터 시작하므로 +1)
const day = date.getDate()         // 4

```

### 4-2-1. new Date() 알아보기

---

1. `date.toLocaleDateString()`는 Date **객체의 날짜를 사용자의 지역 설정에 맞는 문자열로 변환**하는 메서드입니다. 한국의 경우 "2024. 12. 4." 형식으로 출력됩니다.
2. `new Date()`를 사용하는 이유:
- **JavaScript에서 날짜는 불변(immutable) 객체입니다.**
- **날짜 연산이나 변경이 필요할 때마다 새로운 Date 객체를 생성해야 합니다.**
- 기존 날짜 객체를 수정할 수 없기 때문에 새로운 객체를 만들어야 합니다.
1. `new Date()` 초기값 설정:
- **매개변수 없이 사용: 현재 시간으로 설정됩니다.**
- 매개변수 있는 경우:
    
    ```jsx
    new Date(2024, 11, 4)  // 2024년 12월 4일
    new Date("2024-12-04") // 2024년 12월 4일
    new Date(1733317318000) // 타임스탬프로 설정
    
    ```
    
- 즉, 매개변수를 통해 원하는 날짜로 초기화할 수 있습니다.

### 커스텀 포맷팅

```jsx
// Intl.DateTimeFormat 사용
const formatter = new Intl.DateTimeFormat('ko-KR', {
  year: 'numeric',
  month: '2-digit',
  day: '2-digit'
});
formatter.format(new Date(timestamp))  // "2024. 12. 04."

// 수동 포맷팅
const formatDate = (timestamp) => {
  const date = new Date(timestamp);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}.${month}.${day}`;
}

```

## 시간 포함 포맷팅

```jsx
// 전체 날짜와 시간
date.toLocaleString()  // "2024. 12. 4. 오후 10:00:00"

// ISO 문자열 형식
date.toISOString()  // "2024-12-04T13:00:00.000Z"

```

## 5. 17232…로 나오는 이유 ⇒ 2024.12.04로 나오지 않는 이유

---

```jsx
//DiaryItem 의 요소를 createData로만 표기함
{new Date(createdData).toLocaleDateString()} 

```

## 6. sortedData = getSortedDate()를 사용한 이유

---

`sortedData = getSortedDate()`를 사용하는 이유는 다음과 같습니다:

1. 성능 최적화: 정렬된 데이터를 변수에 저장함으로써, 컴포넌트가 **리렌더링될 때마다 정렬 연산을 반복하지 않아도 됩니다.**
2. 재사용성: 정렬된 데이터를 여러 곳에서 사용해야 할 경우, 매번 정렬 함수를 호출하지 않고 저장된 값을 사용할 수 있습니다.
3. 가독성: JSX에서 직접 `getSortedDate()`를 호출하는 대신, 의미가 명확한 변수명을 사용함으로써 코드의 가독성이 향상됩니다.

예를 들어, 다음과 같이 map 함수에서 사용됩니다:

```jsx
{sortedData.map((item) => <DiaryItem key={item.id} {...item}/>)}

```

## 7. …{item} ⇒ 키 없이 그냥 단순히 보내도 되는가?

---

`{...item}`은 spread 연산자를 사용하여 item 객체의 **모든 속성을 펼쳐서 DiaryItem 컴포넌트의 props로 전달하는 것을 의미**합니다.

예를 들어, item 객체가 다음과 같다면:

```jsx
const item = {
  id: 1,
  emotionId: 3,
  content: "오늘의 일기",
  createdDate: "2024-12-04"
}

```

`{...item}`은 다음과 동일합니다:

```jsx
<DiaryItem
  key={item.id}
  id={item.id}
  emotionId={item.emotionId}
  content={item.content}
  createdDate={item.createdDate}
/>

```

이렇게 spread 연산자를 사용하면 객체의 모든 속성을 일일이 작성하지 않아도 되어 코드가 더 간결해집니다.

```jsx
        {sortedData.map((item) => <DiaryItem 
        key={item.id}
        {...item}/>)}
        {/* <DiaryItem/>  */}
```

DiaryItem 컴포넌트에 `...item`만 사용하는 것이 적절한 이유는:

1. **DiaryItem 컴포넌트가 필요로 하는 props가 명확히 정의되어 있습니다:**
- id
- emotionId
- createdDate
- content
1. **sortedData의 각 item 객체가 DiaryItem 컴포넌트의 props와 정확히 일치하는 구조**를 가지고 있습니다.
2. 불필요한 props가 전달될 위험이 적습니다. 데이터 구조가 일기 항목에 **필요한 속성들로만 구성**되어 있기 때문입니다.

따라서 이 경우에는 `...item`을 사용하는 것이 코드를 더 간결하게 만들면서도 안전합니다. 단, key prop은 React의 리스트 렌더링을 위해 별도로 명시해야 하므로 분리하여 작성되었습니다.

# [궁금한점] DiaryList.jsx

---

## 1. a, b파라미터의 의미

---

```jsx
  const getSortedDate = () => {
    return data.toSorted((a,b) => {
      if (sortType === "oldest") {
        return new Date(a.createdData) - new Date(b.createdData)
      } else {
        return new Date(b.createdData) - new Date(a.createdData)
      }
    })
  }
```

- 배열의 정렬 함수에서 **a,b는 배열의 두 요소를 비교하기 위한 파라미터**입니다
- **a는 현재 요소, b는 다음 요소를 의미합니다**
- **반환값이 음수면 a가 앞으로, 양수면 b가 앞으로 정렬됩니다**

### 1-1. 구체적 예시

---

```jsx
const data = [
  { id: 1, createdData: "2024-12-04" },  // a
  { id: 2, createdData: "2024-12-01" }   // b
]

```

**정렬 함수는 이 배열의 요소들을 두 개씩 비교합니다:**

1. a는 첫 번째 객체 (12월 4일)
2. b는 두 번째 객체 (12월 1일)

최신순 정렬의 경우:

```jsx
new Date(b.createdData) - new Date(a.createdData)
// 12월 1일 - 12월 4일 = 음수
// 음수가 나오면 순서 유지 (4일이 앞에 위치)

```

오래된순 정렬의 경우:

```jsx
new Date(a.createdData) - new Date(b.createdData)
// 12월 4일 - 12월 1일 = 양수
// 양수가 나오면 순서 변경 (1일이 앞으로 이동)

```

이렇게 두 날짜를 뺄셈하여 나온 결과값의 부호에 따라 정렬 순서가 결정됩니다.

### 1-2. sort/toSorted의 기본 규칙

---

JavaScript의 sort/toSorted 메서드는 내부적으로 다음과 같은 규칙을 가지고 있습니다:

1. 음수(-) 반환 시: a가 b보다 앞에 위치
2. 양수(+) 반환 시: b가 a보다 앞에 위치
3. 0 반환 시: 순서 유지

```jsx
// 최신순 정렬 (b - a)
new Date("2024-12-04") - new Date("2024-12-01")
// 양수가 나오므로 12월 4일이 앞으로

// 오래된순 정렬 (a - b)
new Date("2024-12-01") - new Date("2024-12-04")
// 음수가 나오므로 12월 1일이 앞으로
```

이는 JavaScript의 sort/toSorted 메서드의 기본 동작 방식이며, 이 규칙에 따라 정렬 순서가 결정됩니다. 이것은 언어 자체의 스펙이므로 개발자가 이 규칙을 따라 정렬 로직을 작성해야 합니다.

```jsx
  const getSortedDate = () => {
    return data.toSorted((a,b) => {
      if (sortType === "oldest") {
        return new Date(a.createdData) - new Date(b.createdData)
      } else {
        return new Date(b.createdData) - new Date(a.createdData)
      }
    })
  }
```

## 2. sort와 toSorted의 차이점

---

```jsx
// sort(): 원본 배열을 직접 수정
const numbers = [3, 1, 4];
numbers.sort(); // numbers 배열 자체가 변경됨

// toSorted(): 새로운 배열을 반환
const numbers = [3, 1, 4];
const sorted = numbers.toSorted(); // 원본 배열은 변경되지 않음

```

# [궁금한 점] Editor.jsx

---

```jsx
const Editor = () => {
  return (
    <div className='Editor'>
      <section className='date_section'>
        <h4>오늘의 날짜</h4>
        <input type="date"/>
      </section>
      <section className='emotion_section'>
        <h4>오늘의 감정</h4>
        {EmotionList.map((item) => <EmotionItem 
        key={item.emotionId}
        // emotionId={item.emotionId}
        // emotionName={item.emotionName}
        {...item}/>)} 
        {/* item 모두 활용? Q.? */}
      </section>
      <section className='content_section'></section>
      <section className='button_section'></section>
    </div>
  )
}
```

## 1. {…item}을 사용하는 이유

---

1. EmotionItem 컴포넌트가 `emotionId`와 `emotionName` 속성을 **모두 사용하고**
2. **item 객체가 정확히 이 두 속성을 가지고 있기 때문입니다.**

예를 들어, EmotionList가 다음과 같은 구조라면:

```jsx
const EmotionList = [
  {
    emotionId: 1,
    emotionName: "행복"
  },
  {
    emotionId: 2,
    emotionName: "슬픔"
  }
]

```

두 방식은 완전히 동일합니다:

```jsx
// 방식 1: 개별 지정
<EmotionItem
  key={item.emotionId}
  emotionId={item.emotionId}
  emotionName={item.emotionName}
/>

// 방식 2: spread 연산자 사용
<EmotionItem
  key={item.emotionId}
  {...item}
/>

```

item 객체의 모든 속성이 EmotionItem 컴포넌트에서 필요하기 때문에 spread 연산자를 사용하여 코드를 더 `간결`하게 작성한 것입니다.

# [궁금한 점] Edit Page

---

## 1.`onSubmit`과 `nav('/', {replace:true})` 관련

---

`onSubmit` 함수는 **New 컴포넌트에서 정의되어 Editor 컴포넌트로 전달**됩니다. 이 함수는 사용자가 입력한 데이터(input)를 받아 `onCreate` 함수를 호출하고, 그 후 홈 페이지로 이동합니다.

`nav('/', {replace:true})`에서 `replace: true` 옵션은 **현재 페이지를 브라우저 히스토리에서 교체**하는 역할을 합니다. 이렇게 하면 사용자가 뒤로 가기 버튼을 눌렀을 때 새 일기 작성 페이지로 돌아가지 않고 이전 페이지로 이동하게 됩니다.

<aside>
💡

`replace: true`는 현재 페이지를 완전히 대체하는 옵션으로, 새 일기 작성 페이지(`/new`)를 히스토리에서 지워 뒤로 가기 버튼을 눌러도 다시 돌아오지 못하게 만듭니다. 이는 사용자 경험을 개선하기 위해 설계된 처리 방식이에요.

</aside>

### 1-1. 일반적인 페이지 이동 (`replace: false`의 기본값)

---

만약 `replace` 옵션을 사용하지 않으면, `nav('/')`를 호출했을 때 **현재 페이지가 브라우저 히스토리에 추가**됩니다. 이렇게 되면 사용자는 페이지를 이동한 후 **뒤로 가기 버튼**을 누르면 작성 중이었던 페이지로 다시 돌아갈 수 있습니다.

예를 들어:

- **현재 페이지**: `/new` (새 일기 작성 페이지)
- `nav('/')`를 호출 → 홈 페이지(`/`)로 이동
- 사용자가 뒤로 가기 버튼을 누르면 `/new`로 다시 돌아갑니다.

### 1-2. `replace: true`를 사용하는 경우

---

`replace: true`를 사용하면 **현재 페이지(`/new`)가 브라우저 히스토리에서 완전히 대체됩니다.** 즉, `/new`가 히스토리에서 삭제되고 `/`만 히스토리에 남게 됩니다. 이렇게 하면 사용자가 뒤로 가기 버튼을 눌러도 `/new`로 돌아가는 게 아니라 **그 이전 페이지로 이동**하게 됩니다.

예를 들어:

- **현재 페이지**: `/new` (새 일기 작성 페이지)
- `nav('/', { replace: true })` 호출 → **홈 페이지(`/`)로 이동**
- 사용자가 뒤로 가기 버튼을 눌러도 `/new`로 돌아가지 않고 `/new` 이전 페이지로 이동합니다.

### 1-3. 왜 `replace: true`를 사용했을까?

---

`replace: true`를 사용한 이유는:

- **뒤로 가기를 통해 새 일기 작성 페이지로 돌아가는 것을 방지하기 위함.**
- 사용자가 일기를 작성한 뒤, 다시 작성 페이지로 돌아가면 작성했던 값들이 남아 있을 수 있는데, 이는 의도하지 않은 행동으로 보일 수 있어요.
- 사용자가 일기를 저장한 후, 작성 페이지를 다시 방문하려면 명확히 **"새로 작성을 시작"하거나 홈 페이지에서 이동**하도록 설계합니다.

## 2. `onChangeInput`과 EmotionItem의 `onClick` 관련

---

`onChangeInput` 함수는 입력 필드의 값이 변경될 때마다 호출되는 함수입니다. 이 함수는 일반적으로 `event` 객체를 받아 처리하지만, **EmotionItem의 경우 직접 클릭 이벤트를 처리해야 하므로 이벤트 객체와 유사한 구조를 만들어 전달합니다.**

```jsx
onClick={() => onChangeInput({
  target: {
    name: "emotionId",
    value: item.emotionId
  }
})}

```

이 코드는 EmotionItem을 클릭했을 때 `onChangeInput` 함수를 호출하면서, 마치 input 요소의 change 이벤트가 발생한 것처럼 객체를 구성해 전달합니다. **`target` 객체는 일반적인 DOM 이벤트의 `target` 속성을 모방한 것입니다.**

### 2-1. 리액트에서 이벤트처리와 일반 DOM 이벤트의 구조

---

**DOM 이벤트(예: `click`, `change`)가 발생하면, 브라우저는 이벤트 객체를 생성**합니다. 이 객체는 이벤트에 대한 다양한 정보를 포함하고 있습니다.

예를 들어, `input` 요소의 `change` 이벤트의 경우:

```jsx
<input
  name="username"
  onChange={(event) => {
    console.log(event.target.name); // "username"
    console.log(event.target.value); // 입력된 값
  }}
/>

```

여기서 `event.target`은 이벤트가 발생한 DOM 요소를 가리키며, **`name`과 `value`는 그 요소의 속성**입니다.

### 2-1-1. 리액트 DOM 요소 name, value의 속성?

---

1. HTML 요소의 속성
HTML 요소들은 여러 가지 속성을 가질 수 있습니다. 예를 들어, `<input>` 요소의 경우:
    
    ```html
    <input name="username" value="John" type="text" />
    
    ```
    
    **여기서 `name`, `value`, `type`은 모두 `<input>` 요소의 속성입니다.**
    
2. DOM에서의 표현
브라우저가 HTML을 파싱하여 DOM(Document Object Model)을 생성할 때, 이**러한 HTML 속성들은 DOM 요소의 속성으로 변환됩니다.**
3. 이벤트 객체와 target
사용자가 입력 필드를 조작하면 (예: 텍스트 입력, 선택 변경 등) **`change` 이벤트가 발생합니다. 이때 브라우저는 이벤트 객체를 생성하고, 이 객체의 `target` 속성은 이벤트가 발생한 DOM 요소를 가리**킵니다.
4. target의 속성 접근
`event.target`이 D**OM 요소를 가리키기 때문에, 우리는 이를 통해 해당 요소의 모든 속성에 접근**할 수 있습니다. 따라서 `event.target.name`과 `event.target.value`를 통해 각각 요소의 `name`과 `value` 속성 값을 얻을 수 있습니다.
5. 왜 이런 구조인가?
    - 일관성: 모든 DOM 요소에 대해 동일한 방식으로 속성에 접근할 수 있습니다.
    - 편의성: 이벤트 핸들러에서 쉽게 요소의 정보를 얻을 수 있습니다.
    - 효율성: 이벤트 객체를 통해 필요한 모든 정보를 한 번에 전달할 수 있습니다.

### ⚠️ 2-2. React에서의 이벤트 처리 : EmotionItem에서의 구현

---

EmotionItem의 경우, `input` 요소가 아니라 **커스텀 컴포넌트**이기 때문에 직접 `change` 이벤트를 발생시킬 수 없습니다. 대신, 클릭 이벤트를 사용하고 **그 안에서 `change` 이벤트와 유사한 구조의 객체**를 만들어 전달합니다.

```jsx
onClick={() => onChangeInput({
  target: {
    name: "emotionId",
    value: item.emotionId
  }
})}

```

이 코드는 `change` 이벤트 객체의 구조를 모방하여 `onChangeInput` 함수가 일관된 방식으로 동작할 수 있게 합니다.

### 2-2-1. 이벤트 구조

---

1. 기본 이벤트 구조

모든 DOM 이벤트(click, change 등)는 기본적으로 다음과 같은 구조를 가집니다:

```jsx
{
  type: "이벤트 타입 (예: 'click', 'change')",
  target: 이벤트가 발생한 DOM 요소,
  currentTarget: 현재 이벤트 핸들러가 attached된 요소,
  // 기타 이벤트 관련 속성들...
}

```

1. click 이벤트 구조

click 이벤트는 주로 다음과 같은 추가 속성을 가집니다:

```jsx
{
  type: "click",
  target: 클릭된 요소,
  clientX: 클릭된 화면 X 좌표,
  clientY: 클릭된 화면 Y 좌표,
  button: 클릭된 마우스 버튼 (0: 왼쪽, 1: 가운데, 2: 오른쪽)
  // 기타 속성들...
}

```

1. change 이벤트 구조

change 이벤트는 주로 form 요소의 값이 변경될 때 발생하며, 구조는 다음과 같습니다:

```jsx
{
  type: "change",
  target: 값이 변경된 요소,
  // target 요소의 주요 속성:
  //   - value: 새로운 값
  //   - checked: 체크박스나 라디오 버튼의 경우 체크 상태
  //   - selectedOptions: select 요소의 경우 선택된 옵션들
  // 기타 속성들...
}

```

이러한 구조를 이해하고 있으면, 커스텀 이벤트를 만들 때 이와 유사한 형태로 구성하여 일관성 있는 코드를 작성할 수 있습니다.

### 2-2-2. 참고하면 좋을 문서

---

1. React 공식 문서의 "Handling Events" 섹션:
[https://react.dev/learn/responding-to-events](https://react.dev/learn/responding-to-events)

이 페이지에서는 React에서 이벤트를 처리하는 기본적인 방법과 합성 이벤트(Synthetic Events)에 대해 설명합니다.

1. React 공식 문서의 "SyntheticEvent" 레퍼런스:
[https://react.dev/reference/react-dom/components/common#react-event-object](https://react.dev/reference/react-dom/components/common#react-event-object)

여기서는 React의 이벤트 객체 구조와 속성들에 대해 자세히 설명하고 있습니다.

1. MDN(Mozilla Developer Network)의 DOM 이벤트 문서:
[https://developer.mozilla.org/en-US/docs/Web/API/Event](https://developer.mozilla.org/en-US/docs/Web/API/Event)

이 문서는 기본적인 DOM 이벤트의 구조와 속성에 대해 자세히 설명합니다. React의 합성 이벤트는 이 DOM 이벤트를 기반으로 만들어졌습니다.

## 3. `onChangeInput` 함수의 동작

---

```jsx
const onChangeInput = (e) => {
  let name = e.target.name
  let value = e.target.value

  if (name === "createdDate") {
    value = new Date(value) // value를 date 형식으로
  }

  setInput({
    ...input,
    [name]: value
  })
}

```

이 함수는 입력값이 변경될 때마다 호출됩니다. `e.target.name`은 변경된 입력 필드의 이름을, `e.target.value`는 새로운 값을 나타냅니다.

`setInput({ ...input, [name]: value })`는 **기존의 `input` 객체를 복사하고(`...input`), 변경된 필드의 값만 업데이트**하는 역할을 합니다. `[name]`은 계산된 속성 이름으로, `name` 변수의 값을 키로 사용합니다.

예를 들어, **emotionId가 변경되면 `setInput({ ...input, emotionId: newValue })`와 같이 동작하여 emotionId만 업데이트되고 다른 필드는 그대로 유지**됩니다.

이렇게 함으로써 여러 입력 필드를 가진 폼에서 각 필드의 변경사항을 효율적으로 관리할 수 있습니다.

## 4. 의존성 배열 누락 문제

---

이 문제는 `useEffect`의 의존성 배열과 초기 상태 설정에 관련된 문제입니다. 현재 코드에서 두 가지 이슈가 있습니다:

1. `useEffect`의 의존성 배열이 비어있어서(`[]`) `initData`가 변경되어도 다시 실행되지 않습니다.
2. 초기 상태값이 하드코딩되어 있어서 (`content: "하하"`) **`initData`의 값이 반영되기 전에 이 값이 먼저 보입니다.**

수정된 코드는 다음과 같아야 합니다:

```jsx
const Editor = ({initData, onSubmit}) => {
  const [input, setInput] = useState({
    createdDate: initData ? new Date(Number(initData.createdDate)) : new Date(),
    emotionId: initData ? initData.emotionId : 3,
    content: initData ? initData.content : "",
  })

  useEffect(() => {
    if(initData) {
      setInput({
        ...initData,
        createdDate: new Date(Number(initData.createdDate))
      })
    }
  }, [initData]) // initData를 의존성 배열에 추가

  // ... 나머지 코드는 동일
}

```

이렇게 수정하면:

1. **초기값이 `initData`를 반영하여 설정됩니다.**
2. **`initData`가 변경될 때마다 `useEffect`가 실행되어 데이터가 올바르게 업데이트**됩니다.