def sort_tuple(num_tuple) : #set이랑 dict은 순서의 정함이 없음
    num_tuple = list(num_tuple)
    num_tuple.sort()
    return(tuple(num_tuple))


result = sort_tuple((5, 2, 8, 1, 3))
print(result)



# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)