# def remove_duplicates_to_set(num_list):
#     return set(num_list)

# set말고 중복 제거 하는 방법.. -> list로
def remove_duplicates_to_set(num_list):
    for num in num_list:
        if num_list.count(num) >= 2:
            num_list.remove(num)
    return set(num_list)


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)



# result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
# print(result)