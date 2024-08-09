#일단 arr을 만들어서 좌표를 계산하고, 좌표에 접근할 수 있도록 하자 -> 모든 좌표의 범위를 지문에서 찾자
arr = [[0]*100 for _ in range(100)] #arr좌표 만들기
for tc in range(4): #총 4번의 직사각형을 만들 것이기 때문에
    #왼쪽아래 x1,y1   #오른쪽 위 x2,y2
    x1, y1, x2, y2 = map(int, input().split()) # 1 2 4 4
    #좌표에 해당되는 부분에 arr[row][col] = 1을 대입시켜준다 -> 중복될경우 continue로 넘기고
    #총 arr[row][col]이 1인 것에 대한 결괄 출력한다.
    for row in range(y1, y2): #다시 상자값을 보니까 그냥 이 범위가 맞음
        for col in range(x1, x2):
            if arr[row][col] == 1:
                continue
            arr[row][col] = 1
    #print(arr) #그리고 for문내에서 확인을 함 --> 전반적으로 바꼈을 것
#그러면 전체 arr을 돌았을 떄 arr이 1인 것을 count하면 됨
total = 0
for row in range(len(arr)):
    for col in range(len(arr[row])):
        if arr[row][col] == 1:
            total += 1
print(total)