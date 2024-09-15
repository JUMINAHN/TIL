import sys

sys.stdin = open('input2005.txt')
#합산의 과정이 어떤식으로 흘러가는지 살펴보기
#일단 첫번째는 왼쪽으로 더 더할 수 없다 범위가 벗어나기 때문에
#-> 1. 그렇다면 arr[row][col] 즉 row가 바뀌어도 모두 col이 0이면 1을 넣으면 되지 않을까?
#Testcase 수
T = int(input())
# Testcase 만큼 반복

#피보나치가 나보다 row가 -1이고, 나보다 row -1랑 col -1해주면 됨
for tc in range(1, T+1):
    N = int(input())
    arr = [[' ']*N for _ in range(N)] #값이 없는것 일단 추후 고려
    #일단 0을 만들어서 넣어봐

    for row in range(N):
        for col in range(N):
            if col == 0:
                arr[row][col] = 1
            elif col == row :
                num = arr[row][col]
                arr[row][col] = 1 #col의 위치에 있는 피보나치
            elif row > col:
                arr[row][col] = arr[row-1][col] + arr[row-1][col-1]

    print(f'#{tc}')
    for a in arr:
        print(" ".join(map(str, a)))

