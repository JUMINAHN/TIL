# 아래 함수를 수정하시오.
def even_elements(my_list):
    for index, my in enumerate(my_list):
        if my % 2 == 1:
            my_list.pop(index) #pop index out of range -> pop은 인덱스 안에있는 범위만 삭제가 가능하다.
    even_list = []
    even_list.extend(my_list)
    return even_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
