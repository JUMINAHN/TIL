import sys

sys.stdin = open('../input5432.txt')

# 테스트 케이스 개수
T = int(input())
for tc in range(1, T + 1):
    arr = input().strip()
    stack = []
    total = 0

    #스택을 사용하여 괄호의 짝을 맞추고, 레이저와 막대기의 끝을 구분하여 잘린 조각의 수를 정확하게 계산
    for i in range(len(arr)):
        if arr[i] == '(':  # 여는 괄호
            stack.append('(')
        else:  # 닫는 괄호
            stack.pop()  # 스택에서 하나를 꺼냄 #어쩃든 하나를 꺼내야 함
            if arr[i - 1] == '(':  # 바로 앞이 여는 괄호면 레이저
                total += len(stack)  # 스택에 남아있는 막대기 수만큼 더함
            else:  # 막대기의 끝
                total += 1  # 막대기의 끝이므로 조각 하나 추가
                # else: total += 1로 레이저가 아니라면 막대기의 끝을 의미합니다. 이 경우 조각 하나를 더합니다

    print(f'#{tc} {total}')