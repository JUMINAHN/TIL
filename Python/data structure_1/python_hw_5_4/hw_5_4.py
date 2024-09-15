# 아래 함수를 수정하시오.
# sort, min, max 사용 금지
def find_min_max(list_data):
    max_num, min_num = list_data[0], list_data[0]
    for data in list_data :
        if data > max_num :
            max_num = data 
        if data < min_num :
            min_num = data
    return min_num, max_num 

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)


# min max 확인
# def find_min_max(list_data):
#     return min(list_data), max(list_data)


# result = find_min_max([3, 1, 7, 2, 5])
# print(result)  # (1, 7)
