# my_multi(2, 3) 결과 : 6
# 함수를 수정하고 호출 결과를 result_1 변수에 할당하여 출력하시오.
def my_multi(num1, num2):
    return num1 * num2

result_1 = my_multi(2,3)
print(result_1)

# is_negative(3) 결과 : False
# 함수를 수정하고 호출 결과를 result_2 변수에 할당하여 출력하시오.
def is_negative(num):
    if num < 0 :
        return True
    else :
        return False

result_2 = is_negative(3)
print(result_2)

def default_arg_func(default='기본 값'): #기본 인자값 => 매개변수에 할당
    return default

result_3 = default_arg_func() #기본 인자값 -> postional
print(result_3)

result_4 = default_arg_func('다른 값')
print(result_4)


# my_multi(2, 3) 결과 : 6
# 함수를 수정하고 호출 결과를 result_1 변수에 할당하여 출력하시오.
# def my_multi():
#     pass

# result_1 = my_multi(2,3)
# print(result_1)

# # is_negative(3) 결과 : False
# # 함수를 수정하고 호출 결과를 result_2 변수에 할당하여 출력하시오.
# def is_negative():
#     pass

# result_2 = is_negative(3)
# print(result_2)

# def default_arg_func():
#     pass

# result_3 = default_arg_func()
# print(result_3)



