def even_elements(my_list):
    new_list = []
    for index, my in enumerate(my_list):
        if my % 2 == 1:
            my_list.pop(index) #list에서 pop
    new_list.extend(my_list)
    return new_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)
