# baekjoon_15666

사이트: 백준
날짜: 2024년 10월 19일
다중 선택: 파이썬
완료: No

## 접근 방법 & 아이디어

## 알아두면 좋을 개념, TIP

1. 함수 실행 종료: return 문은 함수의 실행을 즉시 종료
2. 기본값 반환: 값 없이 return을 사용하면, 함수는 기본적으로 None을 반환

<aside>
💡

**return을 함수에서 사용하는 이유**

</aside>

- 함수의 실행 흐름을 제어하고, 코드의 가독성을 높이며, 특정 상황에서 함수를 빠르게 종료하는 등 다양한 목적으로 활용

## 코드 최종본

## 초기 코드 구현

### 트러블 슈팅1 :  RecursionError: maximum recursion depth exceeded in comparison

---

→ height의 높이가 변화가 없는 것을 확인

```python
#N개의 자연수 중에서 M개를 고른 수열
#같은 수를 여러번 골라도 된다
#내림차순이다. -> 잘못봤다 비내림차순이다.
#문제를 다시 읽어보니까 같은 수 출력해도 됨 == 단 중복되는 것은 여러번 출력하면 안됨

#한줄에 하나씩 문제의 조건을 만족하는 수열 출력 -> 중복되는 수열을 여러번 출력하면 안된다.
N, M = map(int, input().split())
data = list(map(int, input().split())) #4,4,2 -> 내림차순 정렬하기
data = set(data) #집합
data = list(data) #다시 리스트로 => 중복 제거
data.sort()

#똑같은 것울 출력 해도 됨 -> 단, 보니까 자신 보다 작으면 안됨
def recur(num, i): #height라고 생각하면 됨
    result = [] #결과 값
    if num == M: #height이면
        print(' '.join(map(str, *result)))#결과 값
    for i in range(0, N): #list형태로 출력할 것이기 때문에
        #i의 값이 증가하니까 -> recur로 i의 값을 전달할 것
        result.append(data[i]) #결과 값에 출력할 내용을 담음
        #그리고 재귀로 호출
        recur(num, i)
print(recur(0,0))

-----------------------------------------------
# RecursionError: maximum recursion depth exceeded in comparison

#data.sort(reverse=True)# 내림차순 정렬
#print(data) #== 내림 차순 확인 완료
#출력 값을 보면 -> 1을 뽑았으면 그 1은 건들지 못하고 그 뒤에 숫자들을 뽑을 수 있는 것 같다
#visited = [False] * (N) #방문 여부 확인을 위해서
#N+1을 하지 않는 이유는 data의 배열크기 만들 돌것이기 떄문에
# def recur(num): #시작 height
#     result = [] #result에 추가된 값 출력
#     if num == M: #높이가 같아지면
#         print(''.join(map(str, *result))) #출력
#     #그게 아니면 for문으로 하나씩 묶기
#     for i in range(0, N) : #data 인덱스 0부터 N-1까지
#         #그런데 방문을 확인해야 함
#         # if not visited[i]: #방문을 하지 않았다면
#         #     #방문을 한다
#         #     visited[i] = True #그리고 출력값에 추가한다
#         #     result.append(data[i]) #방문하지 않았으니 결과 값에 넣는다.
#         #     recur(num+1) #높이가 증가해야함 -> 깊이 증가
#         #     #방문이 되어있으면

```

### 트러블 슈팅 2 :  RecursionError: maximum recursion depth exceeded in comparison

---

→ for의 i범위만 증가시키고, 이 시작점에 대한 변경 값이 없어서 해당 부분 반영 ⇒ `for 구문`

```python
#N개의 자연수 중에서 M개를 고른 수열
#같은 수를 여러번 골라도 된다
#내림차순이다. -> 잘못봤다 비내림차순이다.
#문제를 다시 읽어보니까 같은 수 출력해도 됨 == 단 중복되는 것은 여러번 출력하면 안됨

#한줄에 하나씩 문제의 조건을 만족하는 수열 출력 -> 중복되는 수열을 여러번 출력하면 안된다.
N, M = map(int, input().split())
data = list(map(int, input().split())) #4,4,2 -> 내림차순 정렬하기
data = set(data) #집합
data = list(data) #다시 리스트로 => 중복 제거
data.sort()

#똑같은 것울 출력 해도 됨 -> 단, 보니까 자신 보다 작으면 안됨
def recur(num, idx): #height라고 생각하면 됨
    result = [] #결과 값
    if num == M: #height이면
        print(''.join(map(str, result)))#결과 값 #map() must have at least two arguments. == ' '.join(map(str, *result)
        #RecursionError: maximum recursion depth exceeded in comparison
        #return 1 #0 => list index out of range
        #값이 증가하게 되니까 재귀에서 빠져나오지 못하는 것 같다
    for i in range(0, N): #list형태로 출력할 것이기 때문에 => #0부터 2까지
        #i의 값이 증가하니까 -> recur로 i의 값을 전달할 것
        result.append(data[i]) #결과 값에 출력할 내용을 담음
        #그리고 재귀로 호출
        recur(num+1, i) #num의 값도 증가해야함 == 이것을 고려하지 못함
recur(0,0) #이미 위에서 출력
```

### 트러블 슈팅3 : 아무런 값도 출력되지 않는 문제

---

- result 값을 내부에서 선언해주었기 떄문에 지속적으로 초기화되는 문제가 발생
- 또한 pop을 해주지 않아서 지속해서 값이 쌓이는 문제가 발생함

```python
#N개의 자연수 중에서 M개를 고른 수열
#같은 수를 여러번 골라도 된다
#내림차순이다. -> 잘못봤다 비내림차순이다.
#문제를 다시 읽어보니까 같은 수 출력해도 됨 == 단 중복되는 것은 여러번 출력하면 안됨

#한줄에 하나씩 문제의 조건을 만족하는 수열 출력 -> 중복되는 수열을 여러번 출력하면 안된다.
N, M = map(int, input().split())
data = list(map(int, input().split())) #4,4,2 -> 내림차순 정렬하기
data = set(data) #집합
data = list(data) #다시 리스트로 => 중복 제거
data.sort()

#똑같은 것울 출력 해도 됨 -> 단, 보니까 자신 보다 작으면 안됨
def recur(num, idx): #height라고 생각하면 됨
    result = [] #결과 값
    if num == M: #height이면
        print(' '.join(map(str, result)))#결과 값 #map() must have at least two arguments. == ' '.join(map(str, *result)
        #RecursionError: maximum recursion depth exceeded in comparison
        #return 1 #0 => list index out of range
        #값이 증가하게 되니까 재귀에서 빠져나오지 못하는 것 같다
        #생각해보니까 set을 해서 N개가 아니다..
    for i in range(num, len(data)): #list형태로 출력할 것이기 때문에 => #0부터 2까지
        #i의 값이 증가하니까 -> recur로 i의 값을 전달할 것
        result.append(data[i]) #결과 값에 출력할 내용을 담음
        #그리고 재귀로 호출
        recur(num+1, i) #num의 값도 증가해야함 == 이것을 고려하지 못함
recur(0,0) #이미 위에서 출력

```

### 트러블 슈팅4 : 원하는 값이 나타나지 않음

---

→ 깊이가 증가할 수록 값이 안나오는 것을 비롯하여 보았을 떄 0번 인덱스가 포함되지 않는 것이 확인 됨

```python

#한줄에 하나씩 문제의 조건을 만족하는 수열 출력 -> 중복되는 수열을 여러번 출력하면 안된다.
N, M = map(int, input().split())
data = list(map(int, input().split())) #4,4,2 -> 내림차순 정렬하기
data = set(data) #집합
data = list(data) #다시 리스트로 => 중복 제거
data.sort()

result = [] #결과 값 == 이것이 recur 값에 있으면 계쏙적으로 초기화 됨
#똑같은 것울 출력 해도 됨 -> 단, 보니까 자신 보다 작으면 안됨
def recur(num, idx): #height라고 생각하면 됨
    if num == M: #height이면
        print(' '.join(map(str, result)))#결과 값 #map() must have at least two arguments. == ' '.join(map(str, *result)
        #RecursionError: maximum recursion depth exceeded in comparison
        #return 1 #0 => list index out of range
        #값이 증가하게 되니까 재귀에서 빠져나오지 못하는 것 같다
        #생각해보니까 set을 해서 N개가 아니다..
    for i in range(num, len(data)): #list형태로 출력할 것이기 때문에 => #0부터 2까지
        #i의 값이 증가하니까 -> recur로 i의 값을 전달할 것
        result.append(data[i]) #결과 값에 출력할 내용을 담음
        #그리고 재귀로 호출
        recur(num+1, i) #num의 값도 증가해야함 == 이것을 고려하지 못함
        #하지만 -> pop을 하지 않으면 기하급수적으로 내용이 늘어남
        result.pop() #7을 넣었으면 출력하고 next
recur(0,0) #이미 위에서 출력
--------------------------------------
#또한 1 1이 누락 됨
1 7
1 9
7 7
7 9
9 7 #해당 값을 봤을때 이게 나올 필요가 없음 
9 9

```

### 트러블 슈팅 5:RecursionError: maximum recursion depth exceeded in comparison

---

- 또 깊이가 증가하지 않는 문제가 발생함 → 해당 부분 누락해서 보완

```python
#한줄에 하나씩 문제의 조건을 만족하는 수열 출력 -> 중복되는 수열을 여러번 출력하면 안된다.
N, M = map(int, input().split())
data = list(map(int, input().split())) #4,4,2 -> 내림차순 정렬하기
data = set(data) #집합
data = list(data) #다시 리스트로 => 중복 제거
data.sort()

result = [] #결과 값 == 이것이 recur 값에 있으면 계쏙적으로 초기화 됨
#똑같은 것울 출력 해도 됨 -> 단, 보니까 자신 보다 작으면 안됨
def recur(num): #height라고 생각하면 됨
    if num == M : #height이면 -> 첫번째 값보다 이후 값이 커야 함 #and result[num-1] <= result[num] == 아님
        print(' '.join(map(str, result)))#결과 값 #map() must have at least two arguments. == ' '.join(map(str, *result)
        #RecursionError: maximum recursion depth exceeded in comparison
        #return 1 #0 => list index out of range
        #값이 증가하게 되니까 재귀에서 빠져나오지 못하는 것 같다
        #생각해보니까 set을 해서 N개가 아니다.
        #현재 num으로 출력해서 계속 고착화 >
    for i in range(num, len(data)): #list형태로 출력할 것이기 때문에 => #0부터 2까지
        #i의 값이 증가하니까 -> recur로 i의 값을 전달할 것
        # if i != 0:
        #     if data[i] >= result[num-1]: #전보다 작으면 넣어
        result.append(data[i]) #결과 값에 출력할 내용을 담음
        #그리고 재귀로 호출
        recur(i) #num의 값도 증가해야함 == 이것을 고려하지 못함
        #하지만 -> pop을 하지 않으면 기하급수적으로 내용이 늘어남
        result.pop() #7을 넣었으면 출력하고 next
recur(0) #이미 위에서 출력
```

### 트러블 슈팅 6 : ecursionError: maximum recursion depth exceeded in comparison

---

```python
result = [] #결과 값 == 이것이 recur 값에 있으면 계쏙적으로 초기화 됨
#똑같은 것울 출력 해도 됨 -> 단, 보니까 자신 보다 작으면 안됨
def recur(num, stidx): #height라고 생각하면 됨
    if num == M : #height이면 -> 첫번째 값보다 이후 값이 커야 함 #and result[num-1] <= result[num] == 아님
        print(' '.join(map(str, result)))#결과 값 #map() must have at least two arguments. == ' '.join(map(str, *result)
        #RecursionError: maximum recursion depth exceeded in comparison
        #return 1 #0 => list index out of range
        #값이 증가하게 되니까 재귀에서 빠져나오지 못하는 것 같다
        #생각해보니까 set을 해서 N개가 아니다.
        #현재 num으로 출력해서 계속 고착화 >
    for i in range(stidx, len(data)): #list형태로 출력할 것이기 때문에 => #0부터 2까지
        #i의 값이 증가하니까 -> recur로 i의 값을 전달할 것
        # if i != 0:
        #     if data[i] >= result[num-1]: #전보다 작으면 넣어
        result.append(data[i]) #결과 값에 출력할 내용을 담음
        #그리고 재귀로 호출
        recur(num+1, i) #num의 값도 증가해야함 == 이것을 고려하지 못함
        #깊이 증가를 빼버린 문제 -> i값 자체를 바꿔버리면 될 것 같음
        #하지만 -> pop을 하지 않으면 기하급수적으로 내용이 늘어남
        result.pop() #7을 넣었으면 출력하고 next
recur(0,0) #이미 위에서 출력

```

### 트러블 슈팅 7 :  IndexError: pop from empty list

---

```python
#한줄에 하나씩 문제의 조건을 만족하는 수열 출력 -> 중복되는 수열을 여러번 출력하면 안된다.
N, M = map(int, input().split())
data = list(map(int, input().split())) #4,4,2 -> 내림차순 정렬하기
data = set(data) #집합
data = list(data) #다시 리스트로 => 중복 제거
data.sort()

result = [] #결과 값 == 이것이 recur 값에 있으면 계쏙적으로 초기화 됨
#똑같은 것울 출력 해도 됨 -> 단, 보니까 자신 보다 작으면 안됨
def recur(num, stidx): #height라고 생각하면 됨
    if num == M : #height이면 -> 첫번째 값보다 이후 값이 커야 함 #and result[num-1] <= result[num] == 아님
        print(' '.join(map(str, result)))#결과 값 #map() must have at least two arguments. == ' '.join(map(str, *result)
        #RecursionError: maximum recursion depth exceeded in comparison
        #return 1 #0 => list index out of range
        #값이 증가하게 되니까 재귀에서 빠져나오지 못하는 것 같다
        #생각해보니까 set을 해서 N개가 아니다.
        #현재 num으로 출력해서 계속 고착화 >
        #깊이가 0이라도 나와야함
    for i in range(num, len(data)): #list형태로 출력할 것이기 때문에 => #0부터 2까지
        #i의 값이 증가하니까 -> recur로 i의 값을 전달할 것
        # if i != 0:
        #     if data[i] >= result[num-1]: #전보다 작으면 넣어
        if len(result) == 0:
            result.append(data[i])
        elif result[-1] <= data[i]:
            result.append(data[i]) #결과 값에 출력할 내용을 담음
        #그리고 재귀로 호출
        recur(num+1, i) #num의 값도 증가해야함 == 이것을 고려하지 못함
        #깊이 증가를 빼버린 문제 -> i값 자체를 바꿔버리면 될 것 같음
        #하지만 -> pop을 하지 않으면 기하급수적으로 내용이 늘어남
        result.pop() #7을 넣었으면 출력하고 next
recur(0,0) #이미 위에서 출력
```

## 지피티 참고

- 기존 내용을 조금 만 더 정돈하고, 정리했으면 맞출 수 있었을 듯
- 조건문만 잘 정리했다면 맞추었을 듯
    - 따라서 요구하는 조건을 잘 정리해보자

```python

#한줄에 하나씩 문제의 조건을 만족하는 수열 출력 -> 중복되는 수열을 여러번 출력하면 안된다.
N, M = map(int, input().split())
data = list(map(int, input().split())) #4,4,2 -> 내림차순 정렬하기
data = set(data) #집합
data = list(data) #다시 리스트로 => 중복 제거
data.sort()

result = [] #결과 값 == 이것이 recur 값에 있으면 계쏙적으로 초기화 됨
#똑같은 것울 출력 해도 됨 -> 단, 보니까 자신 보다 작으면 안됨
def recur(num): #height라고 생각하면 됨
    if num == M: #height이면
        print(' '.join(map(str, result)))#결과 값 #map() must have at least two arguments. == ' '.join(map(str, *result)
        return #하는 이유?
        #RecursionError: maximum recursion depth exceeded in comparison
        #return 1 #0 => list index out of range
        #값이 증가하게 되니까 재귀에서 빠져나오지 못하는 것 같다
        #생각해보니까 set을 해서 N개가 아니다..
    for i in range(len(data)): #list형태로 출력할 것이기 때문에 => #0부터 2까지
        if not result or data[i] >= result[-1] : #result가 없거나 result의 마지막값보다 클 경우
            #i의 값이 증가하니까 -> recur로 i의 값을 전달할 것
            result.append(data[i]) #결과 값에 출력할 내용을 담음
        #그리고 재귀로 호출
            recur(num + 1) #num의 값도 증가해야함 == 이것을 고려하지 못함
        #하지만 -> pop을 하지 않으면 기하급수적으로 내용이 늘어남
            result.pop() #7을 넣었으면 출력하고 next
recur(0) #이미 위에서 출력

```

## 다른 방법 접근 시도