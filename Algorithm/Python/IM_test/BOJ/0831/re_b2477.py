#블로그에서 팁을 받고 진행
import sys
sys.stdin = open('input2477.txt')
#테스트 케이스 개수

fruit = int(input()) #참외의 개수
six = 6
farm = [0] * six #농장

for i in range(six):
    direct, distance = map(int, input().split()) #방향, 거리
    farm[i] = distance
#print(farm)

#어쨌든 farm안에 값이 들어가있을 것
max_idx_1 = 0 #1, 3, 5의 max
max_idx_2 = 1 #2, 4, 6의 max -> 초기값 세팅이 잘못되어있었음

max_wh1 = farm[max_idx_1] #넓이를 구할 값
max_wh2 = farm[max_idx_2] #초기값 세팅을 이상하게함

for i in range(0, six, 2): #0,2,4
    if farm[max_idx_1] < farm[i]:
        max_idx_1 = i #0
        #print('1', i)
        max_wh1 = farm[i] #160

for i in range(1, six, 2): #1, 3, 5
    if farm[max_idx_2] < farm[i]:
        #print('2', i)
        max_idx_2 = i
        max_wh2 = farm[i]
# print(max_wh1)
# print(max_wh2)

max_square = max_wh1 * max_wh2 #큰 정사각형의 넓이#
# print(max_square)
#print(max_square) #값이 왜 안들어가지?
#찾으면 0으로 만든다.
#일단 만약 max_idx_1 이나 2가 N을 초과한다면 0으로
for i in range(six): #farm을 모두 순회할 것인데
    if i == max_idx_1 :#일단 idx_1인거부터
        farm[max_idx_1] = 0
        farm[(max_idx_1+1) % 6] = 0
        farm[(max_idx_1-1) % 6] = 0

    elif i == max_idx_2:
        farm[max_idx_2] = 0#인접 idx
        farm[(max_idx_2+1) % 6] = 0
        farm[(max_idx_2-1) % 6] = 0

#print(farm)
#자 이제 for를 순회하면서 i가 0이 아닌 것
sub_square = 1 #곱할 것
for i in range(six):
    if farm[i] != 0:
        sub_square *= farm[i]
#print(sub_square) #0이 왜 2개 ?

#농장의 넓이
farm_stage = max_square - sub_square
print(farm_stage * fruit)



#이거 원형 큐 사용하면 개꿀인데..
