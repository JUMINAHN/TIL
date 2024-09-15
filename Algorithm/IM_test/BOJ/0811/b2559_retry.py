import sys
sys.stdin = open("input2559.txt")


N, K = map(int, input().split())
data = list(map(int, input().split()))

#윈도우 슬라이딩 기법 맨 앞을 뺴고, 맨 뒤를 뺴는 기법
total = max = 0
for i in range(K):
    total += data[i]
    max += data[i]

#바로 앞을 따고, 바로 앞을 따는 것
for i in range(K,N) :#K만큼 돌 거니까!! 맨 끝까지 계산
    total = total + data[i] - data[i-K]
    if max < total:
        max = total

print(max)