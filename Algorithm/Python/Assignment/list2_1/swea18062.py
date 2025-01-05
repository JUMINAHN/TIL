import sys

sys.stdin = open('input18062.txt')

#가장 큰수, 가장 작은수, 2번쨰 큰수
#1. 선택정렬로 오름차순 정렬을 진행
#2. 숫자 N개
#3. i과 N-i 비교 -> N-1, i
#4. if i == 5면 break


#선택정렬로 정렬
def arr_sort(arr):
    #선택정렬시작 -> 맨마지막 제외 -> 맨마지막은 될 것
    for i in range(len(arr) - 1):
        #선택정렬은 idx 기준 -> 카운팅 정렬은 data -> idx -> idx
        min_idx = i
        for j in range(i+1, len(arr)): #두번쨰거와 비교할 것
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = arr_sort(arr)

    print(f'#{tc}', end = " ")
    for i in range(N):
        if i == 5:
            break
        max = arr[N-1-i]
        min = arr[i]
        print(max, min, end= " ")
    print()