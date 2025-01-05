import sys

sys.stdin = open('input10580.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    line = []
    count = 0
    for _ in range(n):
        start,end = map(int, input().split())
        line.append((start, end)) #전선을 달아요

    #전선을 하나씩 꺼내보아요
    for a,b in line: #오, 왼
        print(a,b)
        for x,y in line:
            print(x,y)
            if a<x and b>y:
                count += 1
            elif a>x and b<y:
                count +=1
    #print(count // 2)