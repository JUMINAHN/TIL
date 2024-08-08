import sys

sys.stdin = open('input18382.txt')

def cal(operate, n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    if operate == '+':
        return n2 + n1
    elif operate == '-':
        return n2 - n1
    elif operate == '*':
        return n2 * n1
    else:
        return n2 // n1

T = int(input())
for tc in range(1, T+1):
    data = list(input().split()) #10 2 + 3 4 + * .
    stack = []
    #그걸 기반으로 연산을 수행한다.
    for s in data:
        if s.isdigit():
            stack.append(s) #stack에 숫자를 넣어
        elif s == '.':
            print(f'#{tc} {stack.pop()}')
            break
        else: #연산자들인데
            #먼저 연산자가 있을 경우.. keep
            if len(stack) >= 2: #2보다 커야 연산 수행 가능
                n1 = stack.pop()
                n2 = stack.pop()
                result = cal(s, n1, n2) #연산자 데이터
                stack.append(result)
            else:
                if len(stack) <= 1: #1보다 작을경우는 연산이 안되게 하는걸 다시
                    print(f'#{tc} {"error"}')
                    break
