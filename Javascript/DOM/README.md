# [실습]JS_DOM

날짜: 2024년 10월 21일

# getElementbyID()와 querySelector의 차이

---

| 특성 | querySelector | getElementById |
| --- | --- | --- |
| 선택자 유형 | CSS 선택자 (ID, 클래스, 태그 등) | 오직 ID만 |
| 사용 예시 | `document.querySelector('#id')` `document.querySelector('.class')` `document.querySelector('div')` | `documㅅ순ent.getElementById('id')` |
| 반환 값 | 일치하는 첫 번째 요소 | 일치하는 요소 |
| 일치하는 요소가 없을 때 | null 반환 | null 반환 |
| 성능 | 상대적으로 느림 | 상대적으로 빠름 |
| 유연성 | 높음 (다양한 선택자 사용 가능) | 낮음 (ID만 사용 가능) |
| 사용 편의성 | 복잡한 선택자 사용 가능 | 단순하고 직관적 |
| 브라우저 지원 | IE8 이상 | 모든 주요 브라우저 |

# querySelector의 반환값

---

<aside>
💡

**특정 요소의 전체 DOM 객체를 반환**

</aside>

- 만약 내가 `div` 에 접근하는 경우
    - 이는 **`<div>`** 태그 자체가 아니라 해당 **`<div>`** 요소의 전체 DOM 객체를 반환

```python
<div id="myDiv">
  <p>Some text</p>
</div>
```

⇒ `div` 요소(그 안의 내용 포함)를 나타내는 DOM 객체를 반환합니다

- 해당 값이 반환하는 값을 기반으로 `속성 접근 및 수정`이 가능해진다.

```python
const div = document.querySelector('div');
console.log(div.id); // id 속성 읽기
div.className = 'new-class'; // class 속성 변경
```

```python
div.textContent = '새로운 텍스트'; // 텍스트 내용 변경
div.innerHTML = '<span>HTML 내용 변경</span>'; // HTML 내용 변경
```

```python
div.style.backgroundColor = 'red'; // 배경색 변경
div.style.fontSize = '20px'; // 글자 크기 변경
```

```python
const children = div.children; // 모든 자식 요소 가져오기
const firstChild = div.firstElementChild; // 첫 번째 자식 요소 가져오기
```

```python
const newElement = document.createElement('p');
div.appendChild(newElement); // 새로운 자식 요소 추가
```

# querySelector와 DOM요소

---

- **`document.querySelector('div')`**는 문서에서 첫 번째로 발견되는 **`<div>`** 요소를 선택하여 반
- 이는 DOM(Document Object Model) 요소 객체
다

## 단순 인스턴스의 변수 접근 or set으로 설정

---

**[단순 인스턴스 변수 접근]**

```jsx
    //img 에  접근해서 src속성에 값 추가
    // #document.getElementById("img태그id").src == 를 통해서 할당해주세요
    const img = document.querySelector('img') //img 속성 => 속성이 아니다 => getAttriubute 
    //그냥 특정 element
    console.log(img) //qeury자체에 접ㄱ느해서 -> 그안의 src인 속성에 접근해야 한다.
    img.src = './profile.jpg'
    img.alt = 'profile'

//    const img = document.querySelector('img')
    // document.setAttribue(img.src, './profile.jpg')
    // document.setAttribute('src', './profile.jpg') //속성 편집
    // document.setAttribute('alt', 'profiles') //속성 편집
```

**[SetAttribute 접근]**

```jsx
    const img = document.querySelector('img')
    img.setAttribute('src', 'profile.jpg') 
    img.setAttribute('alt', '프로필 사진') 
```

- 특정 태그를 선택해서 → 특정 class를 부여한다.

```jsx
    //class List를 따서 => 여기에 추가해주어야 함
    //name.classList.add('.highlight')
    
    console.log(name.classList) //값이 없어 -> 추가해야 해
    name.classList.add('highlight') //color ==> classList에 값을 추가하는 것
    //클래스 속성 자체를 조작하는 것
    //Q. 아이디가 네임인 것도 클래스?
    job.classList.add('highlight')
    experience.classList.add('highlight')
    email.classList.add('highlight')
    phone.classList.add('highlight')

  
    const img = document.querySelector('img')
    img.setAttribute('src', 'profile.jpg') 
    img.setAttribute('alt', '프로필 사진') 
    //img 태그에 img class 부여
    img.classList.add('img') //class를 추가한다>? == 클래스 속성 자체를 조작
    //그럼 자체적으로 class가 존재하는건가? 일단 보류 QQQ!!

    const h1Tag = document.querySelector('h1')
    h1Tag.classList.add('title')

    const bodyTag = document.querySelector('body')
    bodyTag.classList.add('container')

```

| **특징** | **첫 번째 코드 블록** | **두 번째 코드 블록** |
| --- | --- | --- |
| **속성 설정 방식** | `img.src = '값'` | `img.setAttribute('src', '값')` |
| **클래스 추가** | 없음 | `element.classList.add('클래스명')` |
| **조작 대상** | 이미지 태그만 | 여러 요소 (이미지, 제목, 본문 등) |
| **코드 범위** | 제한적 | 광범위 |
| **유연성** | 낮음 | 높음 |
| **권장도** | 덜 권장됨 | 더 권장됨 |

# ClassList 이해하기

---

1. 특정 클래스를 부여한다는 것은 클래스를 추가하는 것을 의미
2. 클래스를 추가하려면 먼저 해당 태그(요소)를 `선택` → 가장 우선시 되는 것
3. 선택된 것은 태그 자체가 아니라 `태그와 그 내용을 포함한 전체 엘리먼트` ⇒ **이것이 핵심**
4. 이 선택된 엘리먼트 덩어리에 `클래스를 추가하거나 삭제`할 수 있다.

| 단계 | 설명 | 예시 코드 |
| --- | --- | --- |
| 1. 태그 선택 | 조작하려는 HTML 요소를 JavaScript로 선택 | `const h1Element = document.querySelector('h1');` |
| 2. 엘리먼트 추출 | 선택된 태그와 그 내용을 포함한 전체 요소가 추출됨 | (위의 코드로 이미 추출됨) |
| 3. 클래스 추가 | 선택된 엘리먼트에 새로운 클래스 추가 | `h1Element.classList.add('new-class');` |
| 4. 클래스 삭제 | 필요시 선택된 엘리먼트에서 클래스 제거 | `h1Element.classList.remove('old-class');` |

# Uncaught InvalidCharacterError: Failed to execute 'remove' on 'DOMTokenList': The token provided ('[object HTMLLIElement]') contains HTML space characters, which are not valid in tokens.

---

```jsx
    const itemGame = document.querySelector('#game') //이건 element -> 근데 class?
    console.log(itemGame)

    studyList.classList.remove(itemGame)

```

```

    studyList.classList.remove(todoList > itemGame)
    console.log(studyList)
```

→ error는 발생하지 않고 변동사항 없음 ⇒ 내부값 확인 필요

# Uncaught TypeError: Cannot read properties of undefined (reading 'toggle')

- Uncaught TypeError: Cannot read properties of undefined (reading 'remove')

---

⇒객체가 null또는 undefine 상태

```jsx
    //그걸 지울 건데? 
    //studylist에서 지워서 에러가 뜬 것 같음
    todoList.classList.toggle(itemGame)  //class 자체를 제거
```

```jsx

    //문제에 자식 요소중에서 game인것을 삭제해라고 헀다.
    studyList.removechild(itemGame) //왜 삭제가 안됨? => 어떤 자식인지 받아왔는데 ? 
    //index.html:41 Uncaught TypeError: studyList.removechild is not a function at index.html:41:15 ??
```

```jsx

    for (let i=0;i<todoList.length-1;i++) { //1개만 출력
      console.log(todoList[i]) //출력  -> 마지막 한개 뺀다.
    } //단순 출력 
```

```jsx
    studyList.removeChild(itemGame) //왜 삭제가 안됨? => 어떤 자식인지 받아왔는데 ? 
    //오타때문
```

## 출력값이 console.log가 찍히지 않는 이유

---

```jsx
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  <script>
```

→ 중복때문에 script가 올바르게 출력되지 않는 문제

# index.html:45 Uncaught TypeError: Cannot read properties of undefined (reading 'add')

---

```jsx
todoList.classList.add('list-group-item-class')
```

# index.html:29 Uncaught NotFoundError: Failed to execute 'removeChild' on 'Node': The node to be removed is not a child of this node. at

---

→ 해당 노드에 child 값을 제거할 수 없다.

→ 또한 이것은 child 노드가 아니다.

```jsx
    //heard id에 들어있는게 classname으로 들어가게된다
    //heard 요소에 있는 id값을 삭제한다.
    const header = document.querySelector('#card') 
    console.log(header)
    header.classList.add('card') //class 추가
    //그리고 id삭제
    //header.classList.remove('#card') //id삭제가 안돼
    //id를 삭제 => heard : 부모에 접근해서 삭제해야 한다?
    const realheader = document.querySelector('header')
    header.removeChild(header)
```

# innerText ⇒ P태그 내부 text추출

---

```jsx
  <script>
    // 아래에 코드 작성
    //helloword를 가지는 px래르 선ㅌ택해서 Ptag변수에 할당한다
    pTag = document.querySelector('div > p') //div 안에 p?
    //li태그를 모두 선택해서 liTags 변수에 할당
    liTags = document.querySelectorAll('li') //li 선택
    //pTag에 있는 내용 값만 추출하기
    console.log(pTag.innerText) //innerText를 넣으면 안에 text만 출력된다.
    console.log(liTags)
  </script>
```

# sth:nth-child(n) : 선택자 링크 참고

---

→ 이거 자체가 하나의 묶음자

[:nth-child - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/ko/docs/Web/CSS/:nth-child)

```jsx

    const itemGame = document.querySelector('#game')
    console.log(itemGame)
    const title = document.querySelector('h1')

    title.textContent = '오늘 공부 목록'

    const studyList = document.querySelector('ul')
    studyList.classList.add('study', 'list-group') //study class 추가 하시오.  => 3번 조건 => list_group을 넣고

    //li:nth-;child(n) 선택자를 사용하여 각각의 li 태그를 하나씩 선택 해 서로 다른 변수에 할당
    const li1 = document.querySelector('li:nth-child(1)') //첫번째 선택자를 의미
    console.log(li1)
    const li2 = document.querySelector('li:nth-child(2)') //두번째 선택자를 의미
    const li3 = document.querySelector('li:nth-child(3)') //세번째 선택자를 의미
    const li4 = document.querySelector('li:nth-child(4)') //네번째 선택자를 의미
    li1.classList.add('list-group-item')
    li2.classList.add('list-group-item')
    li2.setAttribute('aria-current', true) //2번째 태그에는 true를 부여한다.
    li2.classList.add('active')
    li3.classList.add('list-group-item')
    li4.classList.add('list-group-item')

```

# 특정 속성 삭제 : removeAttirbute

---

```python
header.removeAttribute('id') //id 속성 삭제 // 결론

```

# Element란? → 덩어리

---

- HTML 문서의 기본 구성 단위입니다.
- 일반적으로 시작 태그, 내용, 종료 태그로 구성된다.
    - 예 : **`<태그명>내용</태그명>`**
- 속성을 가질 수 있으며, 속성은 요소에 대한 추가 정보를 제공한다
    - 예 : **`<태그명 속성명="속성값">내용</태그명>`**
- HTML 문서의 구조와 의미를 정의하는 데 사용된다.
- 주요 요소 예시: **`<html>`**, **`<head>`**, **`<body>`**, **`<p>`**, **`<div>`** 등

# 호이스팅이란?

---

- JavaScript에서 **변수와 함수의 선언이 해당 스코프의 최상단으로 끌어올려지는 것처럼 동작**하는 현상
- 실제로 코드가 물리적으로 이동하는 것은 아니며, JavaScript 엔진의 동작 방식에 의한 현상
- 변수 호이스팅:
    - `var`로 선언된 변수는 선언과 초기화가 호이스팅 된다(undefined로 초기화).
        - 이러한 문제가 발생하여 var를 사용하지 않음 ⇒ 최신
    - `let`과 `const`로 선언된 변수는 선언만 호이스팅되고 초기화는 되지 않음(TDZ 발생).
- 함수 호이스팅:
    - 함수 선언문은 전체가 호이스팅된다.
    - 함수 표현식은 변수 호이스팅과 동일하게 동작한다.
- 호이스팅은 코드의 가독성과 유지보수성에 영향을 줄 수 있으므로, 변수와 함수는 사용하기 전에 선언하는 것이 좋다.

# 궁금증

---

```jsx

    const todoList = document.querySelectorAll('li')
    console.log(todoList) //todoList자체를 console.log에 찍어봄 => li들의 집합체 NodeList가 나타날 것
    //NodeList(5)

    console.log(todoList.classList) //undefine => class 덩어리는 undefined
    //QQ. class 덩어리가 undefined인 이유가 있을까?
    //AA. todoList는 querySelectorAll()로 선택된 여러 요소의 집합인 NodeList
    //NodeList 자체는 classList 속성을 가지고 있지 않다
    
    const firsttoDo = document.querySelector('li') //첫번째 요소라고 가정했을 때
    console.log(firsttoDo) //첫번째 li값
    //즉 하나의 element를 반환한다.
    
    console.log(firsttoDo.classList) //첫번쨰의 classList의 값 => class가 무엇이 있는지 보기
    //아무런 값도 확인되지 않는 것을 볼 수 있음 == DOMTokenList [value: '']length: 0value: ""[[Prototype]]: DOMTokenList
    //배열의 길이자체가 0이고, value는 없다

    console.log(firsttoDo.className) //QQ. 단순 className은 무엇?
    //QQ. 아무것도 출력되지 않는 것을 볼 수 있는데 그 이유?
    //QQ. 클래스 리스트를 굳이 사용하는 이유? 클래스하나만 넣을 수는 없는지?

    //그럼 여기 firstTodo에 값을 넣으면?
    firsttoDo.classList.add('hello') //새로운 클래스명을 넣는 것 == 새로운 클래스명이 들어간 것 확인됨
    console.log(firsttoDo)
    console.log(firsttoDo.classList) //value 자체가 hello가 생김 -> list에 hello라는 클래스 명이 생김
    console.log(firsttoDo.className) //이제 className이 있기 떄문에 출력이 가능

    firsttoDo.classList.add('hello') //QQ. 동일한 이름을 추가했을 때 hello가 두개 생기나?
    firsttoDo.classList.add('hello2')
    console.log(firsttoDo)
    console.log(firsttoDo.classList) 
    console.log(firsttoDo.className) //있는 것 모두 출력되는 것 같음
```

## **1. classList가 undefined인 이유**

---

- **`todoList`**는 **`querySelectorAll()`**로 선택된 여러 요소의 집합인 NodeList이다.
    - NodeList 자체는 **`classList`** 속성을 가지고 있지 않다.
    - 각 개별 요소(li)는 **`classList`**를 가지지만, NodeList 전체로는 접근할 수 없다.

## 2. className이란?

---

- **`className`**은 요소의 클래스 이름을 문자열로 반환하거나 설정하는 속성이다.
1. **className을 출력했을 때 → 아무것도 출력되지 않는 이유**
    - 해당 요소에 클래스가 설정되어 있지 않기 때문
    - 클래스가 없으면 **`className`**은 빈 문자열을 반환
2. **classList를 사용하는 이유와 클래스 하나만 넣을 수 있는지?**
    - **`classList`**는 여러 클래스를 쉽게 추가, 제거, 토글할 수 있는 메서드를 제공
    - 단일 클래스만 사용할 경우 **`className`**을 사용할 수 있지만, **`classList`**가 더 유연하고 편리

## 3. 동일한 이름의 클래스 추가

---

- **`classList`**는 중복된 클래스를 허용하지 않는다.

# **className vs classList 비교**

---

| **속성** | **className** | **classList** |
| --- | --- | --- |
| 타입 | 문자열 | **DOMTokenList** |
| 설명 | 요소의 모든 클래스 이름을 문자열로 반환. 여러 클래스를 띄어쓰기로 구분. | 여러 클래스를 관리할 수 있는 객체. add, remove, toggle 등의 메서드 제공. |
| 예시 | element.className = "class1 class2" | element.classList.add("class3") |
| 장점 | **간단한 설정 가능.** 모든 클래스 일괄 변경 시 유용. | 중복 방지, **기존 클래스 유지, 유연한 클래스 조작 가능** |
1. **일반적인 상황에서는 classList 사용을 권장**
    - **이유**:
        - 기존 클래스를 유지하면서 새로운 클래스를 추가/제거할 수 있어 안전하다.
        - 중복 클래스 추가를 자동으로 방지한다.
        - add(), remove(), toggle() 등의 편리한 메서드를 제공하여 클래스 조작이 용이하다.
        - 개별 클래스의 존재 여부를 쉽게 확인할 수 있다.(contains() 메서드 사용).
2. **특정 상황에서 className 사용 고려**
    - **이유**:
        - 요소의 모든 클래스를 한 번에 교체해야 할 때 간단하게 사용할 수 있다.

## 실제로 classList에 값이 있는 곳에 → className을 사용한다면?

---

```jsx
// 상기 내용 정리
// 모든 li 요소 선택
const todoList = document.querySelectorAll('li');
console.log(todoList); // NodeList(5) [li, li, li, li, li]

// NodeList에는 classList가 없음
console.log(todoList.classList); // undefined

// 첫 번째 li 요소 선택
const firstToDo = document.querySelector('li');
console.log(firstToDo); // <li>...</li>

// 초기에는 클래스가 없음
console.log(firstToDo.classList); // DOMTokenList []
console.log(firstToDo.className); // ""

// 클래스 추가
firstToDo.classList.add('hello');
console.log(firstToDo.classList); // DOMTokenList ["hello"]
console.log(firstToDo.className); // "hello"

// 동일한 클래스 추가 시도 (중복 추가 안됨)
firstToDo.classList.add('hello');
// 새로운 클래스 추가
firstToDo.classList.add('hello2');

console.log(firstToDo); // <li class="hello hello2">...</li>
console.log(firstToDo.classList); // DOMTokenList ["hello", "hello2"]
console.log(firstToDo.className); // "hello hello2"

-----------------------------------------------
//물음의 핵심

// className을 사용하여 모든 클래스 교체
firstToDo.className = 'ho';

console.log(firstToDo); // <li class="ho">...</li>
console.log(firstToDo.classList); // DOMTokenList ["ho"]
console.log(firstToDo.className); // "ho"
```