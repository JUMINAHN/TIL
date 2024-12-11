# [실습] Reference Type2

날짜: 2024년 10월 24일

# Uncaught ReferenceError: city is not defined

---

```jsx
    // 아래에 코드 작성
    //자체적으로 내부 값을 넣을 것
    person = {
      name : 'Alice', //문자열
      age : 30,  //숫자열
      city : 'New York', //문자열
      introduce : function() {//function ==> 객체 내부에서 메서드 호출하는 방법 => 이해하기 
        //나 자신의 객체 호출된 것을 반환
        return `안녕하세요 ${city}에 거주하는 ${age}살 ${name}입니다.`
        //Uncaught ReferenceError: city is not defined => 나스스로를 참조하지 않아서 생긴 문제로 보임
      }
    }
```

→ this를 사용하지 않아서 발생하는 문제로 보임

# Uncaught TypeError: person1.greeting is not a function

---

- greeting의 function이 없음을 확인할 수 있음
    - `객체`를 반환하는 함수 ⇒ 자체이기 때문에 새로운 class 생성하는 것과 비슷하게 생각하면 됨

![image.png](image.png)

## Uncaught SyntaxError: Function statements require a function name

---

⇒ function의 이름이 요구된다. 

⇒ 따라서 여기서는 greeting = function으로 부여해주어야 함을 유의한다.

```jsx
    function createPerson(name, age, city) { //객체를 반환하는 함수 ==> function 내부
      greeting : function(name, age) { //error발생 확인
      console.log(`${this.name}의 나이는 ${this.age}`)
      }
      return { //name과 age는 동일한 이름의 key값에 value가 할당되어야 한다
        name, //동일한 값을 전달할 것 == 단축구문 사용
        age,
        city
      }
    }

    const person1 = createPerson('홍길동', 30, '옥천')
    console.log(person1) // {name: '홍길동', age: 30, livesIn옥천: true, greeting: ƒ}
```

# index.html:35 Uncaught TypeError: person1.greeting is not a function

---

![image.png](image%201.png)

```jsx
    function createPerson(name, age, city) { //객체를 반환하는 함수 ==> function 내부
      greeting = function(name, age) { //error발생 
        console.log(`${this.name}의 나이는 ${this.age}`)
      }
      return { //name과 age는 동일한 이름의 key값에 value가 할당되어야 한다
        name, //동일한 값을 전달할 것 == 단축구문 사용
        age,
        city
      }
    }
```

⇒ `함수` 값을 선언하고 함수 값을 반환하지 않는 문제 발생

<aside>
💡

**수정 코드**

</aside>

```jsx
    function createPerson(name, age, city) { //객체를 반환하는 함수 ==> function 내부
      greeting = function(name, age) { //error발생 
        console.log(`${this.name}의 나이는 ${this.age}`)
      }
      return { //name과 age는 동일한 이름의 key값에 value가 할당되어야 한다
        name, //동일한 값을 전달할 것 == 단축구문 사용
        age,
        city,
        greeting
      }
    }

    const person1 = createPerson('홍길동', 30, '옥천')
    console.log(person1) // {name: '홍길동', age: 30, livesIn옥천: true, greeting: ƒ}
    person1.greeting() // 홍길동의 나이는 30입니다.
```

# 넘겨받은 인자를 활용해서 키값 변경

---

- error발생 ⇒ 삼항 연산자 활용

```jsx
    function createPerson(name, age, city) { //객체를 반환하는 함수 ==> function 내부
      greeting = function(name, age) { //error발생 
        console.log(`${this.name}의 나이는 ${this.age}`)
      }
      //현재의 상태에서 넘겹당느 인자 city의 값을 활용하여 키 값이 livein{city}가 되도록 설정한다
      return { //name과 age는 동일한 이름의 key값에 value가 할당되어야 한다
        name, //동일한 값을 전달할 것 == 단축구문 사용
        age, //city의 값이 있는 경우 => true없는경우 false
        `livesIn ${city}`: if (city) :  true ? false, //여기서 단축구문? 
        greeting
      }
    }
```

# Uncaught ReferenceError: livesIn is not defined
at createPerson

---

- **`createPerson`** 함수가 반환하는 객체에 **`greeting`** 함수가 포함되지 않아서 발생

```jsx
   function createPerson(name, age, city) { //객체를 반환하는 함수 ==> function 내부
    greeting = function(name, age) { //error발생 
      const livesIn = 'livesIn'
      console.log(`${this.name}의 나이는 ${this.age} 입니다`)
    }
      //현재의 상태에서 넘김 -> 인자 city의 값을 활용하여 키 값이 livein{city}가 되도록 설정한다
      return { //name과 age는 동일한 이름의 key값에 value가 할당되어야 한다
        name, //동일한 값을 전달할 것 == 단축구문 사용
        age, //city의 값이 있는 경우 => true없는경우 false
        [livesIn + city] : city ? true : false //city가 있으면 
        //삼항 연산자 => condition ? true : false
        //하나의 []로 해야함
 
      }
    }

    const person1 = createPerson('홍길동', 30, '옥천')
    console.log(person1) // {name: '홍길동', age: 30, livesIn옥천: true, greeting: ƒ}
    person1.greeting() // 홍길동의 나이는 30입니다.
```

[반환 위치 변경]

```jsx
   function createPerson(name, age, city) { //객체를 반환하는 함수 ==> function 내부
    const livesIn = 'livesIn'
    greeting = function(name, age) { //error발생 
      console.log(`${this.name}의 나이는 ${this.age}`)
    }
      //현재의 상태에서 넘겹당느 인자 city의 값을 활용하여 키 값이 livein{city}가 되도록 설정한다
      return { //name과 age는 동일한 이름의 key값에 value가 할당되어야 한다
        name, //동일한 값을 전달할 것 == 단축구문 사용
        age, //city의 값이 있는 경우 => true없는경우 false
        [livesIn + city] : city ? true : false, //city가 있으면 
        //삼항 연산자 => condition ? true : false
        //하나의 []로 해야함
        greeting
      }
    }

```