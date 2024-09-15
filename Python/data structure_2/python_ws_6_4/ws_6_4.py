# 아래 함수를 수정하시오. #모든 키를 담은 리스트 반환
def get_keys_from_dict(my_dict):
    result = my_dict.keys()
    return list(result)


my_dict = {'name': 'Alice', 'age': 25} #모든 키를 리스트로 반환하는 get_keys_fro_dict
result = get_keys_from_dict(my_dict) #dict을 인자로 받아서
print(result)  # ['name', 'age']
