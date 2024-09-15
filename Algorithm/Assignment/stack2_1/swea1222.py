import sys

sys.stdin = open('input1222.txt')
#테스트 케이스 개수
def op_rate(d):
    if d in ('+', '-'):
        return 1
    elif d in ('*', '/'):
        return 2
    else :
        return 0

def add(v2,v1):
    v2 = int(v2)
    v1 = int(v1)
    return v2 + v1

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(input())

    #일단 후위연산자
    result = []
    stack = []
    for d in data:
        if d.isdecimal() :
            result.append(d)
        else :
            while stack and op_rate(stack[-1]) >= op_rate(d):
                result.append(stack.pop())
            result.append(d)
    while stack:
        result.append(stack.pop())

    #result에는 후위 연산자만 가득함 이제 해당 내용을 기반으로 연산 시작
    add_list = []
    for r in result :
        if r.isdecimal():
            stack.append(r)
        else :
            if len(stack) >= 2:
                v1 = stack.pop()
                v2 = stack.pop()
                result = add(v2,v1)
                stack.append(result)
    #남은 것

    # while stack :
    if len(stack) >= 2:
        v1 = stack.pop()
        v2 = stack.pop()
        result = add(v2, v1)
        stack.append(result)
    print(f'#{tc}', end= " ")
    print(*stack)


