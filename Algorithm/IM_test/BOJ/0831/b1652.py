#8:58
import sys
sys.stdin = open('input1652.txt')

'''
2
. .
. .
#2 2 -> 맞음
'''

def row_check(N, barrier, room):
    total = 0
    # 먼저 행 순회
    for row in range(N):
        #store = 0 #보관
        row_count = 0
        for col in range(N):
            if room[row][col] == '.':
                row_count += 1
            else:  # X를 만나게 되면
                if row_count >= barrier:
                    total += 1 #누울자리 count하고
                row_count = 0 #row count를 0으로 만들어 줘
        if row_count >= barrier:
            total += 1
    return total

def col_check(N, barrier, room):
    total = 0
    # 먼저 행 순회
    for col in range(N):
        #store = 0 #보관
        col_count = 0
        for row in range(N):
            if room[row][col] == '.':
                col_count += 1
            else:  # X를 만나게 되면
                if col_count >= barrier:
                    total += 1 #누울자리 count하고
                col_count = 0 #row count를 0으로 만들어 줘
        if col_count >= barrier:
            total += 1
    return total


N = int(input()) #정사각형의 방
room = [list(input()) for _ in range(N)] #정사각형의 방
barrier = 2 #장애물은 2칸
row = row_check(N,barrier,room)
col = col_check(N,barrier,room)
print(row, col)
#room을 순회하면서 '.'이 있는 것을 count 근데 2칸이상이 존재하면 누울 수 있음

