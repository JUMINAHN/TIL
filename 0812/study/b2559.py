#연속적인 날짜

#전체 날짜, 연속적 날짜
N, K = map(int, input().split())
num_list = list(map(int, input().split()))

first_sum = 0
for i in range(K):
    first_sum += num_list[i]

#윈도우 슬라이딩 -> 배운거써먹기
max_sum = first_sum

move = first_sum
for i in range(K, len(num_list)):
    move = move + num_list[i] - num_list[i-K]
    if max_sum < move:
        max_sum = move
print(max_sum)


