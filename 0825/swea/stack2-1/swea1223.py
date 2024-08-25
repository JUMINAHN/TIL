import sys

sys.stdin = open('input1223.txt')

def op_rate(d) :
    if d in ('+', '-') :
        return 1
    elif d in ('/', '*'):
        return 2
    else :
        return 0

def cal(op, v2, v1):
    v2 = int(v2)
    v1  = int(v1)
    if op == '+':
        return v2 + v1
    elif op == '-' :
        return v2 - v1
    elif op == '*' :
        return v2 * v1
    else :
        return v2 // v1


#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(input())

    stack = []
    result = []
    for d in data:
        if d.isdecimal():
            result.append(d)
        else : #그게 아니면 stack에 넣는다
            while stack and op_rate(stack[-1]) >= op_rate(d):
                result.append(stack.pop())
            stack.append(d)
    while stack:
        result.append(stack.pop())
    #print(result)

    #계산 진행_result 값 기반
    for r in result:
        if r.isdecimal():
            stack.append(r)
        else:
            if len(stack) >= 2:
                v1 = stack.pop()
                v2 = stack.pop()
                result = cal(r, v2, v1)
                stack.append(result)

    if len(stack) >= 2:
        v1 = stack.pop()
        v1 = int(v1)
        v2 = stack.pop()
        v2 = int(v2)
        result = cal(r, v2, v1)
        stack.append(result)

    print(f'#{tc} {"".join(map(str, stack))}')
