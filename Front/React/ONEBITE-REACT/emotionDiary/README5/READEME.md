# [React] 감정 일기장 복습5_Edit 페이지

날짜: 2024년 12월 9일

# Edit Page

---

## 삭제 태그 추가 후 새 일기 쓰기 버튼이 먹통되는 문제
[에러] Editor.jsx:28 Uncaught TypeError: Cannot read properties of undefined (reading 'find') at findData (Editor.jsx:28:26)
at Editor (Editor.jsx:36:21)

---

```jsx
const findData = (params, data) => { //id를 기반으로 일치값 찾기
  const innerData = data.find((item) => String(item.id) === String(params.id))
  return innerData
}
```

⇒ edit 페이지에서만 Mount 되면 되는데 현재 지금 New page파트에서도 랜더링 되기 때문에 문제가 생김

[editor.jsx]

```jsx
  if (params) {
    const innerData = findData(params, data) //무작정 실행이 되니까
    console.log(innerData, 'undefined')
  } //근데 굳이 params를 if로 묶을 필요가 없음 => 없으면 없는대로 undefined
  //아님 => findData 메서드가 실행되기 때문에 if문으로 감싸주는게 맞음
```

[그 중 input 태그 설정과 관련됨]

- 삼항 연산자 쓰면 되지 않을까?

```jsx
  const [input, setInput] = useState({ //여러 데이터 한꺼번에 전달
    //date, diary, emotion값 한꺼번에 저장하는 방식 => 기존 데이터 받아왔고
    id : innerData.id, 
    createdDate : new Date(innerData.createdDate), //new Date(), // 
    emotionId : innerData.emotionId, //"", //
    content : innerData.content //임시, "" //
  })
```

<aside>
💡

**수정 사항**

</aside>

```jsx
  const [input, setInput] = useState({ //여러 데이터 한꺼번에 전달
    //date, diary, emotion값 한꺼번에 저장하는 방식 => 기존 데이터 받아왔고
    id : params ? innerData.id : "", 
    createdDate : params ? new Date(innerData.createdDate) : new Date(), //new Date(), // 
    emotionId : params ? innerData.emotionId : "", //"", //
    content : params ? innerData.content : "" //임시, "" //
  })

```

⇒ 이렇게 되면 또 innerData를 찾을 수 없다고 함 : params를 못받아옴

⇒ `let` 으로 바꿔줘서 사용할 수 있게 함

```jsx
  let innerData
  if (params) {
    innerData = findData(params, data) //무작정 실행이 되니까
    console.log(innerData, 'undefined')
  } 
```

## 수정 버튼 에러
[에러] Editor.jsx?t=1733706864746:52 Uncaught TypeError: Cannot read properties of undefined (reading 'id')
at Editor (Editor.jsx?t=1733706864746:52:28)

---

- id를 읽을 수 없다

## [에러] chunk-MVRAC76T.js?v=2b17de0d:3754 Uncaught TypeError: onSubmit is not a function at onClickBtn (Editor.jsx:68:5)

---

- 뭐지 왜 안될까 ⇒ id값 때문에 연동되어서 안됨

## [오류] 에러는 해결하였으나 update값이 반영되지 않음

---

[Edit.Component[

```jsx
  const onSubmit = (input) => {//타임스탬프 형식
    onUpdate((input.createdDate).getTime(), input.emotionId, input.content, params.id)
    nav('/', {replace : true})
  }
```

- 다시 하니까 된다 ⇒ 뭐지..? ⇒ 타임스탬프의 문제였을까 ⇒ 동일하다
- 저장의 문제

# 작성 데이터 및 선생님 데이터 비교

---

- **Edit.jsx**
    
    ```jsx
    import { replace, useNavigate, useParams } from "react-router-dom"
    import Header from "../components/Header"
    import Button from "../components/Button"
    import Editor from "../components/Editor"
    import { useContext } from "react"
    import { DiaryDispatchContext, DiaryStateContext } from "../App"
    
    const Edit = () => {
      const params = useParams()
      const nav = useNavigate()
      const data = useContext(DiaryStateContext)
      const {onUpdate, onDelete} = useContext(DiaryDispatchContext) //onDelete를 여기서 호출하는게 아니라 내부적으로 활용할 것
      // console.log(params) //params는 id값을 가진다.
    
      //params로 받았는데 일치하는 emotionId, emotionName, Date, diary 를 매칭해서 활용할 필요가 있지 않을까?
      //=> 매칭을 하려면..? => status가 editor에 존재
    
      const onClickDelete = () => {
        //정말로 삭제할까요?
        if (window.confirm("정말 삭제할까요?")) {
          onDelete(params.id) //params를 전해준다. => 확인
          nav('/', {replace : true}) //삭제 완료 => 삭제되는 것을 볼 수 있음
        }
      }
    
      const onSubmit = (input) => {//타임스탬프 형식
        // onUpdate((input.createdDate).getTime(), input.emotionId, input.content, params.id)
        if (window.confirm('정말 수정할까요?')) {
          onUpdate((input.createdDate).getTime(), input.emotionId, input.content, params.id)
          nav('/', {replace : true})
        }
      }
    
      //params 기반으로 그냥 삭제 onDelete 실행해주면 됨
      return (
        <div>
          <Header text={"일기 수정하기"}
          leftChild={<Button text={"< 뒤로 가기"}
          onClick={() => nav(-1)}/>}
          rightChild={<Button text={"삭제하기"} type={"NEGATIVE"}
          onClick={onClickDelete}/>}></Header>
          <Editor
          data={data}
          params={params}
          onSubmit={onSubmit}/>
          {/* <p>{params.id}번 Edit입니다.</p> */}
        </div>
      )
    }
    
    export default Edit
    ```
    
- **Editor.jsx**
    
    ```jsx
    import { emotionData } from '../util/get-matching-image'
    import Button from './Button'
    import EmotionItem from './EmotionItem'
    import './Editor.css'
    import { useState } from 'react'
    import { useNavigate } from 'react-router-dom'
    
    const changeFormatter = (date) => { 
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
    
    //input값을 기반으로 매칭 => input => 근데 input값? => 들어있는가? : New에서 있었던 것..? => 그냥 data자체에서 매칭시켜야할 것 같은데
    const findData = (params, data) => { //id를 기반으로 일치값 찾기
      const innerData = data.find((item) => String(item.id) === String(params.id))
      return innerData
    }
    
    const Editor = ({onSubmit, params, data}) => {
      // console.log(params, 'Edit의 경우')
      // console.log(data, '기존 데이터 내역')
      //이제 params와 일치되는 것을 input에 넣어주면 되지 않을까?
    
      let innerData
      if (params) {
        innerData = findData(params, data) //무작정 실행이 되니까
        // console.log(innerData, 'undefined')
      } 
    
      const nav = useNavigate()
      const [input, setInput] = useState({ //여러 데이터 한꺼번에 전달
        //date, diary, emotion값 한꺼번에 저장하는 방식 => 기존 데이터 받아왔고
        // id : params ? innerData.id : "", 
        createdDate : params ? new Date(innerData.createdDate) : new Date(), //new Date(), // 
        emotionId : params ? innerData.emotionId : "", //"", //
        content : params ? innerData.content : "" //임시, "" //
      })
    
      //onClickEvent도 전체 통합
      const onChangeInput = (e) => {
        let name = e.target.name
        let value = e.target.value
        if (name === "createdDate") {//생성날짜가 name값이면
          value = new Date(value) //새로운 밸류 == 생성된 날짜가 문자일 수 있기 때문에 => new Entry
        }
        setInput({
          ...input, 
          //이름에 따라 필터링
          [name] : value //또 여기에 있는 애가 문자로 저장 될 것
        })
      }
    
      //일단 create기준
      const onClickBtn = () => {
        onSubmit(input) //그냥 입력값 자체를 전달한다.
      }
    
      // 사실 지금 하나로 통합하는 것 뿐 아까랑 다를건 없음
      return (
        <div className='Editor'>
          <section className='date_section'>
            <h4 className='Editor_Date_Title'>오늘의 날짜</h4>
            <input className='Editor_Date_Input' type="date" 
            // nametag도 연결시켜서 => formatter 가능하게.. 
            value={changeFormatter(input.createdDate)} onChange={onChangeInput} name="createdDate" id="" />
          </section>
    
          <section className='emotion_section'>
            <h4>오늘의 감정</h4>
            <div className="emotion_list_wrapper">
              {emotionData.map((item) => 
              <EmotionItem
              value={input.emotionId}
              onClick={() => onChangeInput({//changeInput이 가능한 것 처럼 만들기
                // 기존 onChange가 전달하는 내용을 target으로 바꾼 것 뿐
                target : {
                  name : "emotionId",
                  value : item.emotionId
                },
              })}
              isSelected={item.emotionId === input.emotionId}
              key={item.emotionId}
              {...item}/>)}
            </div>
          </section>
    
          <section className='content_section'>
            <h4 className='Editor_Diary_Title'>오늘의 일기</h4>
            <textarea className='Editor_Diary_Input' 
            value={input.content} onChange={onChangeInput}
            name="content" id="" placeholder='오늘은 어땠나요?'></textarea>
          </section>
    
          <section className='button_section'>
            <Button text={"취소하기"}
            onClick={() => {nav('/')}}/>
            <Button text={"작성 완료"}
            // onCreate 호출
            onClick={onClickBtn}
            type={"POSITIVE"}/>
          </section>
        </div>
      )
    }
    export default Editor
    ```
    

```jsx
      <Editor //신경쓰였던 부분
      data={data} //이부분으로 통합가능하지 않을까
      params={params}
      onSubmit={onSubmit}/>
```

>> 접근

## [에러] Edit.jsx:24 You should call navigate() in a React.useEffect(), not when your component is `first rendered. Error Component Stack`

---

```jsx
  const findData = () => { //id를 기반으로 일치값 찾기
    const innerData = data.find((item) => String(item.id) === String(params.id))
    if(!innerData) {
      //없다면
      window.alert('존재하지 않는 일기입니다.')
      nav('/', {replace : true})
    }
    return innerData
  }
  ...
const currentDiaryItem = findData() //이거 때문에
```

→ 첫번째 랜더링할때 데이터를 받아올 수 없다 : `화면에 그려지기 전`이다. useEffect를 활용해라

⇒ `BrowserRouter` 를 불러오기전에 호출하면 안됨

<aside>
💡

수정 사항

</aside>

```jsx
  useEffect(()=>{
    const innerData = data.find((item) => String(item.id) === String(params.id))
    if(!innerData) {
      //없다면
      window.alert('존재하지 않는 일기입니다.')
      nav('/', {replace : true}) //여기
    }
    return innerData
  }, [data, params.id]) //이렇게? => data랑 params.id가 변경되니까
  //hint도 줬음 : vscode
```

⇒ `useEffect Data` 저장할 곳

## 추가적으로 삼항 연산자가 아닌 useEffect를 사용하여 data 추적

---

```jsx
  useEffect(()=> { //input자체에 넣겠다는 뜻?
    setInput({
      new Date(data.createdDate),
      data.emotionId,
      data.content,
    })
  }, [data]) //데이터가 변경될 때 마다

```

## [오류] chunk-MVRAC76T.js?v=2b17de0d:9174 Uncaught TypeError: Cannot read properties of undefined (reading 'createdDate')
    at Editor.jsx:52:42

---

```jsx
 createdDate : new Date(Number(data.createdDate)) //오류
```

⇒ 여기서 오류 : data는 undefined

**[editor.jsx]**

```jsx
  useEffect(()=>{
    const innerData = data.find((item) => String(item.id) === String(params.id))
    console.log(innerData, 'innerData?')
    if(!innerData) {
      //없다면
      window.alert('존재하지 않는 일기입니다.')
      nav('/', {replace : true}) //여기
    }
    setCurrentDiaryItem(innerData)
    //저장할 곳
    console.log(currentDiaryItem, 'CurrentDiaryItem 들어갔니? == 안들어감')
  }, [data, params.id]) //data랑 params.id는 변경되니까
```

⇒ 여기서 보면 set으로 데이터가 안들어가짐 : 강의 교안이랑 똑같은데,,?

```jsx
  useEffect(()=> { //input자체에 넣겠다는 뜻?
    //data가 있을떄만 진행하게
    if (data) {
      console.log(data, 'data')
      console.log(data.createdDate, 'date?')
      setInput({
        //굳이 렇게 쓸필요 없이 ...data로 넘겨주면 됨
        ...data,
        createdDate : new Date(Number(data.createdDate)) //오류
        // new Date(data.createdDate),
        // data.emotionId,
        // data.content,
      })
    }
  }, [data]) //데이터가 변경될 때 마다
```

⇒ 무작정 실행하는게 아니라 data가 있을때만 실행하도록 하는 것 : 이 부분 이해하기

## 궁금한 점

---

## 1. onSubmit의 렌더링 지연 문제:

---

onSubmit 함수의 렌더링이 늦어지는 이유는 여러 가지가 있을 수 있습니다:

a) **데이터 업데이트와 네비게이션이 비동기적**으로 일어나기 때문입니다. 

onUpdate 함수가 완료되기 전에 네비게이션이 실행될 수 있습니다.

b) **React의 상태 업데이트와 렌더링 사이클 때문에 즉시 반영되지 않을 수 있습니다.**

이를 해결하기 위해, useEffect를 사용하여 데이터 업데이트 후 네비게이션을 수행할 수 있습니다:

```jsx
useEffect(() => {
  if (updateCompleted) {
    nav('/', {replace: true});
  }
}, [updateCompleted]);

const onSubmit = (input) => {
  if (window.confirm('정말 수정할까요?')) {
    onUpdate((input.createdDate).getTime(), input.emotionId, input.content, params.id);
    setUpdateCompleted(true);
  }
}

```

## 1-1. 자세히 이해해보기

---

1. onSubmit 함수의 경우:
    - `onUpdate 함수`는 일반적으로 `데이터베이스나 서버와의 통신을 포함`할 가능성이 높습니다.
    - 이러한 작업은 `비동기적`으로 실행되며, 완료되기까지 시간이 걸릴 수 있습니다.
    - 따라서 **onUpdate가 완료되기 전에 nav('/')가** 실행될 수 있어, 데이터 업데이트가 완전히 반영되기 전에 페이지가 이동할 risk가 있습니다.
2. onClickDelete 함수의 경우:
    - onDelete 함수는 상대적으로 간단한 작업일 가능성이 높습니다 **(예: 로컬 상태에서 항목 제거).**
    - 이 경우 작업이 즉시 완료되므로, nav('/')를 바로 호출해도 문제가 없을 수 있습니다.

그러나, **일관성을 위해 두 경우 모두 useEffect를 사용하는 것**이 좋습니다. 예를 들어:

```jsx
const [isDeleting, setIsDeleting] = useState(false);
const [isUpdating, setIsUpdating] = useState(false);

useEffect(() => {
  if (isDeleting || isUpdating) {
    nav('/', {replace: true});
  }
}, [isDeleting, isUpdating]);

const onClickDelete = () => {
  if (window.confirm("정말 삭제할까요?")) {
    onDelete(params.id);
    setIsDeleting(true);
  }
}

const onSubmit = (input) => {
  if (window.confirm('정말 수정할까요?')) {
    onUpdate((input.createdDate).getTime(), input.emotionId, input.content, params.id);
    setIsUpdating(true);
  }
}

```

이렇게 하면 두 경우 모두 일관된 방식으로 처리되며, 비동기 작업의 완료를 더 안전하게 다룰 수 있습니다.

## ⚠️ 1-2. useEffect 사용가이드

---

| **상황** | **설명** | **예시 코드** |
| --- | --- | --- |
| **1. 데이터 페칭** | **API 호출이나 데이터베이스 쿼리** 등 외부 데이터를 가져올 때 | `javascript useEffect(() => { fetchData(); }, []);` |
| **2. 구독 설정 및 해제** | 웹소켓 연결이나 이벤트 리스너 등을 설정하고 해제할 때 | `javascript useEffect(() => { const subscription = subscribe(); return () => unsubscribe(subscription); }, []);` |
| **3. DOM 조작** | **직접적인 DOM 조작이 필요한 경우** | `javascript useEffect(() => { document.title = `${count} new messages`; }, [count]);` |
| **4. 타이머 설정** | `setTimeout`이나 `setInterval`을 사용할 때 | `javascript useEffect(() => { const timer = setInterval(() => { // 작업 }, 1000); return () => clearInterval(timer); }, []);` |
| **5. 상태 변화에 따른 부수 효과** | **특정 상태가 변경될 때 다른 상태나 작업을 업데이트**해야 하는 경우 | `javascript useEffect(() => { if (user) setProfile(user.profile); }, [user]);` |
| **6. 컴포넌트 마운트/언마운트 시 작업** | **컴포넌트가 처음 렌더링되거나 제거될 때 특정 작업 수행** | `javascript useEffect(() => { console.log('Mounted'); return () => console.log('Unmounted'); }, []);` |
| **7. 비동기 작업 처리** | `Promise`나 `async/await`를 사용하는 비동기 작업을 다룰 때 | `javascript useEffect(() => { async function fetchData() { // 비동기 작업 } fetchData(); }, []);` |
| **8. 성능 최적화** | **불필요한 re-render를 방지하기 위해 특정 값들의 변화만 감지**하고 싶을 때 | `javascript useEffect(() => { // 특정 값 변화만 감지 }, [specificValue]);` |
| **9. 브라우저 API 사용** | **`localStorage`, `sessionStorage` 등 브라우저 API를 사용할 때** | `javascript useEffect(() => { localStorage.setItem('key', value); }, [value]);` |
| **10. 라우팅 변경에 따른 작업** | URL 파라미터 변경 시 데이터를 다시 불러오는 등의 작업 | `javascript useEffect(() => { if (id) fetchUserData(id); }, [id]);` |

이 표는 `useEffect`를 사용할 때 고려해야 할 다양한 상황과 그에 따른 예시 코드를 포함하고 있습니다.

## 2. params를 받아오는 방식:

---

- useEffect를 사용하는 것이 더 효과적일 수 있습니다. 이유는 다음과 같습니다:

a) 컴포넌트 마운트 시 한 번만 실행되므로 **불필요한 재계산을 방지**합니다.
b) 비동기 작업을 처리하기에 더 적합합니다.
c) 코드의 가독성과 유지보수성이 향상됩니다.

useEffect를 사용한 예시:

```jsx
const [input, setInput] = useState({
  createdDate: new Date(),
  emotionId: "",
  content: ""
});

useEffect(() => {
  if (params && innerData) {
    setInput({
      createdDate: new Date(innerData.createdDate),
      emotionId: innerData.emotionId,
      content: innerData.content
    });
  }
}, [params, innerData]);

```

이렇게 하면 컴포넌트가 마운트될 때 한 번만 실행되며, params나 innerData가 변경될 때만 input 상태를 업데이트합니다.

### 2-1. 기존 코드 vs useEffect 비교

| 구분 | 기존 코드 | useEffect 방식 | 차이점 |
| --- | --- | --- | --- |
| **실행 시점** | 컴포넌트 초기 렌더링 시 **한 번만** 실행 | 컴포넌트 마운트 후 + 의존성 값 변경 시 실행 | 🔄 반응성 향상 |
| **상태 업데이트** | 정적인 초기 상태 설정 | **`동적`으로 상태 변경 가능** | 🔍 더 유연한 상태 관리 |
| **코드 구조** | 조건부 로직과 상태 설정 혼합 | 관심사 분리, 로직 명확화 | 📝 가독성 개선 |
| **에러 처리** | **undefined 위험 존재** | 안전한 조건부 처리 | 🛡️ 안정성 증가 |
| **비동기 처리** | 제한적 | **비동기 데이터 쉽게 처리** | 🔀 유연한 데이터 로딩 |

### 🚨 주의사항

- 과도한 useEffect 사용은 성능에 영향
- 의존성 배열 관리 중요
- 불필요한 렌더링 방지 필요

## 종합 비교

---

| **구분** | **당신의 코드** | **선생님의 코드** | **차이점/장점** |
| --- | --- | --- | --- |
| **관심사 분리** | Edit 컴포넌트에서 데이터 fetching과 UI 렌더링 모두 처리 | Edit는 데이터 fetching, Editor는 UI 렌더링과 입력 처리 | **재사용성과 유지보수성 향상** |
| **`useEffect` 활용** | 초기 상태에서 params 기반으로 데이터 설정 | useEffect를 사용하여 데이터 fetching 및 상태 업데이트 | **side effect 관리를 더욱 명확하**게 처리 |
| **`에러` 처리** | 데이터가 존재하지 않는 경우 에러 처리 없음 | 존재하지 않는 일기 데이터에 대한 에러 처리 포함 | **사용자 경험 향상** |
| **`상태` 관리** | input 상태를 직접 관리 | currentDiaryItem이라는 별도의 상태로 관리 | 데이터 흐름을 명확하게 하고, **가독성 향상** |

## ⚠️ 개선 및 학습 방향

| **개선 사항** | **설명** |
| --- | --- |
| **`useEffect` 이해** | React의 핵심 개념으로, side effect 관리 능력 향상 |
| **`책임` 분배 고민** | 각 컴포넌트에 단일 책임을 부여하여 설계 최적화 |
| **`에러` 처리 고민** | 사용자 경험 개선을 위한 체계적인 에러 처리 접근 필요 |
| **`상태 관리` 패턴 학습** | React의 다양한 상태 관리 패턴에 대한 추가 학습 필요 |
- **관련 내용**
    1. useEffect 이해
        - 목적: 컴포넌트의 생명주기와 관련된 side effects를 관리
        - 기본 구조: `useEffect(() => { /* effect */ }, [/* dependencies */])`
        - 주요 사용 사례:
            - **데이터 페칭**
            - 구독 설정/해제
            - **DOM 수동 조작**
        - 클린업 함수: `return () => { /* cleanup */ }`로 리소스 정리
    2. 책임 분배 고민
        - **단일 책임 원칙 (SRP) 적용**
        - 컴포넌트 분류:
            - 컨테이너 컴포넌트: 데이터 관리, 상태 로직
            - 프레젠테이셔널 컴포넌트: UI 렌더링
        - Props를 통한 데이터 및 함수 전달
        - **Custom Hooks를 사용한 로직 분리**
    3. 에러 처리 고민
        - try-catch 구문 활용
        - Error Boundaries 컴포넌트 사용
        - **조건부 렌더링으로 에러 상태 표시**
        - **사용자 친화적인 에러 메시지 제공**
        - 로깅 시스템 구축 (개발자용)
    4. 상태 관리 패턴 학습
        - **Local State: useState Hook**
        - Lifting State Up: 부모 컴포넌트로 상태 끌어올리기
        - **Context API: 전역 상태 관리**
        - **Redux: 복잡한 애플리케이션의 상태 관리**
        - Recoil, Jotai 등 새로운 상태 관리 라이브러리 탐색
    
    각 영역에 대해 더 깊이 있는 학습이 필요하다면 추가 질문해 주세요.
    

## 종합 피드백

| **피드백** | **설명** |
| --- | --- |
| **올바른 방향으로 나아가고 있음** | React의 기본 개념 이해와 기능적 구현 잘 수행하고 있음 |
| **효율적이고 유지보수가 용이한 코드 작성 노력 필요** | 위에서 언급한 개선 사항들을 반영하여 발전 필요 |