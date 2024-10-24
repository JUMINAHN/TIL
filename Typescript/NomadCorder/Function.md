# TS_functions(1.3/5)

날짜: 2024년 10월 24일

# Call Signatures : 나만의 함수 타입 만들기

---

- 마우스를 올렸을 때 나타나게 하는 것 만들기
    - 어떻게 함수를 호출해야하는지 알려줌
    - 자체적으로 매개변수 타입과 반환값 지정

```jsx
function add(a:number,b:number) {
    return a + b
}
//이걸 화살표 함수로 변환
const add2 = (a:number, b:number) => a+b //number를 반환한다는 것을 타입스크립트가 추론해서 알 수 있음
//나만의 add 함수타입을 만들고 싶음 
//따라서 우리는 우리만의 call signature를 만듬 == 마우스를 올렸을 떄 나타나게 하는 것
//어떻게 함수를 호출해야하는지 알려줌

//선언하기
type Add = (a:number, b:number) => number; //여기에는 매개변수 타입과 반환값을 지정해주고
const add3: Add = (a,b) => a+b //add3라는 것의 타입을 적용하고-> 실제로 그냥 일반 함수 사용하듯 사용해주면 됨
```

- 지정된 타입을 기반으로 기존처럼 함수를 사용하면 됨

# 오버로딩 :  함수가 여러개의 call signature를 가지고 있을 때 발생

---

```jsx
//오버로딩 == 직접 작성하진 않을 것이고, 외부 라이브러리에서 많이 활용

//call signature
type Add = (a:number, b:number) => number  //단축키같은 것
const add: Add = (a,b) => a+b

//오버로딩은 함수가 여러개의 call signature를 가지고 있을 때 발생시킴
//Q.클래스나 매서드에서 적용되는게 여기에서도 되는것인지 아니면 call signature인 케이스에만 되는 것인지

//약간의 바보같은 예시
type Add2 = {
    (a: number, b: number) : number
    (a: number, b: string ) : number //두개의 타입이 가능
}
//const add2 :Add2 = (a,b)  => a+b  //Operator '+' cannot be applied to types 'number' and 'string | number'.(2365)
//따라서 한 번 더 체크 해야 함

//이상한 예시지만 오버로딩의 핵심을 볼 수 있음 
const add3 :Add2 = (a,b)  => {
    if (typeof b === 'number') {
        return a + b
    } else { //string일 때
        return a
    }
}
```

## 자바 스크립트 자체에서도 자바처럼 오버로딩을 지원하는가?

---

- JavaScript는 함수나 메서드의 오버로딩을 언어 차원에서 지원하지 않지만, 위와 같은 방법으로 기능을 구현할 수 있다.
    - 여러 개의 메서드를 정의하는 대신, 단일 메서드 내에서 인자의 타입과 개수를 검사하여 다른 동작을 수행하도록 함

| Feature | Java | JavaScript |
| --- | --- | --- |
| Overloading | 지원됨, 같은 이름의 메서드를 여러 개 정의할 수 있으며 매개변수가 다름. | 지원되지 않음, 마지막에 정의된 함수가 이전 것을 덮어씀. 매개변수 검사로 유사한 기능 구현 가능. |
| Overriding | 지원됨, 자식 클래스가 부모 클래스의 메서드를 재정의할 수 있음. | 지원됨, 자식 클래스가 부모 클래스의 메서드를 재정의할 수 있음. |