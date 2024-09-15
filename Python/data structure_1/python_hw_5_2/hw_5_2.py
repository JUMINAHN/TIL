# 아래 함수를 수정하시오.
def count_character(string, find_string):
    number = 0
    for st in string:
        if st == find_string:
            number = number + 1
    return number


result = count_character("Hello, World!", "o")
print(result)  # 2



# def count_character(string, find_string):
#     return string.count(find_string)