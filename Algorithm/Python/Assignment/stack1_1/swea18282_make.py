#괄호의 짝이 맞읅경우 1
#아닐경우 -1
import sys

sys.stdin = open('input18282.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    def my_push(item, size) :
        global top
        top += 1
        if top == size:
            print('overflow')
        else :
            stack[top] = item

    def my_pop():
        global top
        if top == -1:
            return 0 #underflow
        else :
            top -= 1 #top이 하나 감소
            return stack[top+1] #감소하기전의 데이터를 밖으로 내보낸다.

    #stack의
    str = list(input()) #하나씩 괄호를 str에 담았다.
    size = len(str) #의 크기만큼 일단 만들기
    stack = [0] * size #사실 stack자체에눈 0이라는 것이 다 차있기 떄문에 stack의 유무를 비교하는게 맞는가 싶다
    top = -1 #기본 세팅값

    #for문을 돌면서 stack에 담고 pop을 해보자

    for s in str:
        if s == '(':
            my_push(s, size)
        # stack이 비어서 )가 작동하기 어려운 경우
        else : #)일 경우
            if stack:
                my_pop()
            else :
                print(f'#{tc} -1')
                break
    else :
        if stack:
            print(f'#{tc} -1')
        else:
            print(f'#{tc} 1')



