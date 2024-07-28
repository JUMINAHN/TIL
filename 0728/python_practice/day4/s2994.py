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
    matrix_len += 1
print(matrix_len)

for number in matrix:
    temporary_len = 0
    for line in number:
        temporary_len +=1

    if temporary_len <= 4:
        print(f'{number} 리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.')

#range와 len 을 사용하여 matrix와 matrix 리스트의 인덱스를 기준으로 순회할 수 있또록 for문 작성_중첩
#한개씩 접근하는 방법 logic 생각하기
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        print(f'{x},{y} 번째 요소의 값은 {matrix[x][y]} 입니다.')


# matrix = [
#         ['0, 1', '0, 2', '0, 3'], 
#         ['1, 0', '1, 1', '1, 2', '1, 3'], ``
#         ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
#         ['3, 0', '3, 1'], 
#         ['4, 0', '4, 1', '4, 2'], 
#         ['5, 0']
#     ]