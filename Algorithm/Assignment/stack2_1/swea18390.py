import sys

sys.stdin = open('input18390.txt')

def op_rate(d):
    if d in ('+', '-'):
        return 1
    elif d in ('*', '/'): #오타 떄문pop from empty list
        return 2
    else :
        return 0

#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    data = list(input())

    stack = []
    result = []
    #순회해서 확인
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

    while stack:
        result.append(stack.pop())

    print(f'#{tc}', end = " ")
    print("".join(map(str, result)))