import sys

sys.stdin = open('arr_test_same.txt')

#[[1 2 3],[4,5,6],[7,8,9]]
arr = [list(map(int, input().split())) for i in range(3)]
max_r, max_c = 0,0
for row in range(len(arr)):
    r, c = 0,0
    for column in range(len(arr[row])):
        r += arr[row][column]
        c += arr[column][row]
    if max_r < r:
        max_r = r
    if max_c < c:
        max_c = c
print('max_r', max_r)
print('max_c', max_c)


