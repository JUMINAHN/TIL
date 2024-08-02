def find_num(arr, num):
    index = 0
    while index < len(arr) and arr[index] != num:
        index += 1
    if index < len(arr):
        return index
    else:
        return -1

arr = [2,4,7,9,11,19,23] #11을 검색하는 경우
result = find_num(arr,11)
print(result) #4번 인덱스