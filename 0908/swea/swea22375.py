import sys
def onoff(data):
    if data == 1:
        return 0
    elif data == 0:
        return 1

sys.stdin = open('input22375.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #스위치 개수
    change = list(map(int, input().split())) #바꿀 것
    standard = list(map(int, input().split())) #기준이 될 값

    count = 0 #스위치를 넘길애
    for i in range(0, N): #다음 챕터로 넘겨갈 애
        if change[i] == standard[i]:
            continue #같으면 그냥 넘겨
        else: #다르다면 -< 스위치를 켜
            for j in range(i, N) : #해당 idx부터 끝까지 돌아갈 애 -> 그냥 무조건 껏다 켜
                change[j] = onoff(change[j])
            count += 1
    print(f'#{tc} {count}')