import sys

sys.stdin = open('input18282.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #위배케이스 : stack이 비어있는가 / stack이 차있는가  -> 2가지 조건을 고려할 것
    str = list(input().strip()) #괄호와 관련된 값을 모두 전달받는다.

    stack = []
    #for 루프를 통해서 str을 stack에 채워넣는다.
    for s in str:
        if stack:
            if '(' == s:
                stack.append(s)
            else :
                stack.pop()
        else :
            if '(' == s:
                stack.append(s)
            elif ')' == s:
                print(f'#{tc} -1')
                break #전체 break 더이상 확인할 필요가 없음
    else : #다 돌았음에도 stack에이 있다면
        if stack :
            print(f'#{tc} -1')
        else :
            print(f'#{tc} 1')