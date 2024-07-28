def get_value_from_dict(my_dict, input_str):
    return my_dict.get(input_str)

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)