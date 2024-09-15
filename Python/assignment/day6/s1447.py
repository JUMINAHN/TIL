# def union_sets(set_1, set_2):
#     return set_1 | set_2

def union_sets(set_1, set_2):
    set_1 = list(set_1)
    set_2 = list(set_2)
    for s1 in set_1:
        if s1 in set_2:
            set_1.remove(s1)
    return set(set_1 + set_2)


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)