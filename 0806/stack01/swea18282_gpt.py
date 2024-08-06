import sys

sys.stdin = open('input18282.txt')

T = int(input()) #testcase 4번
for tc in range(1, T+1):
    #초기 세팅값
    stack = list(map(str, input()))  # () () ((( )))
    top = -1
    new_stack = [0] * len(stack)

    def my_push(item,size): #입력값, 길이 --> len(stack)
        global top
        if top == size -1: #길이 확인 제대로
            return
        else :
            top += 1
            new_stack[top] = item

    def my_pop() :
        global top
        if top == -1:
            return 0
        else :
            top -= 1
            return new_stack[top+1] #기존에 들어있는 값들에서 작업

    result = 1 #반환할 결과값 설정 -> flag같은 느낌으로
    for i in range(len(stack)):
        if stack[i] == '(':
            my_push(stack[i], len(stack))

        elif stack[i] == ')': #이거라면
            if top == -1: #맨 마지막까지 가서 스택이 비어있을 때
                result = -1 #비어있다. '('가 없다는 뜻 ')'가 더 많다는 의미
                break #더 확인할 필요가없으니 끝낸다.
            my_pop() #그게 아니라면 팝을 해준다.

        else : #괄호가 아닌 다른 문자가 있는 경우 처리
            result = -1 #다른 문자가 있으면 -1

    #모든 문자를 처리한 후 실행 --> top = -1은 문자가 모두 비어있을 떄
    if top != -1: #모든 문자를 처리한 후 '('가 있는지 확인하는 것 --> 요소가 남아있다는 것
        result =- 1 #여는 괄혹 더 많은 경우 괄호의 짝이 맞지 않기 떄문에 -1
    print(f'#{tc} {result}')