#이 두 줄을 사용하면 더 빨리 출력할 수 있음
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #받을 수, 구간합을 계산할 수
arr = list(map(int, input().split())) #N개만큼 받을 수

#그 전 구간합을 다룰 배열 생성
prefix = [0] #0번 idx는 사용하지 않음
sum_value = 0 #현재를 다룰 것
#누적적으로 arr을 합산하고 prefix에 담을 것
for a in arr:
    sum_value += a
    prefix.append(sum_value)
#prefix에 누적합들을 담은 상태

#받을 수에 대한 내용 계산
for i in range(M): #구간합만큼 계산할 수
    s, e = map(int, input().split()) #start, end값을 받는다. idx를 기준으로
    result = prefix[e] - prefix[s-1] #3,2,1 즉 구간합이기 떄문에 뒤에서 앞에 누적내용을 제거해주어야 함
    #단 s-1인 이유는 1번 idx까지는 포함을 해야하기 때문에 그 전단계를 뺴주는 것
    print(result)