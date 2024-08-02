import sys

sys.stdin = open('input18061.txt')

# 이진수
def find_binary(arr, find_num): #index 기준으로 찾음, 찾을번호 P
    start = 0
    end = len(arr) - 1
    count = 0
    while start <= end :
        mid = (start+end) // 2 #index -> 중간값 계산에서 오류!!
        count += 1
        if arr[mid] == find_num:
            break
        elif arr[mid] < find_num:
            start = mid + 1
        else :
            end = mid - 1
    return count

T = int(input()) #T3
for tc in range(1, T+1):
    #사람 A, 사람 B
    #전체쪽수 P, 찾을번호 A, 찾을번호 B
    P, A, B = map(int, input().split()) #400, 300, 350
    arr = [i for i in range(1, P+1)] #arr로 들어갈 애들 -> 전체 쪽수
    Pa = find_binary(arr, A)
    Pb = find_binary(arr, B)
    result = 0
    if Pa == Pb:
        result = 0
    elif Pa < Pb : #먼저 펼치는 사람이 끝나니까
        result = 'A'
    else :
        result = 'B'
    print(f'#{tc} {result}')