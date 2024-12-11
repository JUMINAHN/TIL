# [추가] 교차 State 실습해보기

날짜: 2024년 12월 10일

# 교차 State란?

---

<aside>
💡

**"한 번에 하나의 상태만 가능한 경우"는 여러 옵션 중에서 반드시 하나만 선택되어야 하는 상황**

- Yes/No가 아닌 여러 선택지 중 하나를 선택해야 할 때
- 여러 상태가 동시에 true가 되면 안 되는 경우
- 상태들이 `서로 배타적`(mutually exclusive)일 때 유용합니다

이렇게 하면 실수로 여러 상태가 동시에 활성화되는 것을 방지할 수 있습니다.

</aside>

- 교차 State는 여러 개의 상태가 서로 연관되어 있고 `동시에 발생하면 안 되는 상황에서 사용`하는 상태 관리 패턴입니다.

## 주요 사용 사례

---

- 데이터 로딩 상태 (로딩중/완료/에러)
    
    ```jsx
    // ❌ 잘못된 방식: 서로 충돌할 수 있는 상태들
    const [isLoading, setIsLoading] = useState(false);
    const [isError, setIsError] = useState(false);
    const [isSuccess, setIsSuccess] = useState(false);
    
    // ✅ 올바른 방식: 상호 배타적인 상태를 하나로 관리
    const [status, setStatus] = useState('idle');
    
    ```
    
- 모달 창 관리 (로그인/회원가입/설정)
    
    ```jsx
    // ❌ 잘못된 방식
    const [isLoginModal, setIsLoginModal] = useState(false);
    const [isSignupModal, setSignupModal] = useState(false);
    
    // ✅ 좋은 방식
    const [modalType, setModalType] = useState(null); // null | 'login' | 'signup'
    
    ```
    
- 폼 제출 상태 (대기/제출중/완료/실패)
    
    ```jsx
    // ❌ 잘못된 방식
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [isSubmitted, setIsSubmitted] = useState(false);
    const [hasError, setHasError] = useState(false);
    
    // ✅ 올바른 방식
    const [formStatus, setFormStatus] = useState('initial'); // 'initial' | 'submitting' | 'submitted' | 'error'
    
    ```
    
- 라디오 버튼이나 단일 선택 옵션
    
    ```jsx
    // ❌ 잘못된 방식
    const [isOption1, setIsOption1] = useState(false);
    const [isOption2, setIsOption2] = useState(false);
    const [isOption3, setIsOption3] = useState(false);
    
    // ✅ 좋은 방식
    const [selectedOption, setSelectedOption] = useState(null); // null | '1' | '2' | '3'
    
    ```
    

## 교차 State를 사용하는 이유

---

<aside>
💡

- 교차 State 방지는 **"한 번에 하나의 상태만 가능한 경우"에 특히 유용**합니다.
- 여러 개의 boolean 값으로 관리하면 발생할 수 있는 논리적 모순을 하나의 상태 값으로 관리함으로써 방지할 수 있습니다.
</aside>

| 상황 | 해결 방법 |
| --- | --- |
| 상태 모순 | 단일 진실 공급원 사용 |
| 중복 상태 | 파생 상태 사용 |
| 연관 상태 | 객체로 그룹화 |
- 코드가 더 예측 가능해집니다
- 상태 관리가 단순해집니다
- 버그 발생 가능성이 줄어듭니다
- 유지보수가 더 쉬워집니다

# 예제

---

```jsx
// App.js
import { useState } from 'react';

function App() {
  // 잘못된 방식의 상태 관리
  const [isLoading, setIsLoading] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);
  const [isError, setIsError] = useState(false);

  // 올바른 방식의 상태 관리
  const [fetchStatus, setFetchStatus] = useState('idle');

  const handleBadFetch = () => {
    // 잘못된 방식의 상태 변경
    setIsLoading(true);

    setTimeout(() => {
      // 이런 상황에서 실수로 둘 다 true가 될 수 있음
      setIsLoading(false);
      setIsSuccess(true);
      setIsError(true); // 논리적 모순 발생!
    }, 2000);
  };

  const handleGoodFetch = () => {
    // 올바른 방식의 상태 변경
    setFetchStatus('loading');

    setTimeout(() => {
      // 한 번에 하나의 상태만 가능
      setFetchStatus('success');
      // 또는 setFetchStatus('error');
    }, 2000);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>교차 State 실습</h2>

      <div style={{ marginBottom: '40px' }}>
        <h3>잘못된 방식</h3>
        <button onClick={handleBadFetch}>데이터 가져오기</button>
        <p>로딩 중: {isLoading.toString()}</p>
        <p>성공: {isSuccess.toString()}</p>
        <p>에러: {isError.toString()}</p>
      </div>

      <div>
        <h3>올바른 방식</h3>
        <button onClick={handleGoodFetch}>데이터 가져오기</button>
        <p>현재 상태: {fetchStatus}</p>
      </div>
    </div>
  );
}

export default App;

```

```jsx
//올바른 방식만 
import { useState } from 'react';

function App() {
  // 올바른 방식의 상태 관리
  const [fetchStatus, setFetchStatus] = useState('idle');

  const handleGoodFetch = () => {
    // 올바른 방식의 상태 변경
    setFetchStatus('loading');

    setTimeout(() => {
      // 한 번에 하나의 상태만 가능
      setFetchStatus('success');
      // 또는 setFetchStatus('error');
    }, 2000);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>교차 State 실습</h2>

      <div>
        <h3>올바른 방식</h3>
        <button onClick={handleGoodFetch}>데이터 가져오기</button>
        <p>현재 상태: {fetchStatus}</p>
      </div>
    </div>
  );
}

export default App;

```

이 예제에서는:

1. 잘못된 방식으로 여러 개의 boolean 상태를 사용하는 경우
2. 올바른 방식으로 하나의 문자열 상태를 사용하는 경우

를 비교해볼 수 있습니다. 버튼을 클릭하면 각각의 방식으로 상태가 어떻게 변하는지 확인할 수 있습니다. 특히 잘못된 방식에서는 여러 상태가 동시에 true가 되는 모순된 상황이 발생할 수 있음을 보여줍니다.

## 작성 코드

---

```jsx
import { useState } from 'react';

function App() {
  //상태에 따라 변경 => 기본
  const [nowState, setNowState] = useState("not Connect") //지금 일단 상태가 없음
  //로딩중
  //성공
  //에러
  const onClickBtn = () => {
    setNowState("로딩 중...")

    //뭐 예를 들면 useEffect가 실행이 완료되었다면?
    setTimeout(
      () => {
      console.log('접속 진행중')
      setNowState('접속 완료') // 접속완료
    }, "3000") //3초 뒤 
  }

  return (
    <div>
      <h1>교차 State 실습</h1>
        <button
        onClick={onClickBtn}>활성화 버튼</button>
      <h5>현재 상태 : {nowState}</h5>
    </div>
  );
}

export default App;

```