import sys

sys.stdin = open('input1204.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #testcase번호
    arr = list(map(int, input().split()))
    count = [0] * 101 #0점이상 100점이하 -> 총 101개


    #최빈수 비교 카운트 사용 -> count 정렬 맛보기
    for a in arr:
        count[a] += 1

    #count에 있는 idx값 추출하면 됨 -> 따라서 idx로 접근
    max_idx = 0
    for i in range(len(count)):
        if count[i] > count[max_idx]: #max_idx는 count의 순번이 들어갈 것 --> 즉 count개수를 비교해서 i를 돌려주면 되는 것
            max_idx = i
    print(f'#{tc} {max_idx}')
