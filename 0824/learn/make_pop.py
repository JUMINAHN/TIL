#stack의 pop메서드 구현

#단순 pop 메서드 사용
stack = [1,2,3] #들어있고
print(stack.pop())
print(stack.pop())
print(stack.pop())

#현재 stack 상황
#이전 내용을 응용해서 이어가기
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
top = -1

my_push(3,1)
my_push(3,2)
my_push(3,3)
print(stack) #1,2,3

#pop 메서드 생성 후 구현
#pop 메서드 구현할 것
#상기 기준으로 top은 2 : 원소의 마지막 저장위치가 2번 idx
#idx라고 이해하면 편리
def my_pop(): #pop의 원리자체가 마지막 원소 반환
    global top
    if top == -1 : #그냥 top 자체가 -1이면
        print('underflow')
        return 0 #0 자체를 반환
    else :
        top -= 1 #현재 top 원소 감소
        return stack[top+1] #현재 top을 반환하는게 아니라 그 마지막 top의 원소를 반환하는 것
print(my_pop())
print(my_pop())
print(my_pop())