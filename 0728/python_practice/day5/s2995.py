N = 9
data_1 = '123456789'
arr_1 = []
for data in data_1:
    arr_1.append(data)
print(arr_1)

M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
arr_2 = list(map(int, data_2.split()))
for arr in arr_2:
    if arr % 2 == 0 :
        continue
    print(arr)

# N = 9
# data_1 = '123456789'

# M = 15
# data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'