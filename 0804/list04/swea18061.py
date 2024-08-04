import sys

sys.stdin = open('input18061.txt')
# 책 400쪽 -> 왼쪽이 1, 오른쪽이 400 총 페이지 400인칸
# 중간페이지 -> mid = 왼 + 오 // 2
# 찾는쪽 번호와 같아지면 탐색을 끝난다
# 더 빨리찾는 사람 승자
# P전체 쪽수, A/B가 찾을 번호

def find_num(arr, num):
    start = 0
    end = len(arr) - 1 #p만큼 -> index 범위
    count = 0

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            break
        elif arr[mid] > num :
            end = mid - 1
        else :
            start = mid + 1
        count += 1
    return count

#이진탐색
T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split()) #A와 B가 찾는 쪽수
    arr = [i for i in range(1,P+1)]

    #이진검색 공식.. 기억이 나지 않는다
    Pa = find_num(arr, A)
    Pb = find_num(arr, B)
    if Pa == Pb :
        print(f'#{tc} 0')
    elif Pa < Pb :
        print(f'#{tc} A')
    else :
        print(f'#{tc} B')