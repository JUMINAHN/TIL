import sys

sys.stdin = open('input2304.txt')
N = int(input()) #기둥의 개수
#각 기둥의 위치(C), 높이
M = 1000
build = [0] * M-1

for _ in range(N):
    L, H = map(int, input().split())
    build[L] = H


max_val = max(build)
max_idx = 0
for i in range(len(build)):
    if max_val == build[i]:
        max_idx = i

#왼쪽 기준
for i in range(max_idx):
    if build[i] > build[i+1]:
        build[i+1] = build[i]
for i in range(M-1 ,max_idx, -1):
    if build[i] > build[i-1]:
        build[i-1] = build[i]

total = 0
#print(build)
for i in range(M-1):
    total += build[i]
print(total)