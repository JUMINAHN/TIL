N = int(input())
arr = [0] * 1000000000 #10억 error 예상
for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        arr[i] = 1
count = 0
for i in range(len(arr)):
    if arr[i] == 1:
        count += 1
print(count)