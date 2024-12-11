# def intersection_sets(num1, num2):
#     return num1 & num2

def intersection_sets(num1, num2):
    num1 = list(num1)
    num2 = list(num2)
    new_list = []
    for n1 in num1:
        if n1 in num2:
            new_list.append(n1)
    return set(new_list)

result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)