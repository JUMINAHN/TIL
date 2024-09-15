#selectsort - 선택정렬 :: 작은 값은 원소부터 차례대로 선택하여 위치를 교환하는 방식 O(n2)
arr = [64,25,10,22,11]
for i in range(len(arr) - 1): #맨뒤거는 터치 x
    min_idx = i #가장 작은 것 -> idx 기준
    for j in range(i+1, len(arr)): #맨 마지막은 정렬할 필요 x
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(arr)
print('-'*30)

#이진검색 -> binary 설치 :: 자료가 정렬된 상태여야하고 중간값과 찾고자하는 값을 비교
def find_num(arr, find_key):
    #idx 기준
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == find_key:
            return True #잘보기
        elif arr[mid] > find_key:
            end = mid -1
        else :
            start = mid + 1
    return False

arr = [2,4,7,9,11,19,23]
find_key = 7
result = find_num(arr, find_key)
print(result) #찾았는지 아닌지 true false
print('-' * 30)

#카운팅 정렬 : 발생회수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열에 저장한다
arr = [0,4,1,3,1,2,4,1]
count = [0] * 5
temp = [0] * len(arr)
# 다른것과 다르게 유일하게 먼저 data로 접근 -> 그리고 idx -> idx
for a in arr:
    count[a] += 1

for i in range(1, len(count)) : #처음은 누적이라 셀필요가 없음
    count[i] = count [i-1]

for r in range(len(arr), -1, -1) : #뒤부터 접근
    count[arr[r-1]] -= 1
    idx = count[arr[r-1]]
    temp[idx] = arr[r-1]

print(temp)