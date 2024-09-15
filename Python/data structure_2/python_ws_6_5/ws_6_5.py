# 아래 함수를 수정하시오.
def difference_sets(set_1, set_2):
    set_1 = list(set_1)
    set_2 = list(set_2)
    for s1 in set_1:
        if s1 in set_2:
            set_1.remove(s1)
    return set(set_1)


result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)


#set_1 - set_2