# [React] 한입 배어먹는 REACT inferan 9

날짜: 2024년 12월 3일

# `useReducer`와 Vue의 Store 비교

---

### 1. `useReducer`란?

**`useReducer`는 React에서 상태 관리를 위해 사용하는 훅(hook)입니다.** 주로 복잡한 상태 로직을 관리할 때 유용합니다. `useReducer`는 두 가지 주요 요소로 구성됩니다:

- **reducer 함수: 현재 상태와 액션**을 받아 새로운 상태를 반환하는 함수입니다.
- **dispatch 함수: 액션을 발생시켜 상태를 변경**하는 함수입니다.

### 2. Vue의 Store

Vue에서는 Vuex라는 **공식 상태 관리 라이브러리를 사용하여 애플리케이션의 상태를 중앙에서 관리**합니다. Vuex의 store는 상태(state), **변이(mutations)**, 액션(actions) 등으로 구성되어 있습니다.

- **state**: 애플리케이션의 데이터
- **mutations**: 상태를 변경하는 방법
- **actions**: 비동기 작업을 처리하거나 여러 mutations을 호출하는 방법

### 3. 비교

`useReducer`는 Vuex의 mutations과 **비슷하게 작동**합니다. 두 시스템 모두 상태를 변경하기 위해 특정한 규칙(액션 타입)을 따릅니다. 그러나 `useReducer`는 더 간단한 구조를 가지고 있어 **작은 컴포넌트에서 사용하기에 적합**합니다.

## useState와 useReducer 비교하기

---

`useReducer`와 `useState`는 둘 다 React에서 상태 관리를 위한 훅이지만, 각각의 사용 목적과 방식이 다릅니다. 아래에 두 훅의 차이를 표로 정리하고, 예시를 통해 설명하겠습니다.

### `useState`와 `useReducer` 비교

| 특징 | `useState` | `useReducer` |
| --- | --- | --- |
| **목적** | 간단한 상태 관리 | `복잡`한 상태 관리 |
| **구조** | **상태와 상태 변경 함수(setter)를 반환** | **현재 상태와 dispatch 함수를 반환** |
| **상태 업데이트** | `직접`적으로 새로운 값을 설정 | `액션을 dispatch`하여 상태 업데이트 |
| **복잡성** | 간단하고 직관적 | 더 많은 코드가 필요하지만, 복잡한 로직을 처리 가능 |
| **상태 의존성** | 상태가 서로 독립적일 때 사용 | 여러 상태가 서로 의존할 때 사용 |

### 1. `useState` 예시

```jsx
import React, { useState } from 'react';

const CounterWithState = () => {
  const [count, setCount] = useState(0);

  const increment = () => setCount(count + 1);
  const decrement = () => setCount(count - 1);

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
    </div>
  );
};

export default CounterWithState;

```

### 2. `useReducer` 예시

```jsx
import React, { useReducer } from 'react';

const reducer = (state, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    case 'DECREMENT':
      return { count: state.count - 1 };
    default:
      return state;
  }
};

const CounterWithReducer = () => {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <div>
      <h1>{state.count}</h1>
      <button onClick={() => dispatch({ type: 'INCREMENT' })}>+</button>
      <button onClick={() => dispatch({ type: 'DECREMENT' })}>-</button>
    </div>
  );
};

export default CounterWithReducer;

```

### 설명

- *`useState`*는 간단한 카운터를 구현하는 데 적합합니다. 각 버튼 클릭 시 직접적으로 상태를 변경합니다.
- *`useReducer`*는 더 복잡한 로직을 처리할 수 있습니다. **여기서는 `dispatch` 함수를 사용하여 액션을 발생시키고, 해당 액션에 따라 상태를 업데이트**합니다. 이 방식은 **여러 액션을 처리**해야 할 때 유용합니다.

### 언제 어떤 것을 사용할까?

- **간단한 상태 관리**: `useState`
- **복잡한 상태 로직이나 여러 액션을 처리해야 할 때**: `useReducer`

이렇게 두 훅은 각각의 장점을 가지고 있으며, 상황에 따라 적절히 선택하여 사용할 수 있습니다. 이해가 잘 되셨나요? 추가 질문이 있다면 언제든지 말씀해 주세요!

# `reducer` 동작 방식 이해하기

---

### 1. 초기값과 reducer

- **초기값**: `useReducer(reducer, 0)`에서 `0`은 상태의 초기값입니다.
- **reducer 함수**: 이 함수는 **현재 상태와 액션을 받아 새로운 상태를 계산합**니다. 예를 들어, 사용자가 버튼을 클릭하면 `dispatch`가 호출되고, 그에 따라 reducer가 실행되어 새로운 상태가 반환됩니다.

### 2. dispatch의 의미

- **dispatch**: 액션을 발생시키는 함수입니다. 예를 들어, `dispatch({ type: "INCREASE", data: 1 })`는 "INCREASE"라는 타입과 함께 데이터를 전달하여 상태를 증가시키라는 신호를 보냅니다.

### 3. 액션과 타입

- **액션(action): 상태를 변경하기 위한 정보입**니다. `{ type: "INCREASE", data: 1 }`에서 `type`은 **어떤 종류의 변화를 원하는지**를 나타내고, `data`는 그 변화에 필요한 추가 정보를 제공합니다.
- **타입(type)**: 문자열로, 어떤 작업을 수행할지를 정의합니다. 이는 개발자가 정해주는 것이며, 자유롭게 설정할 수 있지만 일관성을 유지하는 것이 중요합니다.

## 요약

- `useReducer`는 React에서 복잡한 상태 관리를 위한 훅으로, Vuex의 mutations과 비슷한 역할을 합니다.
- 초기값은 컴포넌트가 처음 렌더링될 때 사용할 기본값이며, reducer 함수는 이 값을 기반으로 새로운 상태를 계산합니다.
- dispatch는 액션을 발생시키고, 액션은 어떤 변화를 원하는지를 정의하는 객체입니다.