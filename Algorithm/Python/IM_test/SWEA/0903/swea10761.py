import sys

sys.stdin = open('input10761.txt')
T = int(input())  # Testcase 수
# Testcase 만큼 반복
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    btn_info = []
    for i in range(len(arr) // 2):
        color, distance = arr[2*i], arr[2*i + 1]
        btn_info.append(list(color, distance))
    #btn 정보를 담아준다.
    #btn 정보를 기반으로 움직인다.
    pre_time = 0 #이전 시간을 담을 곳
    b_idx = o_idx = 1 #오렌지 블루 idx를 담을 곳
    for i in range(N):
        now_time = pre_time #현재 시간을 카운트할 것 -> 계속 갱신된 것을 받아올 것임

        #이동하는 것
        while b_idx != btn_info[i][1] or o_idx != btn_info[i][1] : #오렌지와 블루 idx
            if btn_info[i][0] == 'B':
                now_time += 1
                b_idx += 1 #뒤로 못돌아가는데.. 이거랑
            else : #orange면
                now_time += 1
                o_idx += 1
        #버튼을 누르는 행위
        if b_idx == btn_info[i][1] or o_idx == btn_info[i][i] :
            now_time += 1 #현재 우리 버튼을 누르는 행위를 실시한다.

        #현재랑 이전의 값 비교..

