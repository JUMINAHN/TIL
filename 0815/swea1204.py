import sys

sys.stdin = open('input1204.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    test_case = int(input())
    #1000명의 수학 성적을 토대로 통계 자료
    num_list = list(map(int, input().split()))
    #0점이상 100점 --> 최빈수를 구하기 위해서 counting하면 됨 => 따라서 count 101개 만들기
    count = [0] * 101

    for num in num_list:
        count[num] += 1

    #가장 큰 값 -> max(count)를 하면 : 카운트 내부의 값이 가장 큰 것이 출력됨
    #우리가 원하는 것은 count의 idx
    max_idx = 0
    #count 중에서 가장 큰 값이 있는 것을 확인해야 함 따라서 count를 순회
    #idx로 접근해서 idx 추출하기
    for i in range(len(count)):
        if count[max_idx] <= count[i]: #적으면서 접근하면 더 괜찮음 -> count[i] 자체가 내부 값을 의미하는 것
            max_idx = i
    print(f'#{test_case} {max_idx}')