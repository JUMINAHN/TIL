import sys

sys.stdin = open('input1224.txt')

def op_rate(d):
    if d in ('+', '-'):
        return 1
    elif d in ('/', '*'):
        return 2
    else :
        return 0

def cal(data, v1, v2):
    v1 = int(v1)
    v2 = int(v2)
    if data == '+':
        return v2 + v1
    elif data == '-':
        return v2 - v1
    elif data == '*':
        return v2 * v1
    else :
        return v2 // v1


#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(input())

    result = []
    stack = []
    #순회
    for d in data:
        if d.isdecimal():
            result.append(d)
        elif d == '(':
            stack.append(d)
        elif d == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else :
            while stack and op_rate(stack[-1]) >= op_rate(d):
                result.append(stack.pop())
            stack.append(d)
    while stack :
        result.append(stack.pop())

    for r in result:
        if r.isdecimal():
            stack.append(r)
        else :
            if len(stack) >= 2:
                v1 = stack.pop()
                v2 = stack.pop()
                result = cal(r, v2, v1)
                stack.append(result)
    if len(stack) >= 2:
        v1 = stack.pop()
        v2 = stack.pop()
        result = cal(r, v2, v1)
        stack.append(result)
    print(f'#{tc} {"".join(map(str, stack))}')