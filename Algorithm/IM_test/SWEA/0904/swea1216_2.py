import sys

sys.stdin = open('input1216.txt')
#5번 케이스 왜 안돼?

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = 100
    test_case = int(input())
    arr = [input() for _ in range(N)]

    max_len1 = 1 #최대 길이 1
    for row in range(N):
        for i in range(N):
            for j in range(i+1, N+1): #여기 다시 보기
                data = []
                for col in range(i, j):
                    data.append(arr[row][col])
                reverse_data = data[::-1]
                if data == reverse_data:
                    if max_len1 <= len(data):
                        max_len1 = len(data)
    for col in range(N):
        for i in range(0, N):
            for j in range(i+1, N+1):
                data = []
                for row in range(i, j): #파이썬에서 슬라이싱할 때 마지막 인덱스가 포함되지 않기 때문
                    data.append(arr[row][col])
                reverse_data = data[::-1]
                if data == reverse_data:
                    if max_len1 <= len(data):
                        max_len1 = len(data)
    print(f'#{tc} {max_len1} ')
#     if max_len1 < max_len2:
#         print(f'#{tc} {max_len2}')
#     else:
#         print(f'#{tc} {max_len1}')
# #                    print(arr[row][col])

