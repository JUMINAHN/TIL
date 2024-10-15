#야호 바로했따
N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = []
visited = [False] * (N) #idx -> 일단 비움

def recur(num):
    if num == M:
        print(" ".join(map(str, result)))

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(data[i])
            recur(num+1)
            visited[i] = False
            result.pop()

recur(0) #0번쨰 idx