arr1 = ['a', 'b', 'c', 'd', 'e', 'f']
arr2 = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ']
arr3 = [1, 2, 3, 4, 5, 6]
#zip은 하나씩 묶음

result = zip(arr1, arr2, arr3)
#print(result)
#print(list(result))

# for i in result: #zip으로 묶여진 리스트에 하나씩 나오는 것을 확인할 수 있음
#     print('i', i)


#요소 하나하나가 나누어 들어와짐
for a,b,c in result:
    print('a에 들어가는 것 : ', a, 'b에 들어가는 것 : ',b, 'c에 들어가는 것 : ',c )

# for a, b, c in zip(arr1, arr2, arr3):
#     print(f'{"".join(map(str, a))} {"".join(map(str, b))} {"".join(map(str, c))}')