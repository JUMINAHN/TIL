# 아래 함수를 수정하시오.
def intersection_sets(set_1, set_2):
    set_1 = list(set_1)
    set_2 = list(set_2)
    result = []
    for s1 in set_1:
        if s1 in set_2:
            result.append(s1)
    return set(result)


result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)



#set_1 & set_2