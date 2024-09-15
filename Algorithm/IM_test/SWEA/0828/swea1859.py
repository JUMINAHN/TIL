import sys

sys.stdin = open('input1859.txt')

# Testcase 수
T = int(input()) #Test == 3
# Testcase 만큼 반복
for tc in range(1, T+1):
    Day = int(input()) #3
    schedule = list(map(int, input().split())) #10 7 6

    total = 0
    kijoon_day = schedule[-1] #마지막 날 기준
    for i in range(len(schedule)-1, -1, -1): #마지막날 제외
        if kijoon_day < schedule[i]:
            kijoon_day = schedule[i] #기준 날짜를 바꿔줘
        else : #기준 날짜보다 크다면
            result = kijoon_day - schedule[i]
            total += result
    print(f'#{tc} {total}') #4053?