#10:35~ 일단 두시간 초고함 11:04
#근데 문제는 짜고보니까 X -> 3이 끝인데 다른데까지 도는 문제가 발생하게 됨..
import sys
sys.stdin = open('input2564.txt')

C, R = map(int, input().split()) #가로, 세로
#상/하/좌/우
#위니까 열의 개수만큼
#0부터 10이 input되어야 함! -> 단 0을 포함해서 세는게 아님! 그냥 4-0 = 4인 것, idx 기준이면 4-0+1을 해줘야했음!! 주의
t_col = [0] * (C+1) #윗칸
b_col = [0] * (C + 1)
l_row = [0] * (R+1) #아래칸
r_row = [0] * (R+1)
#복사가 된듯
store_count = int(input()) #상점의 개수

#block 안이라고 생각하지말고 외부선임
for i in range(1, store_count+1) : #상점의 개수만큼 순회
    direct, distance = map(int, input().split()) #블록의 위치(동서남북), 거리 // distance는 그대로 끌고가도 됨
    if direct == 1:#북,top
        t_col[distance] = i #1부터 store개수만큼 input
    elif direct == 2:#남
        b_col[distance] = i
    elif direct == 3:#서
        l_row[distance] = i
    else :#동
        r_row[distance] = i
#상점에 값을 input한 것이 맞게 들어갔는지 확인하기 위해 각 값 출력 -> 맞게 들어감
direct, me_i = map(int, input().split()) #위치와 거리(distacne) : i설정 이유는 idx 위치를 헷갈리지 않기 위해 -> 해당 거리를 기준으로 계산을 진행할 것
#먼저 상점을 1개씩 찾아야하니까 위와 똑같이 순회하고 direct를 찾는다.

#교점이 있을떄랑 없을때를 찾아야 함
#결론은 작은것들만 더해주면 되지 않을까?
#그런데 index 찾는값이 없을경우 에러..?
total = 0
for i in range(1, store_count+1):
    if direct == 1: #북쪽이고 -> 같은 범위 내에 있는지 확인하기
        #t_col에 값이 있다면
        if 1 in t_col:
            store_i = t_col.index(i) #i(상점 번호가)가 들어있는 위치 // #나는 me_i
            #나에서 store_i 를 빼주고(절대값 사용), 그리고 그 나머지
            diff_distance = abs(me_i - store_i) #거리 차이
            result = min(diff_distance, C-diff_distance) #상단이니까
        else : #없다면
            pass
    elif direct == 2:
        pass
    elif direct == 3:
        pass
    else : #direct4라면
        pass