#구간합
N, M = map(int, input().split()) #수의 개수 N, 합을 구해야 하는 횟수 M
#2째줄에는 N개의 개수
arr = list(map(int, input().split()))

#N,M = 각 10만씩이라서 1-10억이 된다..
#즉 M만큼 주어진 범위의 arr을 순회해야하는 것
result = []
for _ in range(M):
    # 3째줄부터는 M개의 줄에는 합을 구해야하는 구간 i와 j
    #total = 0
    i, j = map(int, input().split()) #이것은 arr을 순회해야하는 범위
    # for num in range(i-1, j): #3이면 3까지 0 1 2까지 하는것이기 때문에
    #     total += arr[num]
    result.append(sum(arr[i-1:j]))

for i in range(len(result)):
    print(result[i])
