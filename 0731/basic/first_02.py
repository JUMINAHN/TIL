import sys

sys.stdin = open('arr_test_row.txt')

# 행 우선 순회
# arr에 예상 [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]
arr = [list(map(int, input().split())) for i in range(5)] #행의 개수가 N == 5개

#각 행을 순회했을 떄 가장 큰 값 구하기
#행의 큰 값 == 즉 각 행을 비교해야한다. 열의 내용을 다 더해야한다.
#즉 다룰것은 하나의 행자체이기 떄문에 그 위에 더할 값을 넣는다
total = 0 #가장 큰 값이 들어갈 위치
for row in range(len(arr)) : #행의 개수
    s = 0
    for column in range(len(arr[row])): #열의 개수
        s += arr[row][column]
    if s > total : #지금 값이 가장 큰 값이 들어간 곳과 비교했을 떄 크다면 해당 값이 들어간다 -> 반복적
        total = s
print('max num : ', total)


# 행 -> 열 하나씩 접근하기(기본)
for row in range(len(arr)):
    for column in range(len(arr[row])):
        print(arr[row][column])
    print('------') #영역 구분 --> 행이 바뀔때마다 표기될 것