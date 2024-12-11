# [React] 감정 일기장 복습5_Diary 페이지

날짜: 2024년 12월 9일

# Diary Component 만들기

---

## Custom Hook만들기

---

[자신만의 Hook 만들기 – React](https://ko.legacy.reactjs.org/docs/hooks-custom.html)

## [오류] Diary.jsx에서 setDiaryDate를 했는데도 못받아옴

---

```jsx
const Diary = () => {
  const [diaryDate, setDiaryDate] = useState()
  const params = useParams()
  const data = useContext(DiaryStateContext)
  const result = useDiary(data, params.id)
  //호출말고 일단 불러오는 것 사용

  useEffect(()=>{
    if (result) {
      console.log('result' , result)
      setDiaryDate(result)
      // console.log(changeFormatter(diaryDate.createdDate))
    }
  }, [result, data, params.id])

  //못받아오면 로딩중
  // if (diaryDate) {
  //   return <div>...로딩중</div>
  // }

```

```jsx
 useEffect(()=>{
    if (result) {
      console.log('result' , result)
      setDiaryDate(result)
      // setDiaryDate({
      //   ...result,
      //   createdDate : new Date(Number(result.createdDate))
      // })
      // console.log(changeFormatter(diaryDate.createdDate))
      //데이터 => 못받아오는 이유 객체 new Date()? => 동일한데
    }
  }, [result])

 // 못받아오면 로딩중
  if (diaryDate) {
    return <div>...로딩중</div>
  }
//아직도 값을 못받아옴..
```

⇒ 보다가 알게 되었는데 못받아오면을 적어놓고 `(diaryDate)` 만 받아옴

## content 내용 제외

---

```jsx
  console.log('content', content)
  console.log('createdDate', createdDate) //undefined
  console.log('emotionId', emotionId) //undefined
  console.log('id', id) //undefined
```

⇒ 데이터를 못받아온다?

## 날짜 데이터 null값

---

```jsx
      <Header text={`${getEmotionImage(diaryDate.createdDate)}기록`}
```

<aside>
💡

수정 사항 ⇒ Date 객체 다시 확인

</aside>

```jsx
console.log(diaryDate, 'diaryDate 받아와지는데 왜 HeaderText는 못받아오는가?')

     ..
      <Header text={`${changeFormatter(new Date(diaryDate.createdDate))}의 기록`}

```

⇒ 갑자기 된다?

**[Viewer.jsx]**

```jsx
const Viewer = ({content, createdDate, emotionId, id}) => {
  console.log('content', content)
  console.log('createdDate', createdDate) //undefined
  console.log('emotionId', emotionId) //undefined
  console.log('id', id) //undefined

```

## 궁금한점

---

## 1. 필요한 클래스명만 설정하는 것:

- 맞습니다. 불필요한 클래스를 줄이면 코드가 간결해지고 유지보수가 쉬워집니다.

## 2. CSS 속성 설명:

- space-around: 요소들 사이에 동일한 간격을 두고 배치합니다.
- **word-break: 단어의 줄바꿈 방식을 지정합니다.**
- **overflow-wrap: 박스를 넘어가는 단어의 줄바꿈 방식을 지정합니다.**

## 3. text-align: left:

- 기본적으로 왼쪽 정렬이 자연스러운 읽기 방식이기 때문입니다.

## 4. div 안에 p 태그 사용:

- **시맨틱한 HTML 구조를 위해서입니다**. p 태그는 문단을 나타내는 데 적합합니다.

# 강의 내역과 코**드 비교**

---

[내코드]

- **Diary.jsx**
    
    ```jsx
    import { useNavigate, useParams } from "react-router-dom"
    import Button from "../components/Button"
    import Header from "../components/Header"
    import Viewer from './../components/Viewer';
    import useDiary from "../hooks/useDiary"
    import { useContext, useEffect, useState } from "react"
    import { DiaryStateContext } from './../App';
    import { changeFormatter } from "../util/get-matching-date";
    import { getEmotionImage } from "../util/get-motion-image";
    
    const Diary = () => {
      const nav = useNavigate()
      const [diaryDate, setDiaryDate] = useState()
      const params = useParams()
      const data = useContext(DiaryStateContext)
      const result = useDiary(data, params.id)
      //호출말고 일단 불러오는 것 사용
    
      useEffect(()=>{
        if (result) {
          console.log('result' , result)
          setDiaryDate(result)
          // setDiaryDate({
          //   ...result,
          //   createdDate : new Date(Number(result.createdDate))
          // })
          // console.log(changeFormatter(diaryDate.createdDate))
          //데이터 => 못받아오는 이유 객체 new Date()? => 동일한데
        }
      }, [result])
    
     // 못받아오면 로딩중 => 
      if (!diaryDate) {
        return <div>...로딩중</div>
      }
      console.log(diaryDate, 'diaryDate 받아와지는데 왜 HeaderText는 못받아오는가?')
    
      
      // console.log(diaryDate, 'hello')
      return (
        <div>
          {/* hederText 수정 => 일치값을 데이터 변환해줄 것 */}
          <Header text={`${changeFormatter(new Date(diaryDate.createdDate))}의 기록`}
          leftChild={<Button text={"< 뒤로가기"}
          onClick={() => nav(-1)}/>}
          rightChild={<Button text={"수정하기"}
          onClick={() => nav(`/edit/${params.id}`)}/>}/>
          <Viewer 
          diaryDate={diaryDate}/>
        </div>
      )
    }
    
    export default Diary
    ```
    
- **Viewer.jsx**
    
    ```jsx
    import { useParams } from "react-router-dom"
    import { getEmotionImage } from "../util/get-motion-image"
    import { emotionData } from "../util/get-matching-image"
    import "./Viewer.css"
    import useDiary from "../hooks/useDiary"
    import { useContext } from "react"
    import { DiaryStateContext } from './../App';
    
    //특정 data 받아오는 것 => edit 페이지에서 사용 => 필터링
    //emotionData 필터링하는 것 => 불러오기
    const Viewer = ({diaryDate}) => {
      // console.log('content', content)
      // console.log('createdDate', createdDate) //undefined
      // console.log('emotionId', emotionId) //undefined
      // console.log('id', id) //undefined
      console.log(diaryDate, '받아옴')
      const emotion = 5
      //호출말고 일단 불러오는 것 사용
      // const findContent = emotionData.find((item) => String(item.emotionId) === String(emotion))
      const findContent = emotionData.find((item) => String(item.emotionId) === String(diaryDate.emotionId))
      // console.log(params.id)
      return (
        <div className="Viewer">
          <section className="emotion_section">
            {/* 이것도 보고 div태그 */}
            <h4>오늘의 감정</h4> 
            {/* 변경 예정 => 특정 emotionImage로, backgroundColor도 */}
            <div className={`emotion_section_img emotion_section_img_${diaryDate.emotionId}`}>
              {/* div로 형식 통일 */}
              <img src={getEmotionImage(Number(diaryDate.emotionId))} alt="" />
              <h4>{findContent.emotionName}</h4>
              {/* div로 */}
            </div>
          </section>
          <section className="content_section">
            <h4>오늘의 일기</h4>
            <div className="content_section_info">{diaryDate.content}</div>
          </section>
        </div>
      )
    }
    
    export default Viewer
    ```
    
- **Viewer.css**
    
    ```jsx
    .Viewer {
      display: flex;
      flex-direction: column;
      justify-content: center;
      /* align-items: center; */
      text-align: center;
      /* aligin-items는 하기 div때문에 또 이상해진듯 */
    }
    
    .Viewer > section {
      margin: 15px;
    }
    
    .Viewer > section > h4 {
      font-size: 24px;
      font-weight: bold;
    }
    
    .Viewer .emotion_section {
      display: flex;
      flex-direction: column;
      /* justify-content: center; */
      align-items: center;
    }
    
    .Viewer .emotion_section .emotion_section_img {
      border-radius: 5px;
      /* text-align: center; */
      /* justify-content: center; */
      /* display: flex; */
      /* flex-direction: column; */
      /* align-items: center; */
      /* justify-content: center; */
      padding: 10px;
      width: 40%;
    
      /* align-items: center;   */
    }
    
    /* div는 먹지 않음 */
    .Viewer .emotion_section .emotion_section_img > h4 {
      color: white;
      font-size: 18px;
      font-weight: bold;
    }
    
    .Viewer .emotion_section .emotion_section_img_1 {
      background-color: rgb(99,201,101);
    }
    .Viewer .emotion_section .emotion_section_img_2 {
      background-color: rgb(157,215,114);
    }
    .Viewer .emotion_section .emotion_section_img_3 {
      background-color: rgb(253,206,23);
    }
    .Viewer .emotion_section .emotion_section_img_4 {
      background-color: rgb(253, 132, 70);
    }
    .Viewer .emotion_section .emotion_section_img_5 {
      background-color: rgb(253, 86, 95);
    }
    
    .Viewer .content_section {
      margin-top: 50px;
    }
    
    .Viewer .content_section .content_section_info {
      background-color: rgb(236, 236, 236);
      border-radius: ;
      padding : 40px;
      font-size: 24px;
      font-weight: bold;
    }
    ```
    
- **get-matching-date.js**
    
    ```jsx
    //edit
    
    export const changeFormatter = (date) => { 
      // input으로 입력되는 친구도 똑같은 문자열이기 때문에 날짜로 다시 변환
        // console.log(date)
        const year = date.getFullYear()
        const month = date.getMonth() + 1
        const day = date.getDate()
        //근데 단순히 작성하면 2024-12-8 => 우리가 원하는 00-00이 아님
        if (month < 10 && day < 10) {
          return `${year}-0${month}-0${day}`
        } else if (month < 10) {
          return `${year}-0${month}-${day}`
        } else if (day < 10) {
          return `${year}-${month}-0${day}`
        } else {
          return `${year}-${month}-${day}`
        }
      } 
    ```
    
- **get-matching-image.js**
    
    ```jsx
    // 아이디별
    export const emotionData = [
      {
        emotionId : 1,
        emotionName : '완전 좋음'
      },
      {
        emotionId : 2,
        emotionName : '좋음'
      },
      {
        emotionId : 3,
        emotionName : '그럭저럭'
      },
      {
        emotionId : 4,
        emotionName : '나쁨'
      },
      {
        emotionId : 5,
        emotionName : '최악'
      }
    ]
    ```
    

| 항목 | 평가 및 제안 |
| --- | --- |
| **실력 평가** | • 기능적 구현: 우수
• CSS: 개선 필요
• React 컴포넌트 구조 및 상태 관리: 양호 |
| **주요 차이점** | **• 클래스명 구조: 선생님 코드가 더 간결하고 일관성 있음
• CSS 구조: 선생님 코드가 더 모듈화되고 재사용성 높음**
• 반응형 디자인: 선생님 코드에서 더 고려됨 |
| **개선 제안** | 1. CSS 클래스명을 더 의미있고 일관성 있게 구성
2. 반응형 디자인을 고려한 CSS 작성
**3. CSS 속성의 의미와 영향에 대한 깊이 있는 이해
4. 시맨틱 HTML 구조에 대한 추가 학습** |
| **학습 방향** | • 레이아웃 구성 기술 향상
• 반응형 디자인 학습
• CSS 및 디자인 패턴에 대한 추가 학습 |
| **종합 평가** | 전반적으로 잘 구현됨. CSS와 디자인 패턴 학습을 통해 추가 발전 가능성 높음 |

## 시멘틱 태그

---

시맨틱 HTML 구조는 웹 페이지의 콘텐츠에 의미를 부여하는 방식으로 HTML을 작성하는 것을 말합니다. 이는 웹 페이지의 구조와 의미를 명확하게 전달하여 접근성, 검색엔진 최적화(SEO), 그리고 코드의 가독성을 향상시킵니다.

## 주요 시맨틱 태그와 용도:

| 태그 | 용도 |
| --- | --- |
| `<header>` | 페이지나 섹션의 머리말 |
| `<nav>` | 네비게이션 링크 |
| `<main>` | 페이지의 주요 콘텐츠 |
| `<article>` | 독립적인 콘텐츠 단위 |
| `<section>` | 관련 콘텐츠의 묶음 |
| `<aside>` | 주요 내용과 간접적으로 연관된 내용 |
| `<footer>` | 페이지나 섹션의 꼬리말 |

## 시맨틱 HTML의 장점:

1. 접근성 향상
2. SEO 최적화
3. 코드 가독성 및 유지보수성 개선
4. 기기 간 호환성 증가

## 비시맨틱 vs 시맨틱 예시:

```html
<!-- 비시맨틱 -->
<div class="header">
  <div class="nav">...</div>
</div>
<div class="main-content">...</div>
<div class="footer">...</div>

<!-- 시맨틱 -->
<header>
  <nav>...</nav>
</header>
<main>...</main>
<footer>...</footer>

```

시맨틱 HTML을 사용함으로써, 개발자는 더 의미 있고 구조화된 웹 페이지를 만들 수 있습니다.