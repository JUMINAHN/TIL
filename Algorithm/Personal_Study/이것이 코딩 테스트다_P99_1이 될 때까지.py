#숫자를 나누는 것이 더 많은 숫자를 줄일 수 있음
#1. N에서 1을 뺀다
# 2.N을 K로 나눈다.
# 두 과정중 하나를 반복적으로 선택하여 수행하려고 한다
# 1이 될떄까지의 최소 횟수를 구한다.
N, K = map(int, input().split())

count = 0
while N != 1 : #1일떄까지
    if N % K == 0:
        N = N//K
    else :
        N -= 1
    count += 1
print(count)