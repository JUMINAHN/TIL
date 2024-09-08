import sys
import copy
sys.stdin = open('input2477.txt')
fruit = int(input()) #밭의 면적을 구한 후 곱할 것
#6각형
six = 6
line = []
for _ in range(six): #육각형 -> 퐁당 퐁당할 것이라서 direct가 사실 필요없을 것 같음
    direct, distance = map(int, input().split())
    #순서대로 짜피 담긴다.
    line.append(distance)
#순서대로 담겨서
#제일 큰 애들 두개 뽑아서 전체 면적
first_max = 0 #남북 중 가장 큰 것 담을 곳 #0, 2, 4
second_max = 0 #동서 중 가장 큰 것 담을 곳 #1, 3, 5

first_idx = 0 #인접 idx를 찾아야하기 떄문에
second_idx = 0

#인접하지 않은 것 두개 뽑아서 면적 구하기
for i in range(0, six-1, 2): #5까지
    if first_max < line[i]:
        first_max = line[i]
        first_idx = i
for i in range(1, six, 2):
    if second_max < line[i]:
        second_max = line[i]
        second_idx = i
#print(first_idx, second_idx) -> 맞게 들어감
big_square = first_max * second_max
#print(first_max, second_max)

check_line = copy.deepcopy(line) #line 인접한 곳에 0으로 표기할 것
for i in range(six):
    if i == first_idx: #얘부터 하자
        check_line[i] = 0 #나는 0으로 만들고
        if i+1 >= six:
            i = (i+1) % six+1
        check_line[i+1] = 0 #왜이게 갑자기 멀리 가지
        if i-1<0 : #0보다 작아질 경우
            #-1을 -> 5로 바꿔줘야 하거든
            i = (i-1) % six+1 #범위를 고려했을 때
        check_line[i-1] = 0 #그게 아니면 그냥 0 넣으면 됨
for i in range(six):
    if i == second_idx: #얘부터 하자
        check_line[i] = 0 #나는 0으로 만들고
        if i+1 >= six:
            i = (i+1) % six+1
        check_line[i+1] = 0 #왜이게 갑자기 멀리 가지
        if i-1<0 : #0보다 작아질 경우
            #-1을 -> 5로 바꿔줘야 하거든
            i = (i-1) % six+1 #범위를 고려했을 때
        check_line[i-1] = 0 #그게 아니면 그냥 0 넣으면 됨
#print(line)
#print(check_line) #보면 -> 왼쪽은 됨 -> 오른쪽이 문제
#똑같이 두번쨰거도


#아닌 것을 뽑아서 곱해주기
small = 1 #곱해줄 것이기 떄문에
for i in range(six):
    if check_line[i] != 0:
        small *= check_line[i]
# print(big_square)
# print(small)
real_square = big_square - small
print(real_square * fruit)