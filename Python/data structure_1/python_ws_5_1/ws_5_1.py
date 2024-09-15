# 아래 함수를 수정하시오.

def reverse_string(result):
    new_data = reversed(result) #reversed는 객체로 반환됨
    return ''.join(new_data)


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH



# def reverse_string(result):
#     new_data = reversed(result) #reversed는 객체로 반환됨
#     return new_data


# result = reverse_string("Hello, World!")
# print(result)  # !dlroW ,olleH
