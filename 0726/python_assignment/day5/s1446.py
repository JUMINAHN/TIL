# min, max 사용중
# def find_min_max(list_num) : #최대, 최소 튜플 반환
#     return min(list_num), max(list_num)

def find_min_max(list_num) : #최대, 최소 튜플 반환
    list_num.sort()
    return list_num[0], list_num[-1]


result = find_min_max([3, 1, 7, 2, 5])
print(result)