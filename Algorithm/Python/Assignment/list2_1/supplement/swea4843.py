import sys

sys.stdin = open('input4843.txt')


# 선택정렬사용하기
# idx로 접근하고, 작은 것을 기준으로 맨처음것과 위치 바꾸기
# 맨뒤에값은 자동으로 남고, 그 다음값과 비교하기 떄문에 arr의 길이만큼 range를 돌지 않는다.
# idx로 접근하기
def sort_data(arr, N):
    for i in range(N - 1):
        min_idx = i
        for j in range(i+1, N): #비교된 것을 굳이 비교할 필요가 없기 때문에
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] #그 다음값을 비교하는 방식
    return arr

#10개만 출력
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    #arr자체를 정렬하기
    arr = sort_data(arr, N)
    #정렬한 것 기반으로 값 출력하기

    print(f'#{tc}', end= " ")
    for i in range(5):
        max_num = arr[N-1-i]
        min_num = arr[i]
        print(max_num, min_num, end = " ")
    print()