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

# querySelector와 DOM요소

---

- **`document.querySelector('div')`**는 문서에서 첫 번째로 발견되는 **`<div>`** 요소를 선택하여 반
- 이는 DOM(Document Object Model) 요소 객체
다

## 단순 인스턴스의 변수 접근 or set으로 설정

---

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