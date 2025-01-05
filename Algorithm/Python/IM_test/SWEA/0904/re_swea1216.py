import sys

sys.stdin = open('input1216.txt')
#가장 긴 회문의 길이를 구하는 것임 ;; 문제 제대로 읽기
# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    test_case = int(input())
    N = 100
    arr = [input() for _ in range(N)]

    # 전체를 담을 변수
    max_len = 0
    #행
    for row in range(N):
#        for i in range(0, N):
        for j in range(row, N):
            data = [] #원하는 형태로 나옴
            for col in range(row, j+1):
                #print(arr[row][col])
                 data.append(arr[row][col])
            if data == data[::-1]:
                num = len(data)
                if max_len <= num:
                    max_len = num
    #print(max_len)
    # 열
    for col in range(N):
        #        for i in range(0, N):
        for j in range(col, N):
            data = []  # 원하는 형태로 나옴
            for row in range(col, j+1):
                # print(arr[row][col])
                data.append(arr[row][col])
            if data == data[::-1]:
                num = len(data)
                if max_len <= num:
                    max_len = num
    print(f'#{tc} {max_len}')


#            if max_len < len(data):
#                max_len = data
    #
    #         if data == data[::-1]:
    #             total += 1
    # print(total)

    #['C', 'C', 'A', 'C', 'A', 'C']
    #['A', 'A', 'C']
    #['C'] 되는 문제 발생