def my_multi(number_1, number_2):
    return number_1 * number_2
# my_multi(2, 3) 결과 : 6
# 함수를 수정하고 호출 결과를 result_1 변수에 할당하여 출력하시오.
result_1 = my_multi(2,3)
print(result_1)

def is_negative(number):
    if number < 0:
        return True
    else :
        return False
# is_negative(3) 결과 : False
# 함수를 수정하고 호출 결과를 result_2 변수에 할당하여 출력하시오.
result_2 = is_negative(3)
print(result_2)


def default_arg_func(default='기본 값'):
    return default

result_3 = default_arg_func()
print(result_3)

result_4 = default_arg_func('다른 값')
print(result_4)
