#버블정렬 연습해보기 -> 뭔가 뇌가 기억하고 있음
arr = [55,7,78,12,42] #버블
for i in range(len(arr)-1, -1, -1):
    for j in range(0, i) : #맨 뒤랑 비교
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)