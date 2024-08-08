import sys

sys.stdin = open('input18390.txt')

#2+3*4/5 코드

def op(operate):
    if operate in ('+', '-'):
        return 1
    elif operate in ('*', '/'):
        return 2
    return 0 #그게 아니면 괄호들


T = int(input())
for tc in range(1, T+1):
    data = input()
    #값입력받아서 후위연산자로 변환하기
    stack = []
    result = []
    #먼저 data를 다 돌았으면
    for d in data:
        if d.isdigit():#digit면 바로 출력
            result.append(d) #2,3,4, 5
        else: #연산자라면
            # stack에 이미 연산자가 있다면
            # 지금 input되는 것과 우선순위 비교
            while stack and op(d) <= op(stack[-1]): #stack에 있을 때 연산자들이
                operate = stack.pop()
                result.append(operate)
            stack.append(d) #stack에 아무것도 없을 떄! #+*/ --> /들어오면 pop되어야 해
    #여기서 stack이 다 돌지 않았다면
    while stack:
        result.append(stack.pop())
    print(f'#{tc} {"".join(result)}')
#    for r in result:
#        print(r, end="")

