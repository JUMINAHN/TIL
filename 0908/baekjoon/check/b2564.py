import sys

sys.stdin = open('../input2564.txt')
#가로, 세로
C, R = map(int, input().split())
north = [0] * C #1
east = [0] * R #4
south = [0] * C #2
west = [0] * R #3

store = int(input())
for i in range(1, store+1):
    direct, distance = map(int, input().split())
    if direct == 1:
        north[distance] = i
    elif direct == 2:
        south[distance] = i
    elif direct == 3:
        west[distance] = i
    else :
        east[distance] = i
direct, distance = map(int, input().split())
if direct == 1:
    north[distance] = 'X'
elif direct == 2:
    south[distance] = 'X'
elif direct == 3:
    west[distance] = 'X'
else:
    east[distance] = 'X'
line = north + east + south[::-1] + west[::-1]
#print(line)
X_idx = 0
for i in range(len(line)):
    if line[i] == 'X':
        X_idx = i
print(X_idx)


print(line)
#왼쪽 / 오른쪽 모두 비교해야 함
total = 0
for i in range(1, store+1): #찾을 상점
    store_idx = 0
    for j in range(len(line)):
        if line[j] == i:
            store_idx = j
    #찾은 것에서 X_idx 빼주기
    if store_idx < X_idx:
        total += (X_idx - store_idx)
    else :
        total += (store_idx - X_idx)
print(total)

# total = 0
# for i in range(1, store+1): #찾을 상점
#     store_idx = 0
#     for j in range(len(line)):
#         if line[j] == i:
#             store_idx = j
#     #찾은 것에서 X_idx 빼주기
#     if store_idx < X_idx:
#         total += (X_idx - store_idx)
#     else :
#         total += (store_idx - X_idx)
# print(total)
