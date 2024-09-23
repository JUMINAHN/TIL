'''
다시 풀기
'''
#알파벳 소문자로만 이루어진 단어 S가 주어짐
#각 알파벳에 대해서 단어에 포함되어 있는 경우는 처음 등장하는 위치
#포함되어 있지 않은 경우에는 -1을 출력

#입력 : 단어S가 주어진다.
#출력 : 알파벳에 대해서 a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 구분해서 출력
S = input() #baekjoon에 대해서 찾기
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#그런데 보면 값이 처음으로 등장하는 위치를 찾는 것
#b가 처음 등장하는 위치 1번쨰 index
#a가 처음 등장하는 위치 0번쨰 index
#따라서 처음 등장하는 위치의 index를 찾으면 됨
find_idx = []
for s in S:
    find_idx.append(alpha.index(s)) #해당 index를 찾음
#print(find_idx)
#이미 나온 값이면 첫번째만 두고 두번쨰는 pass하고 -> 해당 i를 넣는다.
#find_idx에 들어있는 값 == 1 0 4 10 9 14 14 13 이거가 해당 하는 순번의 위치
#따라서 이 find_idx의 idx가 baekjoon의 결과값이 될 것
#alpha벳 전체를 돌아야하는데 find_idx에서 값이 있는지 찾아야 함
for i in range(len(alpha)):
    if i in find_idx: #find_idx에 해당되는 값이라면 --> index만 비교해야함 왜냐면 find_idx내부 값이 idx값이기 때문에
        #find_idx의 index에서 찾으세요
        #print(find_idx[i], end=' ') #i를 출력하는게 아니라 find_idx의 i를 출력해야 함

        #print(i, end=' ') #find_idx의 개수가 하나씩 나와야 하는데 --> 즉 이것은 해당 i에 값이 있다는 의미
        #find_idx를 활용해야 한다고 생각함
        #find_idx에서 1을 가지고 있는 idx위치를 반환해야 함
        print(find_idx.index(i), end=' ')
    else: #그게 아니라면 -1을 출력하세요
        print(-1, end=' ')



# #값이 없다면 -1 -> index로 찾기 : 그냥 단순히 list에 넣으면 됨
# for i in range(len(alpha)):
#     if alpha[i] in S: #해당 값에 있다면
#         print(alpha.index())


# for s in S: #s가 A~Z중 어디에 속해있는지를 찾는 것
#     print(alpha.index(s), end=' ')

