import sys

sys.stdin = open('arr_test_input.txt')

# 2차원 배열 만들기
# [[1,2,3], [4,5,6], [7,8,9]]
arr = [list(map(int, input().split())) for _ in range(3)] #행은 3이고, list에 있는 내용이 행마다 추가
#여기에 대한 요소를 1개씩 접근해보자
for row in range(len(arr)):
    for column in range(len(arr[row])):
        print(arr[row][column]) #한개씩 찍어보는 것
    print('------영역구분-------')