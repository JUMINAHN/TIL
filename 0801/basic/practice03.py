# 예제 응용
def find_index(arr, find_num):
    #index로 시작해야 함
    start = 0
    end = len(arr) - 1 #end 범위 잘 정하기 #6
    while start<=end : #범위는 기억할 것
        mid = (start + end) // 2
        if arr[mid] == find_num:
            return True
        elif arr[mid] < find_num: #두개의 위치 잘보기
            start = mid+1
        else :
            end = mid-1
    return False

arr = [2,4,7,9,11,19,23] #배열
N = 18 #찾는값 --> 있는지 없는지의 유무
M = 19
result = find_index(arr, N) #flae
result2 = find_index(arr, M) #true가 되어야 함
print(result)
print(result2)


# 예제 응용
