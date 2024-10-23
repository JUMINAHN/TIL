# [실습/참고] Reference Type1

날짜: 2024년 10월 23일

# 전개구문 활용 및 이해하기 예시

---

```jsx
    //함수에서 역할 두가지 == p.24 
    // 1. 인자 확장 (함수 호출 시)
    let numbers = [1, 2, 3]
    let numbers2 = [1,2]
    function myFunc(x, y, z) {
      return x + y + z
    }

    console.log(myFunc(numbers[0], numbers[1], numbers[2])) //원래 인자를 이런식으로 썻어야했는데
    //하지만 전개 구문 활용을 통해 바꿈
    -----------------------------------------------------------------
    console.log(myFunc(...numbers))
    console.log(myFunc(...numbers2)) //NaN으로 출력됨

    function myfunc(x, y, z) {
      return [x, y, z]
    }
    console.log(myfunc(...numbers))
    console.log(myfunc(...numbers2)) //개수가 맞지 않았을 때 더하기가 안됨
    //1,2,undefined => 즉 더할 수 없기 떄문에 NaN이 나온다.

    // 2. 나머지 매개변수 (함수 선언 시)
    const myFunc2 = function (a1, a2, ...restParams) { //...으로 표기
      return [a1, a2, restParams]
    }
    console.log(myFunc2(1, 2, 3, 4, 5)) // [1, 2, [3, 4, 5]]
    console.log(myFunc2(1, 2)) // [1, 2, []]
```

## 전개 구문 (Spread Syntax) : 함수 `호출시` → 관련 유형 다뤄봐야할듯?

---

- 전개 구문은 `배열이나 객체의 요소를 개별적으로 분리`하여 함수 호출, 배열 리터럴, 객체 리터럴 등에서 사용할 수 있도록 해준다.
- 전개 구문은 `...`을 사용하여 표현된다

### 사용 예시

1. **배열의 요소를 함수의 개별 인자로 전달**:
    
    ```jsx
       let numbers = [1, 2, 3]
        function myFunc(x, y, z) {
          return x + y + z
        }
    
     //console.log(myFunc(numbers[0], numbers[1], numbers[2])) //원래 인자를 이런식으로 
     console.log(myFunc(...numbers)) //[1,2,3] 이라는 배열
     //매개 인수 부족이 NaNㅂ반환
    
    ```
    

## 나머지 매개변수 (Rest Parameters)

---

- 나머지 매개변수는 함수 정의에서 여러 개의 인자를 하나의 배열로 수집할 때 사용
- 나머지 매개변수도 `...`을 사용하여 표현

### 사용 예시

1. **함수에서 가변 인자 수 처리**:
    
    ```jsx
        const myFunc2 = function (a1, a2, ...restParams) { //...으로 표기
          return [a1, a2, restParams]
        }
        console.log(myFunc2(1, 2, 3, 4, 5)) // [1, 2, [3, 4, 5]]
        console.log(myFunc2(1, 2)) // [1, 2, []]
    ```
    

## 차이점 요약

---

| **전개 구문 (Spread Syntax)** | **나머지 매개변수 (Rest Parameters)** |
| --- | --- |
| 배열이나 객체의 요소를 개별적으로 분리 | 여러 인자를 배열로 수집 |
| 주로 함수 호출 시 인자를 확장하거나 배열/객체를 병합할 때 사용 | 함수 정의에서 가변 인자 수를 처리할 때 사용 |
| 사용 위치: 함수 호출 시 또는 배열/객체 리터럴 내 | 사용 위치: 함수 정의 내 |

# 화살표 작성 예시

---

```jsx
    const arrow1 = function (name) {
      return `hello, ${name}`
    }
    // 1. function 키워드 삭제 후 화살표 작성
    const arrow2 = (name) => {
      return `hello, ${name}`
    } // `=`도 주의할 것

    // 2. 인자의 소괄호 삭제 (인자가 1개일 경우에만 가능)
    const arrow3 = name => {return `hello, ${name}`}

    // 3. 중괄호와 return 삭제 (함수 본문이 return을 포함한 표현식 1개일 경우에만 가능)
    const arrow4 = name => `hello, ${name}`
```

# 함수 선언 후 반환값 → undefined가 뜰 때

---

- return 값에 `console.log` 출력 여부 확인하기

```jsx
    const isValid = function(sth) {
      if (sth.length >= 8) {
        return true //반환값을 전달하는데 console.log를 전달할 필요가 없다 == undefined가 뜸
      } else {
        return false
      }
    }
```

# 정수로 이루어진 배열 인자를 받아서 모든 요소를 합한 값으로 반환

---

[초기 코드 작성]

```jsx
    /*
      정수로 이루어진 배열의 인자로 받아 모든 요소를 합한 값을 반환하는 함수 totalOfArrays 함수를 작성하시오.
      - 함수 표현식으로 작성한다.
    */
    const totalOfArrays = function(...numbers) {
      total = 0
      for (const num of numbers) {
        total += num
      }
      return total
    }

    console.log(totalOfArrays([1, 2, 3, 4, 5])) // 15
```

→ 출력 값이 : 15가 나와야하는데 `01,2,3,4,5`로 나오는 것을 확인할 수 있다

[두번째 코드 작성]

```jsx
    const totalOfArrays = function(...numbers) { //문자로 받아지나?
      total = 0
      for (const num of numbers) {
        total += Number(num) //number로 감싸주면? => Nan이 된다
      }
      return total
    }
```

<aside>
💡

수정 결과

</aside>

- **배열 자체를 인자로 받게 하고 싶다면 전개 구문은 필요가 없다**

```jsx
    const totalOfArrays = function(sth) { //그냥 일반 배열은 배열 자체로 받아진다
      total = 0 
      for (const s of sth) { //일반 배열을 받아와서 그것을 loop로 도는 것
        total += s
      }
      return total //15 출력
    }

```

## 원하는 것처럼 전개 구문을 사용하려면?

---

- 매개변수와 호출방법을 바꿔야 한다.

```jsx
const totalOfArrays = function(...numbers) {
  let total = 0;
  for (const num of numbers) {
    total += num;
  }
  return total;
}

console.log(totalOfArrays(...[1, 2, 3, 4, 5])); // 15
```