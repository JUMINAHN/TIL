arr = [4,9,6,7,9]
count = [0]*10 #0부터 9까지 #총 10개를 담아야 한다.
temp = [0] * len(arr)

#일단 data자체를 순회한다.
for a in arr:
    count[a] += 1 #count자리에 있는 것을 담는다.
print(count)

#해당 부분을 누적합시킨다.
for i in range(1, len(count)): #0번쨰 인덱스는 누적시킬 필요가 없기 떄문에
    count[i] = count[i] + count[i-1]
print(count)

#누적시킨것을 기준으로 count가 아닌 arr값을 정렬화한다.
for i in range(len(arr), -1, -1): #뒤에서 부터 정렬화
    count[arr[i-1]] -= 1 #data의 맨마지막부터 접근 -> count에 해당되는 것을 감소시킴
    idx = count[arr[i-1]] #그 해당되는 값을
    temp[idx] = arr[i-1] #그 값을 새로운 temp에 담아주면
print(temp)