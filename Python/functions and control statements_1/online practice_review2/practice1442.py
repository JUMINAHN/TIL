# sort 함수 사용
def sort_tuple(exist_tuple): #5,2,8,1,3
    exist_tuple = list(exist_tuple)
    how_many = 0
    for e in exist_tuple:
        how_many += 1    

    for i in range(how_many-1, 0, -1):
        for j in range(i):
            if exist_tuple[j] > exist_tuple[j+1]:
                exist_tuple[j], exist_tuple[j+1] = exist_tuple[j+1], exist_tuple[j]
    return tuple(exist_tuple)

result = sort_tuple((5, 2, 8, 1, 3))
print(result)


