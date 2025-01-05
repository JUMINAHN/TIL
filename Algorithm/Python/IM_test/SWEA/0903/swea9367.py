#연속으로 커지는 길이
#import sys

#sys.stdin = open('input9367.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input()) #당근의 개수
    arr = list(map(int, input().split())) #당근을 input받아서

    max_length = 1
    count = 1
    for i in range(0, N-1):
        if arr[i] < arr[i+1]:
            count += 1
        else :
            if max_length <= count:
                max_length = count
            count = 1
    if max_length <= count:
        max_length = count
    print(f'#{tc} {max_length}')
