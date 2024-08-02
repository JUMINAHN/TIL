import sys

sys.stdin = open('arr_delta.txt')

arr = [list(map(int, input().split())) for _ in range(3)] #행, 열 3일 것 -> 행 3
data_r = [0, 1, 0, -1]
data_c = [1, 0, -1, 0]

for row in range(len(arr)):
    for column in range(len(arr[row])) :

        for k in range(len(data_r)) : #이동값 순회 -> 상/하/좌/우 순회
            #인덱스 번호를 뽑아낼 것 -> 이동한 값을 찾기 위해서 -> 이동
            move_row = row + data_r[k]
            move_column = column + data_c[k]

            if 0 <= move_row < len(arr) and 0 <= move_column < len(arr[row]):
                print(f"현재 위치 ({row},{column})의 인접 요소: {arr[move_row][move_column]}")
                #print(arr[move_row][move_column])