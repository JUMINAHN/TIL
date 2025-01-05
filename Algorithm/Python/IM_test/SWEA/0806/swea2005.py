import sys

sys.stdin = open('input2005.txt')

#Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    # 파스칼
    N = int(input())
    def fibo(n):
        # global count
        # count += 1
        if n < 2:
            return n  # 2보다 작으면 출력
        else:
            return fibo(n - 1) + fibo(n - 2)  # 피보나치 수열

    for i in range(1, N+1):
        print(fibo(i))

    # print(f'#{tc}')
    # print(fibo(1))
    # print(fibo(1), fibo(1))
    # print(fibo(1), fibo(3), fibo(1))
    # print(fibo(1), fibo(4), fibo(4), fibo(1))