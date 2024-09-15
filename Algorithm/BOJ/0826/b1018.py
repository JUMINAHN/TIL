N, M = int(input()) #전달받은 사각형
arr = [list(input()) for _ in range(N)] #N만큼
X = 8

line1 = ['W','B','W','B','W','B','W','B']
line2 = ['B','W','B','W','B','W','B','W']

#흰색배열 먼저
want_chess1 = []
for i in range(X):
    if i % 2 == 0: #짝수일떄 line1먼저
        want_chess1.append(line1)
    else :
        want_chess1.append(line2)

#검은색 배열 먼저
want_chess2 = []
for i in range(X):
    if i % 2 == 0: #짝수일떄 line1먼저
        want_chess2.append(line2)
    else :
        want_chess2.append(line1)

#해당 사각형을 기준으로 원하는 체스판과 일치하는게 가장 많은 것을 찾아서 counting

#검정색 기준
# for i in range(0, N-X+1): #체스판
#     for row in range(i, i+X): #체스만큼
#         for col in range(i, i+X) : #여기는 M을 해야할텐데,,
#             if arr[]

#흰색 기준