import sys

sys.stdin = open('input1223.txt')

def priority(data):
    if data in ('+', '-'):
        return 1
    elif data in ('*', '/'):
        return 2
    return 0 #아닐 경우 일단 0리턴 --> 괄호가 대표적

def operate(op, n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    if op == '+':
        return n2 + n1
    elif op == '-':
        return n2 - n1
    elif op == '*':
        return n2 * n1
    else:
        return n2 // n1

#Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    num_len = int(input())
    data = input()

    stack = []
    switch = []
    #후위표기식
    for d in data:
        if d.isdigit():
            switch.append(d)
        else:
            while stack and priority(d) < priority(stack[-1]): #stack에 값이 있으면
                switch.append(stack.pop())
            stack.append(d) #stack에 값이 없으면
    #그리고 stack에 남은 값들 pop해줌
    while stack:
        switch.append(stack.pop())
    # print(stack)
    # print(switch)

    #후위표기식을 계산으로 변환
    for s in switch:
        if s.isdigit():
            stack.append(s)
        else : #연산자라면 --> 2개 이상이어야 함
            if len(stack) >=2:
                n1 = stack.pop()
                n2 = stack.pop()
                result = operate(s, n1, n2)
                stack.append(result)
    print(f'#{tc} {"".join(map(str, stack))}')

    #연산자들이 남으면..?

