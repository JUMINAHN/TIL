import sys

sys.stdin = open('input3499.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input()) #카드 개수
    arr = list(input().split())
    print(f'#{tc}', end= ' ')
    if N % 2 == 1:
        front = arr[:N//2+1]
        back = arr[N//2+1:N]
        # for i in range((N//2)+1):
        #     print(front[i], end=' ')
        #     if i == N-1:
        #         break
        #     else :
        #         print(back[i], end=' ')
    else :
        front = arr[:N//2] #쉽게 생각하기
        back = arr[N//2:N]
        # for i in range(N // 2):
        #     print(front[i], end=' ')
        #     print(back[i], end=' ')
    for i in range(N // 2):
        print(front[i], end=' ')
        print(back[i], end=' ')
    if N % 2 == 1:
        print(front[-1], end = ' ') #이렇게 해도 되나,..
    print()
    # print(front)
    # print(back)


    # for i in range(N//2-1, N):
    #     if i == N-1:
    #         back.append('')
    #     else :
    #         back.append(arr.pop(i))
    # print(arr)
    # print(back)
    # # #번갈아 가면서 출력
    # for i in range(N//2):
    #     print(back[i], end =' ')
    #     print(arr[i], end =' ')
    # print()
