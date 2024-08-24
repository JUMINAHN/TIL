import sys

sys.stdin = open('../input18282.txt')

def check_brackets(brackets):
    stack = []
    for bracket in brackets: #문자열 하나씩
        if bracket == '(': #
            stack.append(bracket) #추가
        else:  # bracket == ')'
            if not stack: #stack이 아닐 경우
                return False
            stack.pop() #stack일경우 pop
    return len(stack) == 0

T = int(input())
for tc in range(1, T+1):
    brackets = input().strip() #문자열 자체로 받음
    result = 1 if check_brackets(brackets) else -1 #brackets가 있을경우 1이고, 아니면 -1
    # if check_brackets(brackets): -> python은 함수 호출을 조건문에서 사용할 수 있따.
    #     result = 1
    # else:
    #     result = -1
    print(f'#{tc} {result}')