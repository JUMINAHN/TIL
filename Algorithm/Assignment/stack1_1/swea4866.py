import sys


#{, ( 모두 점검필요
sys.stdin = open('input4866.txt')

def check_stack(str):
    # stack의 여부만 확인하자.
    stack = []
    # str의 루프를 먼저 모두 돌아서 stack에 담던지 뺴던지하는게 목표
    for s in str:
        if s == '(' or s == '{':  # 이거라면
            stack.append(s)
        elif s == ')' or s == '}':  # 지금 그 외적인게 너무 많음
            # 차있지 않으면 break
            if not stack:
                return 0  # 정상적으로 짝을 이룬 상태가 아니라는 뜻
            # stack이 차있을때
            stack.pop()

    # 자 여기서 바로 stack이 비어잇는지 유무 확인
    if stack:
        return 0 #남아 있다는 뜻이니까
    else :
        return 1

#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    str = input().strip() #공백으로 영역을 나누는 것이 아니다.
    result = check_stack(str)
    print(f'#{tc} {result}')

    #자이제 스택에 값은 남아 있을때 -> for문을 다 돌아도 있을 떄