#접근방식
#가장 큰것에서 가장 작은 것을 뺼것, 그래서 하나하나 찾을 필요가 없음 -> 정렬화
#1. 선택정렬을 통해서 전체 정렬을 하고
#2. 그 인덱스 가장 작은것은 +1, 가장 큰것은 -1을 해준다
#3. dump횟수만큼 반복한다.
#3. 최종적으로 현재의 min, max를 확인하고 max-min빼서 결과값을 도출해야 한다.
import sys

sys.stdin = open('input1208.txt')


def idx_sort(box_height):
    for i in range(100-1): #전체 box_height가 가지고있는 횟수에서 -1 : 마지막 값 제외
        min_idx = i #선택정렬은 index 기준이니까 가장 작은 index먼저 부여 -> 점차 접근 정렬
        for j in range(i+1, 100):
            if box_height[min_idx] > box_height[j]: #기준 점인 맨처음(유동)과 그 뒤에 어디에 있는것비교
                min_idx = j #값이+ min이 더크면 -> 발견된 위치 옮겨줌
        box_height[min_idx], box_height[i] = box_height[i], box_height[min_idx]
    #print(box_height) #정렬된 값 확인 -> 맞게 정렬됨
    return box_height

def try_dump(dump, box_height):
    for i in range(dump + 1): #dump만큼 반복
        box_height = idx_sort(box_height)  # box_height를 정렬한 값
        box_height[0] += 1
        box_height[-1] -= 1  # 마지막에는 값을 더하고 뺴고 최종값이 반영이 되지 않은 상태
    return box_height

T = 10
for tc in range(1, T+1):
    dump = int(input())
    box_height = list(map(int, input().split())) #arr 박스의 높이들이 들어옴, 100개까지
    #3. dump횟수만큼 반복하기
    dump_result = try_dump(dump, box_height)
    #4. 마지막 값은 정렬이 되어있지 않은 상태 --> 뺴긴 완료함
    result_arr = idx_sort(dump_result)
    #4. 최종적으로 min, max값을 확인해서 거기서 max - min하기
    print(f'#{tc} {(result_arr[-1] - result_arr[0])}')