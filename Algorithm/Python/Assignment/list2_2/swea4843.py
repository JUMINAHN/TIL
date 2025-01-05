import sys
sys.stdin = open('input4843.txt')
#테스트 케이스 개수
#이진 탐색
T = int(input())
for tc in range(1, T+1):
    #큰수 작은수 번갈아가면서 출력시키기
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    #rint(arr)
    print(f'#{tc}', end = ' ')
    for i in range(5): #총 10개 출력
        last = arr.pop()
        first = arr.pop(0)
        print(last, first, end=" ")
    print()