def find_index(arr, find_num):
    i = 0
    while i < len(arr) and arr[i] != find_num :
        i += 1
    if i < len(arr):
        return i
    else :
        return -1

find_num1 = 3
find_num2 = 101
arr = [2, 77, 8, 99, 4, 6, 3, 22, 10, 9]
result = find_index(arr, find_num1) #있는 것
result2 = find_index(arr, find_num2) #없는 것
print(result)
print(result2) #없음의 -1, 맨마지막 인덱스인 -1과 헷갈리는 것 주의