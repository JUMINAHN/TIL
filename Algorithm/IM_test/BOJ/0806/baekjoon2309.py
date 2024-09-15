import sys

sys.stdin = open('input2309.txt')
T = 9
arr = []
for i in range(T):
    arr.append(int(input()))

#선택 정렬 시작!
for i in range(len(arr)-1):
    mid_idx = i
    for j in range(1+i, len(arr)):
        if arr[mid_idx] > arr[j]:
            mid_idx = j
    arr[i], arr[mid_idx] = arr[mid_idx], arr[i]

#선택 정렬된 애들로
#7명의 난쟁이의 합이 100이 넘으면 안됨
total = 0
final_arr = []
for i in range(len(arr)):
    if total >= 100:
        break
    total += arr[i]
    final_arr.append(arr[i])
for f in final_arr:
    print(f)