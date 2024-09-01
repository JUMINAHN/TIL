import sys
sys.stdin = open('input2564.txt')


C,R = map(int, input().split()) #가로와 새로의 길이
#2차원 배열을 만들기보다는 1차원으로 상하좌우를 만드는게 좋겠다고 판단됨
t_row = b_row = [0] * R
l_col = r_col = [0] * C

store_count = int(input()) #상점의 개수
for i in range(1, store_count+1): #store의 개수를 살린다. #상점의 번호를 담을 것
    direct, distance = map(int, input().split()) #방향과 거리 #거리는 받은 것보다 -1을 작게해야 idx 접근가능
    if direct == 1: #북족
        t_row[distance-1] = i
    elif direct == 2: #남쪽
        b_row[distance-1] = i
    elif direct == 3: #서쪽
        l_col[distance-1] = i
    else : #동쪽
        r_col[distance-1] = i
#원하는 값이 맞게 1부터 3까지 들어갔는지 확인
print(t_row)
print(b_row)
print(l_col)
print(r_col)