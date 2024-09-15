import sys

sys.stdin = open('input1222.txt')

def op(data):
    if data in ('+', '-'):
        return 1
    elif data in ('/', '*'):
        return 2
    return 0

def cal(op, n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    if op == '+':
        return n2 + n1
    elif op == '-':
        return n2 - n1
    elif op == '*':
        return n2 * n1
    else :
        return n2 // n1

T = 10
for tc in range(1, T+1):
    data_len = int(input())
    data = input()

    stack = []
    switch = []
    #후위 연산자로 변환
    for d in data:
        if d.isdigit():
            switch.append(d)
        else:
            while stack and op(d) < op(stack[-1]): #stack에 값이 있다면, 그리고 이전값보다 작거나 같다면 모두 팝하고 내껄 넣어
                switch.append(stack.pop())
            stack.append(d) #값이 없다면
    #아직 스택에 남아있다면 모두 append
    while stack:
        switch.append(stack.pop())

    #후위 연산자를 기반으로 연산
    for s in switch:
        if s.isdigit():
            stack.append(s)
        # 연산자라면 --> '+'라면
        # 길이가 2개이상이어야함
        else:
            if len(stack) >= 2:
                n1 = stack.pop()
                n2 = stack.pop()
                result = cal(s, n1, n2)
                stack.append(result)
    print(f'#{tc} {"".join(map(str, stack))}')
