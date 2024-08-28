#연속된 것 == 윈도우 슬라이딩
#브루투포스 합을 구할 수 있는 것 중에 시간 초과 == 구간합
#구간합에서 마이너스 하는 것이 시간 복잡도를 줄일 수 있음

N, M = map(int, input().split()) #수의 개수 N, 합을 구해야 하는 횟수 M
arr = list(map(int, input().split())) #배열값 5 4 3 2 1 (구간합을 구해야할 수 == N)
#실제 idx의 개수와 다름
#실제 idx개수는 N의 값보다 1개 더 작음

#부분합 배열은 0부터 시작한다는 것을 유의하자
prefix_sum = [0] #접두사 합 배열, 실제 0번째 idx는 사용을 하지 않을 값
sum_value = 0 #부분합 계산

for i in arr: #arr로 5 4 3 2 1
    sum_value += i #총 값을 더한다. == 15
    prefix_sum.append(sum_value) #누적합을 더한다. 5 9 12 14 15

for i in range(M): #합을 구해야하는 횟수
    s, e = map(int, input().split()) #범위 start부터 end까지
    # 3, 2, 1을 구하고 싶기 때문에 range로 생각을 했을때 마지막 값의 포함 여부와 비슷하개 생각하면 됨
    print(prefix_sum[e] - prefix_sum[s - 1])