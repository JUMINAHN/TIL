#일단 지금 전체너비를 사용할 일이 없어서 arr을 만들진 않겠습니다.
#종이자르기 방식처럼 접근하겠습니다.
box_num = int(input())
col_line = []
row_line = []
for _ in range(box_num):
    c, r = map(int, input().split())
    col_line.append(c)
    row_line.append(r)
#print(col_line) -> 일단 같이 바껴야 할듯 -> 묶음이니까
#print(row_line)
for i in range(len(col_line)-1):
    min_idx = i
    for j in range(i+1, len(col_line)):
        if col_line[min_idx] > col_line[j]:
            min_idx = j
    col_line[i], col_line[min_idx] = col_line[min_idx], col_line[i]
    row_line[i], row_line[min_idx] = row_line[min_idx], row_line[i]

#print(col_line)
#print(row_line)
for i in range(1, len(row_line)):
    if row_line[-1] == i:
            break
    elif row_line[i] < row_line[i - 1]:
        row_line[i] = 0 # 같이 없애 버려 --> remove 요소 삭제 안없어졌는데
        col_line[i] = 0
print(col_line) #-> 원하는대로 바꼈어 -> 8은 9까지 짤려야하는데,,
print(row_line)
#그리고 row가 만약 바로 앞보다 작으면 날려버려
# for i in range(1, len(row_line)): #맨처음은 상관이 없을 것 같음
#     # 맨 마지막 살리는 방법
#     if row_line[-1] == i:
#         break
#     elif row_line[i] < row_line[i - 1]:
#         row_line.pop(i)  # 같이 없애 버려 --> remove 요소 삭제 안없어졌는데
#         col_line.pop(i)


