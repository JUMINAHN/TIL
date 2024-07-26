# 아래 함수를 수정하시오.
def remove_duplicates(list_data): 
    new_list = list(set(list_data)) #중복 제거를 위해 -> set사용
    return new_list

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
