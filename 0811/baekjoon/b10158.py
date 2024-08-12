#import sys
#sys.stdin = open("input10158.txt")

w,h = map(int, input().split()) #칸 넓이
p,q = map(int,input().split()) #초기 좌표값 위치 p,q => x,y
t = int(input()) #출발후 8시간 후의 위치 찾기

data_row = [1, -1] #idx 접근 -> 델타 상하좌우 이런거랑 무관하게 다시 생각
data_col = [1, -1]

col = p
row = q
time = 0

kc = 0
kr = 0

while time <= t:
    #여기서 같이 바끼면
    move_row = row + data_row[kr]
    move_col = col + data_col[kc] #잘보기
    if 0 <= move_row < h and 0 <= move_col < w :
        time += 1
        row = move_row #디버깅 2나 깎임
        col = move_col
    else :
        if not 0 <= move_row < h:
            row = h - 1
            kr = (kr + 1) % 2

        if not 0 <= move_col < w:
            col = w - 1
            kc = (kc + 1) % 2
print(col, row)
