N, K = map(int, input().split()) #N:온도를 측정한 전체 날짜의 수 K:온도의 합을 구하기 위한 연속적인 날짜
arr = list(map(int, input().split()))

#windowsliding 사용

sum_slide = arr[:K+1] #idx K까지 짤리기 떄문에 K + 1을 해줬따
max_sum = sum(sum_slide)
for i in range(N-K, N):
    result = sum_slide + sum_slide[i-K] + arr[i]
    if max_sum < result:
        max_sum = result
print(max_sum)