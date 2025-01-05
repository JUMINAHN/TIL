import sys

sys.stdin = open('input1208.txt')

#평탄화의 최고점과 최저점의 차이를 반환하는 program
#dump 수행 -> 평탄화
#가로길이는 항상 100
#

def sort_num_plma(arr, N): #선택정렬을 통해 정렬 #idx로 정렬함
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

T = 10
for tc in range(1, T+1):
    dump = int(input())
    N = 100
    arr = list(map(int, input().split()))

    for i in range(dump):
        arr = sort_num_plma(arr,N)
        arr[-1] -= 1
        arr[0] += 1
    arr = sort_num_plma(arr, N)
    print(f"#{tc} {arr[-1] - arr[0]}")