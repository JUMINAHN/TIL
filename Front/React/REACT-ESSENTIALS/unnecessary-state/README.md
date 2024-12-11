# [추가] 계산된 값 권장 및 불필요한 State 관리 방지 실습하기

날짜: 2024년 12월 10일

# 계산된 값 권장 및 불필요한 상태 관리 방지의 개념

---

<aside>
💡

계산된 값은 상태로 담지 않고, 일반 변수에 할당하여 사용하는 것이 좋다. 

이 방식은 React의 상태 관리에서 불필요한 복잡성과 성능 저하를 피하는 데 도움이 됩니다. 

</aside>

- React의 상태 관리 및 성능 최적화와 관련된 중요한 원칙입니다.
- 쉽게 설명하기 위해 비유를 사용하여 설명해 보겠습니다.

## 비유: 요리와 재료

---

```jsx
Imagine you are cooking a meal. Let’s use this analogy to understand the concept.
```

## **1. 재료 관리**:

- 요리를 할 때, 필요한 재료는 바로바로 준비해야 합니다. 예를 들어, 볶음밥을 만들 때 쌀과 채소를 준비하는 것처럼요. 하지만, 계속 갓 지은 쌀을 따로 보관하면서, 쌀의 양을 계속 업데이트할 필요는 없습니다. 필요할 때마다 쌀을 다시 만들어 쓰면 됩니다.

## **2. 불필요한 재료 보관**:

- 만약 매번 쌀의 양을 상태로 관리하기 시작하면, 쌀이 얼마인지, 언제 만들어야 하는지를 따로 관리해야 합니다. 이를 통해 혼란스러워지고, 필요하지 않은 상태를 계속 관리하게 됩니다.

## **3. 계산하여 사용할 수 있는 재료**:

- 대신에, 당신이 넣고 싶은 다른 재료들의 양에서 쌀의 양을 계산할 수 있다면? 즉, 채소의 양과 만약 당신이 **항상 1:2 비율로 쌀과 채소를 섞기로 했다면, 채소의 양만으로 쌀의 양을 계산할 수 있습니다. 이 경우 쌀의 양을 따로 관리할 필요가 없습니다.**

## React에서의 적용

---

이 비유를 React의 `state`와 `props`로 되돌아가 보겠습니다.

<aside>
💡

계산된 값 권장 및 불필요한 상태 관리 방지의 원칙은 애플리케이션의 복잡성을 줄이고
성능을 최적화하기 위해 중요합니다.
가능하다면 props나 기존 state로부터 계산 가능한 값은 별도로 state로 관리하지 않고,
필요한 즉시 계산하여 사용하는 것이 좋습니다

</aside>

## 불필요한 상태 관리 예

---

먼저 불필요한 상태 관리의 예를 보겠습니다. 여기서는 `fullName`을 상태로 관리하고 있지만, `firstName`과 `lastName`으로부터 계산이 가능한 경우입니다.

```jsx
import React, { useState } from 'react';

function UserProfile() {
  const [firstName, setFirstName] = useState('John');
  const [lastName, setLastName] = useState('Doe');
  const [fullName, setFullName] = useState('');

  const updateFullName = () => {
    setFullName(`${firstName} ${lastName}`);
  };

  // 사용자가 이름을 변경할 때마다 전체 이름을 업데이트
  const handleFirstNameChange = (event) => {
    setFirstName(event.target.value);
    updateFullName(); // fullName 업데이트
  };

  const handleLastNameChange = (event) => {
    setLastName(event.target.value);
    updateFullName(); // fullName 업데이트
  };

  return (
    <div>
      <input
        type="text"
        value={firstName}
        onChange={handleFirstNameChange}
        placeholder="First Name"
      />
      <input
        type="text"
        value={lastName}
        onChange={handleLastNameChange}
        placeholder="Last Name"
      />
      <h2>Full Name: {fullName}</h2>
    </div>
  );
}

export default UserProfile;

```

위 코드에서 `fullName`은 `firstName`과 `lastName`의 조합으로 만들어져야 합니다. **하지만 매번 입력을 변경할 때마다 `setFullName`을 호출해야 하기 때문에 불필요한 상태 업데이트가 발생**합니다.

# ⚠️개선된 코드 예

---

이제 위 코드를 개선하여 계산된 값을 사용하는 방법을 보여드리겠습니다. `fullName`을 별도의 상태로 관리하지 않고, `firstName`과 `lastName`으로부터 직접 계산합니다.

```jsx
import React, { useState } from 'react';

function UserProfile() {
  const [firstName, setFirstName] = useState('John');
  const [lastName, setLastName] = useState('Doe');

  // fullName을 계산된 값으로 정의
  const fullName = `${firstName} ${lastName}`;

  const handleFirstNameChange = (event) => {
    setFirstName(event.target.value);
  };

  const handleLastNameChange = (event) => {
    setLastName(event.target.value);
  };

  return (
    <div>
      <input
        type="text"
        value={firstName}
        onChange={handleFirstNameChange}
        placeholder="First Name"
      />
      <input
        type="text"
        value={lastName}
        onChange={handleLastNameChange}
        placeholder="Last Name"
      />
      <h2>Full Name: {fullName}</h2>
    </div>
  );
}

export default UserProfile;

```

### 사용 사례와 장점

- **UI 업데이트**: 사용자 입력에 따른 UI 변경이 실시간으로 이루어집니다.
- **성능 향상**: 불필요한 상태 업데이트와 렌더링이 줄어들어 성능이 향상됩니다.
- **유지보수 용이**: 코드가 더 단순해지므로 유지보수가 쉬워집니다.

### 결론

이와 같이 React에서는 가능한 경우 상태를 줄이고, 단순히 기존의 `props`나 `state`를 활용하여 계산된 값을 사용하는 것이 좋습니다. 이는 코드의 가독성을 높이고, 성능을 최적화하는 데 크게 기여합니다.

## 작성 코드

---

```jsx
// UserProfile.js

import { useState } from "react";

//자체 상태관리

function UserProfile() {
  //근데 이것도 input값을 객체로 만드는게 낫지 않는지..? 계산 로직에서
  const [firstName, setFirstName] = useState("")
  const [lastName, setLastName] = useState("")

  const fullName = `${firstName}${lastName}`

  const onChangeFirst = (e) => {
    setFirstName(e.target.value)
  }

  const onChangeLast = (e) => {
    setLastName(e.target.value)
  }

  return (
    <div>
      <h1>User Profile</h1>
      <input type="text" name="" id=""
      value={firstName}
      onChange={onChangeFirst} />
      <input type="text" name="" id="" 
      value={lastName}
      onChange={onChangeLast}/>
      <h2>Check your Full Name! : {fullName}</h2>
    </div>
  );
}

export default UserProfile;
```