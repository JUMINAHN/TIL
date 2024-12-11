# 아래 함수를 수정하시오.
def remove_duplicates_to_set(list_data):
    list_data = set(list_data) 
    return list_data #set자체를 반환해야 한다.


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
