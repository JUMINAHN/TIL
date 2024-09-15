
import sys
input = sys.stdin.readline

day, K = map(int, input().split())
temper = list(map(int, input().split())) #3 -2 -4 -9 0 3 7 13 8 -3
max = 0
for i in range(len(temper)-K):
    total = 0
    for j in range(i+1,i+K+1): #k값도 바꿔줘야하거든 -> 이전에는 단순히 값만 구했어 -> 범위가 똑같이 간격이 늘어나야 하는데 고려하지 못함
        total += temper[j-1]
    if max < total:
        max = total
print(max)
