import sys
sys.stdin = open('../stack2-1/input4874.txt')


def cal(op, v2, v1):
    v2 = int(v2)
    v1 = int(v1)
    if op == '+':
        return v2 + v1
    elif op == '-':
        return v2 - v1
    elif op == '*':
        return v2 * v1
    else :
        return v2 // v1

#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    data = list(input().split())
    #후위 연산자 자체가 들어간 상태

    stack = []
    result = []
#숫자는 스택에 넣는다.
#연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
#‘.’은 스택에서 숫자를 꺼내 출력한다.

    for r in data:
        if r.isdecimal() :
            stack.append(r)
        elif r == '.': #숫자를 꺼내 출력한다.
            if len(stack) == 1: #1만 남아있으면문제 없음
                print(f'#{tc} {stack.pop()}')
            else :#없으면 문제
                print(f'#{tc} error')
            break
        else :
            if len(stack) >= 2:
                v1 = stack.pop()
                v2 = stack.pop()
                result = cal(r, v2, v1)
                stack.append(result)
            else : #1보다 작을 경우, 연산이 되지 않는 것
                print(f'#{tc} error')
                break
    # print(stack)


#1 84
#2 error
#3 168