import sys

sys.stdin = open('input1206.txt')

T = 10
for tc in range(1, T+1):
    N = int(input()) #N개의 건물 높이가 주어진다.
    arr = list(map(int, input().split()))
    total = 0
    for i in range(2, len(arr)-2): #범위가 앞뒤 2가 없기 때문에 -> 내가 초기값 2로 시작하는 것 지정 안해줌
        max = arr[i-2] #가장 큰 값을 첫번째로 둔다
        for j in range(i-1, i+3): #총 5개를 비교해야하는데 거기서 내 앞에거랑 내 뒤에 2번쨰까지 비교를 한다.
            if i == j: #그런데 i와 j값이 같아질 경우 즉 내가 나타날 경우는 스킵을하고
                continue
            elif max < arr[j]: #초기값 보다 그 뒤에 값들이 더 크다면 그걸 옮겨 준다.
                max = arr[j]
        #그럼 max에 가장 큰 값이 들어있을 것임 --> 이걸 나와 비교해줘야 함
        if max < arr[i]: #내가 더 크다면 나에서 기존 값을 뺴줘
            total += (arr[i]) - max #i가 나, 내가 기준 --> 전체값에 반영을 해줘야함 --> 루프는 계속 범위를 바꾸기 떄문에 초기화가 될 수 있음 유의할 것
    print(f'#{tc} {total}')