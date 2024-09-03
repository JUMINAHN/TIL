import sys

sys.stdin = open('input1989.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    data = input()
    if data == data[::-1]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')