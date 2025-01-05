#연속된 1의 개수와 동일하게 문제 접근하고 문제를 풀면된다.
T = int(input())
for tc in range(1, T+1):
    arr = list(input()) #OOXXOXXOOO
    N = len(arr)
    
    #배열을 돌면서 O인지 X인지 확인
    total = 0 #값을 합산할 변수
    count = 0 #O를 확인할 곳
    for i in range(N):
        if arr[i] == 'O':
            count += 1 #count 증가시키고
            total += count #total에 count를 넣는다.
        else : #만약 O가 아니라면
            count = 0 # count를 다시 제로화 한다.
    print(total) #전체 값