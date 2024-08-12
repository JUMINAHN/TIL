#시간초과가 떳던 방법으로 풀기
N, K = map(int, input().split())
num_list = list(map(int, input().split()))


max_num = 0

for i in range(len(num_list)-K):
    sum = 0
    for j in range(i, i+K): #원하는 범위 만큼 더하기
        sum += num_list[j]
    if max_num < sum :
        max_num = sum
print(max_num)

