w, h = map(int, input().split()) #전체column, row
p, q = map(int, input().split()) #start위치
t = int(input()) #소요시간

#row -> 좌표를 만든상태에서는 -1, 1로 시작하는게 맞지만 지금은 단순 이동에 사용할 것이기 떄문에 굳이..
data_row = [1, -1]
data_col = [1, -1]


#수열 -> 2w, 2h --> (p+t)%2h
col = w - (abs(w - (p+t) % (2*w)))
row =  h - abs(h - (q+t) % (2*h))

print(col, row)