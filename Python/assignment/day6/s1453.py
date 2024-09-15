#update 함수 사용
def add_item_to_dict(dic_info, key_info, value_info):
    new_dict = {key_info : value_info}
    dic_info.update(new_dict)
    return dic_info

#setdefualt 사용
# def add_item(d_info, k_info, v_info):
#     d_info.setdefault(k_info, v_info)
#     return d_info

# print('-'*30)
# result = add_item(my_dict,'country','USA')
# print(result)



my_dict = {'name': 'Alice', 'age': 25} 
result = add_item_to_dict(my_dict, 'country', 'USA') 
print(result)




# my_dict = {'name': 'Alice', 'age': 25} 
# result = add_item_to_dict(my_dict, 'country', 'USA') 
# print(result)