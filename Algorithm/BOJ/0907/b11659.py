import sys
sys.stdin = open('input11659.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(M):
    a, b = map(int, input().split())
    sum = 0
    for i in range(a-1, b):
        sum += arr[i]
    print(sum)