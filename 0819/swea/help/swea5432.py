import sys

sys.stdin = open('input5432.txt')

# 테스트 케이스 개수
T = int(input())
for tc in range(1, T + 1):
    arr = input().strip()
    stack = []
    total = 0

    for i in range(len(arr)):
        if arr[i] == '(':  # 여는 괄호
            stack.append('(')
        else:  # 닫는 괄호
            stack.pop()  # 스택에서 하나를 꺼냄
            if arr[i - 1] == '(':  # 바로 앞이 여는 괄호면 레이저
                total += len(stack)  # 스택에 남아있는 막대기 수만큼 더함
            else:  # 막대기의 끝
                total += 1  # 막대기의 끝이므로 조각 하나 추가

    print(f'#{tc} {total}')