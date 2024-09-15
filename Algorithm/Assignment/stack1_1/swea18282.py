import sys

sys.stdin = open('input18282.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input()))
    stack = [0] * len(arr) #개수만큼 만들어진다.
    top = -1 #초기값
    #push, pop메서드 만들어 보기
    def my_push(item, size):
        global top
        if top == size: #size -> stack의 마지막 index check
            return
        else :
            top += 1
            stack[top] = item

    def my_pop():
        global top
        if top == -1: #0보다 더 작은 것을 찾으려고 하면
            return 0
        else :
            top -= 1
            return stack[top+1]

    #배열을 돌면서 검증한다.
    result = 1
    for a in arr : #들어있는 것을 순회해야함
        if a == '(':
            my_push(a, len(stack))
        elif a == ')':
            if top == -1: #스택이 비어있는데 )값이 더 많다면
                result = -1
            my_pop()
        #다른문자가 있는 경우

    #만약 (가 더많다면 top이 -1이 아니라면
    if top != -1:
        result = -1
    print(f'#{tc} {result}')


