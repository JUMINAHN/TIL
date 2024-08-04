import sys

sys.stdin = open('input1961.txt')

def change_direct(arr, N):
    #각각의 좌표값을 찾기 위해선 동일한 크기의 arr을 만들어 줘야한다.
    #90도 회전한 내용을 옮긴다 -> 회전을 할 떄는 좌표를 기준으로 옮긴다
    #목적지에 담을 내용은 원본과 다르게 새로 만들어져야 한다 -> 원본에 영향이 가면 안되기 떄문에
    #기존대비 새로운 좌표값에 값을 넣고자 할 때 어떠한 부분이 어떻게 다른지를 중점으로 옮긴다.
    new_arr = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            new_arr[row][col] = arr[N-1-col][row]
    return new_arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr1 = change_direct(arr,N) #90
    arr2 = change_direct(arr1,N) #180
    arr3 = change_direct(arr2, N) #270

    #해당 값을 한꺼번에 묶어서 영역별로 출력한다.
for a,b,c in list(zip(arr1,arr2,arr3)):
    print(f'{"".join(map(str, a))} {"".join(map(str, b))} {"".join(map(str, c))}')


    #print(arr1) -> 741 852 963이 영역별로 묶어서 나온다
#    what = list(zip(arr1, arr2, arr3))
#    print(what) #같은것 끼지 묶임 --> 같은 열끼리 zip으로 묶는다. #zip으로 묶인 한덩이 ([7, 4, 1], [9, 8, 7], [3, 6, 9])
#    for w in what: #([7, 4, 1], [9, 8, 7], [3, 6, 9])
#        print(w)
#    for a, b, c in what: #zip만 푸는것
#        print(a, b, c)
#    for a, b, c in what: #what자체가 가진 list덩어리니까 한줄씩 출력됨
#       print(f'{"".join(map(str, a))}{b}{c}')






