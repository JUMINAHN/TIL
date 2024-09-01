arr = [1,2,3,4,5] #5가 있는 위치
result = arr.index(5) #4번 idx
print(result)

result2 = arr.index(2) #2가 있는 위치
print(result2) #예상 1

#result3 = arr.index(7)
#print(result3) -> error발생

#result4 = arr.find(7) __> find가 없다
#print(result4)

t_col = [0] * (11)
if 1 in t_col:
    print('yes')
else :
    print('no')