import sys

sys.stdin = open('input.txt')
#테스트 케이스 개수
# 행 순회하면서 count
# 열 순회하면서 count
# count 함수 쓸거면 전치행렬로 만들어야 할듯?
# 그 범위 안에 1 ~ 9 각 숫자 하나씩 있어야 함
# count 쓸거니까 리스트로 가져오자
def check_row(arr):
    result_1 = 0
    #print(arr)
    for lst in arr: # 한줄 가져옴 [7, 3, 6, 4, 2, 9, 5, 8, 1]
        #print(lst)
        #print(lst.count(9))
        for i in range(1, 10):   # 1부터 9 있는지 확인
            if lst.count(i) == 1:
                #print(i)
                continue
            else:   # 하나라도 아니면
                result_1 = 0
                break #i자체에 break
        if result_1 == 0:
            break
        else:   # 이상없으면(1~9 1개씩 있으면)
            result_1= 1
    return result_1


def check_col(arr):
    result_2 = 0
    arr_t = []  # 전치행렬 생성
    for r in range(9):
        temp = []
        for c in range(9):
            temp.append(arr[c][r])
        arr_t.append(temp)

    for lst_t in arr_t:
        for j in range(1,10):   # 1~9까지 숫자 있는지
            if lst_t.count(j) == 1:
                continue
            else:               # 없거나 1개가 아니라면
                result_2 = 0
                break   # 더 볼 것도 없지
        if result_2 == 0:
            break
        #else:   # 반복문 다 돌아서 1 ~ 9까지가 1개씩만 있다면
        result_2 = 1
    return result_2


def three_three(arr):
    result_3 = 0
    for r in range(0,6,3): #row 0, 3, 6, 9로 바뀜
        for c in range(0,6,3): #col 0, 3, 6, 9로 바뀜
            slice_arr = arr[r:r+3]  # 확인 -> arr[0:3]부터 시작 [3:6], [6:9] #배열 idx row가 3개씩 출력됨
            #[7, 3, 6, 4, 2, 9, 5, 8, 1], [5, 8, 9, 1, 6, 7, 3, 2, 4], [2, 1, 4, 5, 8, 3, 6, 9, 7]
            #print(slice_arr)
            slice_arr2 = []
            for s in slice_arr:
                # [7, 3, 6, 4, 2, 9, 5, 8, 1], [5, 8, 9, 1, 6, 7, 3, 2, 4], [2, 1, 4, 5, 8, 3, 6, 9, 7]
                #  [7, 3, 6, 4, 2, 9, 5, 8, 1]
                slice_arr2.append(s[c:c+3]) # 3x3 배열로 가공
                # 7, 3, 6
                #5, 8, 9
                #2, 1, 4
            if r == 9 and c == 9: #여기서 빠져나가게 했는데?
                break
            #아니니까 스킵
            cnt = [0]*10
            for a in range(3): #0,1,2 #a가 9일때 count가 되는 건가?
                for b in range(3): #0,1,2
                    num = slice_arr2[a][b]
                    cnt[num] += 1 #0빼고 다 들어가니까

            for u in range(1,10): #그래서 그걸 1부터 10까지 카운트할 것이고
                if cnt[u] != 1: #1이 아니면
                    result_3 = 0 #0을 대입해주고 나간다
                    break
            else:   # cnt정렬에 있는 값이 그게 아니면 그냥 1을 준다.
                result_3 = 1
    return result_3


T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]    # 9 x 9배열

    # 행, 열, 3x3순회했을때 모두 조건 충족하면 1
    r1 = check_row(arr)
    # # # print(r1)
    r2 = check_col(arr)
    # print(r2)
    r3 = three_three(arr)
    #print(r3)
    if r1 == 1 and r2 == 1 and r3 == 1:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')