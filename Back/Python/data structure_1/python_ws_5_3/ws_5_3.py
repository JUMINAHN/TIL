# 아래 함수를 수정하시오. --> max도 사용이 안됨
def sort_tuple(exist_tuple): #5,2,8,1,3
    exist_tuple = list(exist_tuple) #list
    #개수가 얼마인지
    how_num = 0
    for exist in exist_tuple:
        how_num += 1
    
    for i in range(how_num-1, 0, -1):
        for j in range(i):
            if exist_tuple[j] > exist_tuple[j+1] :
                exist_tuple[j], exist_tuple[j +1] = exist_tuple[j+1], exist_tuple[j]
    return tuple(exist_tuple)

    #for i in range()

            
    #return tuple(new_list) 


result = sort_tuple((5, 2, 8, 1, 3))
print(result)


# dirtybubble
    # new_list = [exist_tuple[0]]
    # for index, exist in enumerate(exist_tuple):
    #     if index == 0:
    #         continue
        
    #     if exist > exist_tuple[index - 1] : #위치 바꾸기
    #         new_list.insert(index, exist)
    #     elif exist < exist_tuple[index - 1] :
    #         new_list.insert(index-1, exist)

