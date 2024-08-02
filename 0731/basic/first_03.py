import sys

sys.stdin = open('arr_test_column.txt')

arr = [list(map(int, input().split())) for _ in range(5)] #기준값이 무엇이냐에 따라 range도 달라짐! 주의
#열이 가진 최대값 구해보기
total = 0 #최대값을 넣을 곳
for column in range(len(arr[0])):
    s = 0 #반복적으로 column을 고정하고 row에 있는 것만 뽑아올 것이기 떄문
    for row in range(len(arr)):
        s += arr[row][column]
    if total < s:
        total = s
print('max num :', total)

#열 접근하기
#column 범위를 접근할 떄 가장 어려웠던 부분이었음
#arr[0]으로 접근하는 이유는 열의 개수는 모두 동일하고 행의 개수만 다름
#열의 개수가 동일하다는 것은 행의 첫번쨰와 똑같다는 의미 따라서 -> arr[0]을 기준으로 잡고 접근
for column in range(len(arr[0])) :
    for row in range(len(arr)):
        print(arr[row][column]) #그대로 포지션은 같음
    print('-------------------')