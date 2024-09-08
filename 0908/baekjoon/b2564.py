import sys
#나는 달팽이로 하드 코딩함
sys.stdin = open('input2564.txt')

C, R = map(int, input().split()) #C == 10 : 가로 , R == 5 : 세로
store = int(input()) #상점의 개수
#동서남북의 방향, 그리고 line의 위치
up = [0] * C
right = [0] * R
down = [0] * C
left = [0] * R

#상점
for i in range(1, store+1): #상점의 번호를 idx에 담는다.
    direct, pos = map(int, input().split())
    pos -= 1
    if direct == 1 :
        up[pos] = i
    elif direct == 2:
        down[pos] = i
    elif direct == 3 :
        right[pos] = i
    elif direct == 4:
        left[pos] = i

#동근 -> 4보다 클 수 있기 떄문에
direct, pos = map(int, input().split())
pos -= 1
if direct == 1 :
    up[pos] = 'X'
elif direct == 2:
    down[pos] = 'X'
elif direct == 3 :
    right[pos] = 'X'
elif direct == 4:
    left[pos] = 'X'

#한 줄로 펼쳐보기
one_line = up + left + down[::-1] + right[::-1]
print(one_line)
X_idx = 0
for i in range(len(one_line)): #X의 인덱스를 찾았다.
    if one_line[i] == 'X':
        X_idx = i
        break
total = 0
for i in range(1, store+1): #store개수만큼 반복
    store_idx = 0
    for j in range(len(one_line)): #i를 찾으면 됨
        if one_line[j] == i : #oneline i -> oneline에서 1이 들어가있는 것
            store_idx = j #지금 j를 찾고
            total += abs(X_idx - store_idx)
print(total)



