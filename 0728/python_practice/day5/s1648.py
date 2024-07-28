#set함수 사용
# def remove_duplicates(num_list):
#     return list(set(num_list))

def remove_duplicates(num_list):
    new_list = []
    for num in num_list:
        if num in new_list:
            continue
        new_list.append(num)
    return new_list

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)