import sys
sys.stdin = open('input2828.txt')
N, M = map(int, input().split()) #스크린 N, 바구니 M
screen = [0] * (N+1) #스크린
#마지막에는 screen의 0번째 idx를 pop해줘야함, 1부터 시작하기 떄문에 ----------------------------------> 추후 점검

J = int(input()) #사과가 떨어지는 개수
apple_pos = [int(input()) for _ in range(J)]
left_idx = 1
right_idx = M
move = 0
#바구니가 어디있는지
for pos in apple_pos: #사과의 위치
    if pos < left_idx: #만약 사과가 바구니보다 왼쪽에 있따면
        distance = left_idx - pos
        move += distance
        left_idx -= distance #pos의 위치로
        right_idx -= distance
    elif pos > right_idx: #만약 사과가 바구니보다 오른쪽에 있다면
        distance = pos - right_idx
        move += distance
        right_idx += distance
        left_idx += distance
print(move)
