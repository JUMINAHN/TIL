import sys

sys.stdin = open('input1959.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split()) #첫번째 배열의 길이 // 두번쨰 배열의 길이
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #B에대한 첫번째 내용을 담을 곳
    if N < M:
        small_B = B[:N] #그만큼 담겼어 #012가 담기는게 맞는데
        #print(small_B)
        total = 0 #그래서 슬라이딩 한 것 같이 담아주기
        max_total = total
        for i in range(N): #1은 1끼리 2는 2끼리 -> 작은 수만큼 돌기
            total += A[i] * small_B[i]
        for i in range(M - N + 1):  # B를 순회할 것임
            total = total - (small_B[i - N] * A[0]) + (small_B[i] * A[-1])  # 얘
            if max_total < total:
                max_total = total
    else :
        small_B = B[:M] #그만큼 담겼어 #012가 담기는게 맞는데
        #print(small_B)
        total = 0 #그래서 슬라이딩 한 것 같이 담아주기
        max_total = total
        for i in range(M): #1은 1끼리 2는 2끼리
            total += A[i] * small_B[i]
        for i in range(0, N-M+1): #B를 순회할 것임
            total = total - (small_B[i-M] * A[0]) + (small_B[i] * A[-1])  #얘
            if max_total < total:
                max_total = total
    print(f'#{tc} {max_total}')
#        small_B[i]#새로운 추가된 애
#     print(max_total)