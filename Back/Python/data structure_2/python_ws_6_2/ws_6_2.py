# 아래 함수를 수정하시오.
def get_value_from_dict(my_dict, key): #dict과 key를 인자로 받아서 키에 대응하는 값을 반환
    return my_dict.get(key)


my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name') #이 값을 가져오는 함수를 작성
print(result)  # Alice
