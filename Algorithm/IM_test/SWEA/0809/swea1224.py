import sys

sys.stdin = open('input1224.txt')
def priority(data):
    if data in ('+', '-'):
        return 1
    elif data in ('*', '/'):
        return 2
    return 0 #괄호가 들어왔을 때

def operate(op, n1, n2):
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

#Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    num_length = int(input())
    data = input()

    stack = []
    switch = []
    #후위표기식으로 바꿔보기
    for d in data:
        if d.isdigit():
            switch.append(d) #조건범위 오류
        elif d == '(':
            stack.append(d)
        elif d == ')':
            while stack and stack[-1] != '(': #괄호가 아닐때
                switch.append(stack.pop())
            stack.pop() #괄호 빼기
        else:
            while stack and priority(d) < priority(stack[-1]): #스택우선순위
                switch.append(stack.pop())
            stack.append(d)
    #남은 스택에 있는 애들 빼내기
    while stack:
        switch.append(stack.pop())
    # print(stack)
    # print(switch)

    #후위 연산자 계산하기
    for s in switch:
        if s.isdigit():
            stack.append(s)
        else: #연산자
            if len(stack)>=2:
                try :
                    n1 = stack.pop()
                    n2 = stack.pop()
                    result = operate(s, n1, n2)
                    stack.append(result)
                except:
                    print('오류')
    print(f'#{tc} {"".join(map(str, stack))}')