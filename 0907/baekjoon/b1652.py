#import sys
#sys.stdin = open('input1652.txt')
#방은 N*N으로 생김
#누울자리 찾는중
#연속해서 2칸 이상 빈칸 있으면 누울 수 있음
#가로, 세로 가능
#양옆으로 쭉뻗으면서 누울 수 있다.
N = int(input())
K = 2 #가능한 누울 수 있는 자리의 최소 크기
lying = [list(input()) for _ in range(N)]
#누울 수 있는 자리의 수를 계산하는 program
#행
total = 0 #총 누울 수 있는 자리 개수
for row in range(N):
    count = 0
    for col in range(N):
        if lying[row][col] == '.':
            count += 1
        else : #아니면
            if count >= K:
                total += 1
            count = 0
    if count >= K:
        total += 1
#열
#전치행렬
total2 = 0
lying2 = list(map(list, zip(*lying)))
for row in range(N):
    count = 0
    for col in range(N):
        if lying2[row][col] == '.':
            count += 1
        else : #아니면
            if count >= K:
                total2 += 1
            count = 0
    if count >= K:
        total2 += 1
print(total, total2)