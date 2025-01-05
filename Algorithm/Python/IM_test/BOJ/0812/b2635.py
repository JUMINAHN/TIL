N = int(input())

max_result = []
for i in range(1, N+1): #양의 정수 중 선택 #100전까지
    temp = [N]
    temp.append(i)
    while temp[-2] - temp[-1] >= 0:
        result = temp[-2] - temp[-1]
        temp.append(result)

    if len(max_result) < len(temp):
        max_result = temp
print(len(max_result))
for max in max_result:
    print(max, end = " ")