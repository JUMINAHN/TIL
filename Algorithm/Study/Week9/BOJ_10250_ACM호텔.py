'''
다시 풀기
'''

#정문으로 걸어서 가장 짧은 거리에 있는 방
#걷는 거리가 가장 짧도록 방을 배정
#걷는 거리가 같을 때에는 아래층 방을 더 선호
#층에 W개의 방이 있는 H층 건물
#호텔 정문은 일층 엘베 바로 앞에 있는데, 정문에서 엛베 거리는 무시(맨왼쪽)
#방번호는 YXX나 YYXX형태인데 여기서 Y나 YY는 층수를 나타내고 XX는 엘리베이터에서부터 세었을때의 번호
#N번째로 도착한 손님에게 배정될 방 번호를 계산하는 프로그램
#H,W,N 세정수를 포함하고 있으며 각각 호텔의 층수, 각 층의 방 수, 몇번째 손님

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    H, W, N = map(int, input().split())  # 호텔의 층수, 각 층의 방 수, 몇번째 손님
    # 열부터 세알리기
    # 빌딩에 데이터 넣기
    arr = [[0]*W for _ in range(H)]  # 행이 H
    #print(arr)

    #arr에 해당되는 값 넣기
    for col in range(W):
        for row in range(H):
            #반대로 접근
            arr[row][col] = str(W-row) + str(col)
    print(arr)

