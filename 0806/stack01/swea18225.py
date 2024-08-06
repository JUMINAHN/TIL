import sys

sys.stdin = open('input18225.txt')

T = int(input())
for tc in range(1, T+1):
    data = list(map(str, input()))
    stack = [0] * len(data)
    top = -1 #맨 위상단
    def my_push(item, size):
        global top
        if top == size:
            return #초과함
        else:
            top +=1 #처음은 0
            stack[top] = item

    def my_pop(): #pop
        global top #현재의 top 위치 -> idx 0에서 시작
        if top == -1 : #0보다 더 작은 stack에 없다면
            return 0 #0을 반환
        else :
            top -= 1
            return stack[top+1] #마이너스하기 전 현 스택에 대한것을 반환 --> 기준은 지금

    for d in data:
        if d != stack[top] or top == -1:
            my_push(d, len(data))
        else :
            my_pop()
    result = top+1
    print(f'{tc} {result}')



