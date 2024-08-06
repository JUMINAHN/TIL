import sys

sys.stdin = open('input2628.txt')
row, col = map(int, input().split()) #배열의 크기
cut_count = int(input()) #자르는 것 개수
arr = [[0]*col for _ in range(row)] #가로와 세로 최대 길이 10

for cc in range(1, cut_count+1):
    rc, num_idx = map(int, input().split())

    new_arr = [] #자른 종이를 담을 공간
    if rc == 0: #rc가 가로일 때 0
        for i in range(row):  # row가 3일때 cut한다고 가정할 때 -> 0부터 row까지
            if arr[i] == num_idx-1: #num_idx는 실제 입력받은 것이고 -> 들어갈 idx비교 해야함
                new_arr.append(arr[:i]) #i번까지 짜르고 A번
                new_arr.append(arr[i:]) #i이후부터 나누고 B번을 각각 담는다
                #근데 arr에 반영되지 않을 경우 새로운 절취가 생길 것 같은데,,,
            elif arr[i] > num_idx - 1: #그러면 새로운 설취를 기반으로 인덱스 반영..?
                new_arr.append(arr[:i])
                new_arr.append(arr[i:])


    else : #rc가 세로일 때  1
        for col in range(col): #col
            for row in range(row) :  #row
                if col == num_idx - 1:
                    new_arr.append(arr[row][:i])
                    new_arr.append(arr[row][i:])
                elif i > num_idx - 1:  # 그러면 새로운 설취를 기반으로 인덱스 반영..?
                    new_arr.append(arr[row][:i])
                    new_arr.append(arr[row][i:])

    #자 그래서 탄생한 new_arr:
    max = 0
    for new in new_arr:
        result = len(new) * len(new)
        if max < result:
            result = max
print(max)