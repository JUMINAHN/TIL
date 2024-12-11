# def difference_sets(num1, num2):
#     num1 = list(num1)
#     num2 = list(num2)

#     for n1 in num1:
#         if n1 in num2:
#             num1.remove(n1)
#     return set(num1)
def difference_sets(num1,num2):
    return num1 - num2

result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)
