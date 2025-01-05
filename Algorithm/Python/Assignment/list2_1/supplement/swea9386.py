import sys

sys.stdin = open('input9386.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input())) #space가 없으면 => split되지 않음
    #print(arr)

    max_num = 0
    count = 0
    for i in range(N):
        if arr[i] == 1:
            count += 1
        else :
            count = 0
        if max_num < count :
            max_num = count
    print(f'#{tc} {max_num}')