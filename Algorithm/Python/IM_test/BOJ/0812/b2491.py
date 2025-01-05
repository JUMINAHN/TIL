num = int(input())
num_list = list(map(int, input().split()))


max_len1 = 1
num_len1 = 1 #나의 값까지 포함
#길이가 큰 값 출력
for i in range(1, len(num_list)):
    if num_list[i] >= num_list[i-1]:
        num_len1 += 1
    else :
        num_len1 = 1
    if max_len1 < num_len1:
        max_len1 = num_len1

min_len1 = 1
num_len2 = 1 #나의 값까지 포함
#길이가 작은 값 출력
for i in range(1, len(num_list)):
    if num_list[i] <= num_list[i-1]:
        num_len2 += 1
    else :
        num_len2 = 1 #초기화 값이 1이어야 함 --> 나의 값
    if min_len1 < num_len2:
        min_len1 = num_len2

if min_len1 < max_len1:
    print(max_len1)
else :
    print(min_len1) #3이상인 경우가 없기 때문에
