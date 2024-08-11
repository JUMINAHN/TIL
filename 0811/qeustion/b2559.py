#슬라이딩 윈도우
#범위 10만 이상이면 for루프로 로직 구현 XX
N, K = map(int, input().split())
data = list(map(int, input().split()))
#맨앞에꺼, 맨뒤에꺼 빼기



total = sum = 0
for i in range(K):
    sum += data[i]
    total += data[i]

for i in range(K, N):#i는 k부터 오른쪽으로 빠지고 i-K는 맨 앞
    sum = sum + data[i] - data[i-K]
    if total < sum:
        total = sum
print(total)
print(sum)