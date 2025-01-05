import sys

sys.stdin = open('input1216.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    test_case = int(input())
    N = 100
    arr = [input() for _ in range(N)]

    total = 0
    for row in range(N):
        data = []
        for i in range(0,N):
            for j in range(i,N): #왜냐면 j가 0부터 시작하면 안되기 떄문에
                for col in range(i,j+1): #+1인 이유는.. 0부터 0의 계산이 되지 않기 떄문에
                    data.append(arr[row][col])
            #print(data)
        if data == data[::-1]:
            if total < len(data):
                total = len(data)
    for col in range(N):
        data = []
        for i in range(0,N):
            for j in range(0,N):
                for row in range(i,j):
                    data.append([arr[row][col]])
        if data == data[::-1]:
            if total < len(data):
                total = len(data)
    print(total)