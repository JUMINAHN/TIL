# 스택을 구현하기
# 쉽게 구현하는 방법

# 단순 append
# size를 지정할 필요가 없음
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# stack의 사이즈를 지정
# append를 push 알고리즘으로 구현

def my_push(size, item):
    global top #top이 계속 유동적으로 바뀔 것이니까
    top += 1 #마지막 원소를 넣어줄 위치를 가리킴
    if top == size:
        print('overflow') #size를 초과했기 때문, 즉 stack의 전체 배열의 범위를 초과한 것
        return False #거짓
    else :
        stack[top] = item #stack의 [0]번쨰 idx에 추가한다.

size = 3
stack = [0] * size
top = -1 #마지막 원소 저장 위치

my_push(3,1)
my_push(3,2)
my_push(3,3)
print(stack)