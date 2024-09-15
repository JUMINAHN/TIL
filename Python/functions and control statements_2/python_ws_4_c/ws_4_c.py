matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]

matrix_len = 0
for m in matrix:
    matrix_len = matrix_len + 1
print(matrix_len)


for number in matrix: #['0,1', '0,2', '0,3']
    temporary_len = 0
    for n in number:
        temporary_len = temporary_len + 1
    if temporary_len <= 4:
        print(f'{number} 리스트는 {temporary_len}개만큼 요소를 가지고 있습니다')


#range와 len을 사용해서 matrix와 matrix 
#matrix의 x,y 번째 요소 값은 matirx입니다.
for x in range(len(matrix)) : #0부터 5번까지 돌건데 
    for y in range(len(matrix[x])):
        print(f'matrix의 {x}, {y}번째의 요소의 값은 {matrix[x][y]} 입니다.')



# for x in matrix:
#     for y in x:
#         print(f'matrix의 {y}번째 요소의 값은 {y} 입니다.')




# #위에 있는걸 활용할 수 있을 것 같단 말임
# for x in range(len(matrix)) : #0부터 5번까지 돌건데 --> 개수니까 x번째 요소
#     for m in matrix:
#     print(f'matrix의 {x}, 번째 요소의 값은')