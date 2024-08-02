def sort_index(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j #최소값 변경
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

arr = [64, 25, 10, 22, 11]
result = sort_index(arr)
print(result)