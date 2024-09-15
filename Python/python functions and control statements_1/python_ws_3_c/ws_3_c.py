def recur_example(number):
    if number == 1:
        return 1
    else:
        return number + recur_example(number - 1)
result_1 = recur_example(5)
print(result_1) 


def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base*power(base, exponent - 1)
result_2 = power(2, 3)
print(result_2) 

def sum_of_digits(number):
    if number < 10:
        return number
    else:
        return (number%10) + sum_of_digits(number // 10)
result_3 = sum_of_digits(321)
print(result_3) 