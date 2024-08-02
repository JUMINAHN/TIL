import sys

sys.stdin = open('arr_zigzag.txt')
#지그재그 순회하기
arr = [list(map(int, input().split())) for i in range(3)] #행이 3개
for row in range(len(arr)): #3행
    for column in range(len(arr[row])) : #4열
        if row % 2 == 1: #row를 기준으로 홀수면 역순 출력
            result = arr[row][len(arr[row])-1-column] #기억 잘하기 #row가 고정되었기에 column
        else :
            result = arr[row][column] #정방향 출력
        print(result) #column을 다돌았을 때