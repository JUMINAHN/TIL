import sys
sys.stdin = open('input2304.txt')

#일차원과 이차원을 생각하기
K = 1001 #1000까지 있어야하니까
N = int(input()) #기둥의 개수
poll = [0] * K #기둥 나열
for _ in range(N): #기둥 개수만큼 순회
    #기둥의 위치, 기둥의 높이
    pos, height = map(int, input().split())
    poll[pos] = height
#print(poll) -> 기둥 내부에 값이 맞게 들어가있는지 확인하기

#1. 가장 큰 곳의 idx번호 구하기
max_idx = 0
max_data = 0
for i in range(K):
    if max_data < poll[i]:
        max_data = poll[i]
        max_idx = i
#print(max_idx, max_data) -> 확인
#2. 처음부터 가장 큰 곳 까지 영역을 나누기
    #2-1. 다음날보다 오늘이 크다면 다음날에 오늘 값을 반영해준다.
#now_1 = next_1 = 0
for i in range(0, max_idx): #오늘과 내일로 구분할 것이기 떄문에 max_idx까지 표기해도 괜찮다.
    if poll[i] > poll[i+1]:
        poll[i+1] = poll[i]
    #변수 자체라 반영이 되지 않음
    # now_1 = poll[i]
    # next_1 = poll[i+1]
    # if now_1 > next_1:
    #     next_1 = now_1
#print(poll) -> 확인

#3. 끝에서부터 가장 큰 곳 까지 영역을 나누기
for i in range(K-1, max_idx, -1): #K까지
    #print(i, i-1)
    #3-1. 마지막날보다 그 전날이 작다면 전날에 마지막 값을 반영해준다.
    if poll[i] > poll[i-1]:
        poll[i-1] = poll[i]
#print(poll) -> 범위 설정의 오류

#창고 값 계산
total = 0
for i in range(K):
    total += poll[i]
print(total)