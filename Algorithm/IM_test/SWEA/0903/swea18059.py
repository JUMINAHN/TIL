# import sys
#
# sys.stdin = open('input18059.txt')
#이거를 왜?

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    R = 10 #10*10격자
    arr = [[0]*R for _ in range(R)]

    N = int(input()) #색종이 개수
    for _ in range(N): #색종이를 넣을 행위 반복
        r1,c1,r2,c2,color = map(int, input().split())
        # print(r1)
        # print(r2)
        # print(c1)
        # print(c2)
        #print(color) #color가 1일때 2일떄?
        for row in range(r1, r2+1):
            #print(row)
            for col in range(c1, c2+1): #오탄
                #print(row)
 #               print(arr[row][col])
                arr[row][col] += color #왜 색칠이 안돼?
                #print(arr[row][col])
                #print(arr[row][col])
        #print(arr)
    #print(arr)
        #
        # else :
        #     for row in range(r1, r2 + 1):
        #         for col in range(c2, c2 + 1):
        #             arr[row][col] += 2
    #print(arr)
    #내가 생각한 흐름이 아닐 때, 오탈자 있는지 확인하기
    # total = 0
    # for row in range(N):
    #     for col in range(N):
    #         if arr[row][col] == 3:
    #             total += 1
    total = 0
    for row in range(R):
        for col in range(R):
            #print(arr[row][col])
            if arr[row][col] == 3:
                total += 1
    print(f'#{tc} {total}')