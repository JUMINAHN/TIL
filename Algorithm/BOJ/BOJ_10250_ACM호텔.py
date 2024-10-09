# 정문으로 걸어서 가장 짧은 거리에 있는 방 선호
# 걷는 거리가 가장 짧도록 방을 배정
# 각층에 W개의 방이 있는 H층 건물 W*H
# YY,XX 로 구성됨 => YY는 층수(H), XX는 넓이&가로 길이(W)
# W가 같을떄는 Y가 작은것을 기준으로 선호
# 결론적으로 맨 왼쪽부터 순서대로 배정됨
# N번쨰 손님에게 배정되어야하는 방 번호 출력
'''
2
6 12 10 => 402
30 50 72 => 1203
'''
# import sys
#
# sys.stdin = open('input10250.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #N번쨰로 도착할 손님의 수
    H, W, N = map(int, input().split()) #높이 6, 가로 12, N번쨰 방문 손님
    #배정의 오류
    acm_hotel = []
    for col in range(1, W+1):
        floor = []
        for row in range(H): #층부터 -> 반대로 :: 아까그거처럼 -1한거랑 똑같음
            if col >= 10: #row가 아니라 col을 기준으로 해야함
                floor.append(f'{H-row}{col}') #여기값 잘못설정함 -> 잘못 기입함
            else : #계속 잘붙다가 왜 안붙지?
                floor.append(f'{H-row}{0}{col}') #이게 맞음
        acm_hotel.append(floor) #왼쪽부터 채우기
    #print(acm_hotel) #다만 지금 세로로 되어야 함 -> 행/열 바꿔주면 됨 == 전치행렬

    acm = list(map(list, zip(*acm_hotel))) #단순 str로 묶으니까 튜플
    count = 0
    result = 0 #호텔번호
    #자 여기서 동일하게 접근
    for col in range(W):
        for row in range(H):
            if count == N:
                break
            result = acm[H-1-row][col]
            count += 1
        if count == N:
            break
    print(result)

#반례
'''
1
10 10 100
정답은 1010
'''

