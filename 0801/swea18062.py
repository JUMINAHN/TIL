import sys

sys.stdin = open('input18062.txt')

def sort_index(arr):
    for i in range(len(arr)-1): #마지막은 x
        min_idx = i
        for j in range(i+1, len(arr)): #1부터 끝까지 계산할 것
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] #선택 정렬
    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #정수 개수
    ai = list(map(int, input().split())) #10개 들어갈 것 적기
    #선택정렬로 -> 순서대로 정렬시키기
    sort_result = sort_index(ai)

    #print(sort_result)
    #max min을 번갈아가면서 제일큰거 -> 두번쨰 큰거 접근
    #그럼 최종적으로 min이 max보다 넘겨버리면 안됨
    print(f'#{tc}', end=" ")
    final_data = []
    for i in range(N): #0부터 9까지 -> 총 10개
        min_n = ai[i]
        max_n = ai[N-1-i]
        if max_n < min_n :
            break
        if len(final_data) == 10:
            break
        final_data.append(max_n)
        final_data.append(min_n)
        #음 출력 10개만 어찌하지
    for final in final_data:
        print(final, end=" ")
    print()
    #max min을 번갈아가면서 출력시키기 len[ai] = 10
    #min = 0, max = N-1 (9)


