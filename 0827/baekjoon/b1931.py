#못품, 접근 방식 감도 못잡음

N = int(input())
start = []
end = []
for _ in range(N):
    s, e = map(int, input().split())
    start.append(s)
    end.append(e)

#이걸 start 기준으로 선택 정렬
for i in range(N - 1):
    min_idx = i
    for j in range(1+i, N):
        if start[min_idx] > start[j]:
            min_idx = j
    start[i], start[min_idx] = start[min_idx], start[i] #시작 기준
    end[i], end[min_idx] = end[min_idx], end[i] #끝 기준

max_count = 0
#이 for가 반복되면 좋겠어 왜냐하면 계속 경우를 비교해줘야 하니까
#근데 저 for는 위의 기준으로 계속 바뀌면 좋겠어
for i in range(N): #회의실 모두 순차적으로 순회
    count = 0
    find_i = i
    for j in range(i, N): #회의실 start, end 기반으로 순회
        find_e = end[find_i]
        count += 1
    if find_e >= start[j]:
        find_e = end[j] #위치를 넣고
        count += 1 #찾았으니까 count 1해주고
    if max_count <= count:
        max_count = count
print(max_count)