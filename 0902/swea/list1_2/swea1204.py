import sys

sys.stdin = open('input1204.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #1000명의 수학 성적을 토대로 통계 자료
    #가장많이 빈출적으로 발생한 숫자 출력 -> 점수

    test_case = int(input())
    math = list(map(int, input().split()))

    #가장 많이 반복되는 숫자 -> count로 배열에 담아야 할 듯
    count = [0] * 101 #0점부터 100점이하의 값이기 떄문에
    for m in math:
        count[m] += 1 #count 점수에 해당 될 경우 +1을 해준다.
    #print(count) : 배열에 맞게 들어있음을 확인함
    #카운트에서 가장 많이 나온 숫자
    check_count = 0 #17번 카운트가 나왔다.
    for i in range(len(count)):
        if count[check_count] <= count[i]: #단의 조건이 여기서 진행됨
            check_count = i #checK-count는 센 숫자 그자체이고, 나는 많이 반복되는 것에 대한 idx를 추출하고자 했다.
    print(f'#{tc} {check_count}')
