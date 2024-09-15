# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, k, v):
    new_dict = dictionary.copy()
    new_dict.setdefault(k, v) #set default 함수는 해당 값이 없다면 그 값을 딕셔너리에 추가하게 한다
    return new_dict


my_dict = {'name': 'Alice', 'age': 25} #특정 키와 값을 이용해서 항목 추가
result = add_item_to_dict(my_dict, 'country', 'USA') #이걸 추가한 새로운 딕셔너리 반환
print(result)
