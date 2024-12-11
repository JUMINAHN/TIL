# 아래 함수를 수정하시오.
def remove_duplicates(list_data): #중복된 요소를 제거한 새로운 리스트를 반환하는 함수를 작성
    new_lst = []
    new_lst.extend(list_data)
    new_lst= list(set(new_lst))
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
