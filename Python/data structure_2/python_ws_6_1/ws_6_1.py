# 아래 함수를 수정하시오.
def union_sets(set_1, set_2):
    set_1 = list(set_1)
    set_2 = list(set_2)
    for s1 in set_1:
        if s1 in set_2:
            set_1.remove(s1)
    #print(set_1)
    # result = set_1.extend(set_2) --> set1자체에 추가하는 것이기 때문에 이것 유의하기
    set_1.extend(set_2) 
    return set(set_1)


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)



# set 자체 함수 사용시
# def union_sets(set_1, set_2):
#     result = set_1 | set_2
#     return result