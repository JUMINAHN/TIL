#5:2 ~ 6:1
import sys #육각형으로 고정이 됨
sys.stdin = open('input2477.txt')
#테스트 케이스 개수
fruit = int(input()) #참외의 수
six = 6
arr = [0] * six #육각형 -> 들어갈 배열
#C == 남 / 북 (3/4)
#R == 동 / 서 (1/2)

#시작이 C인지 R인지 판별하기 위해서
#C가 먼저 시작한다면 cmax가 아닌것에서 2번째의 col을 가져오게 된다. -> 1 3 5에서
start_col = -1
#R이 먼저 시작한다면 rmax가 아닌것에서 2번쨰의 row를 가져오게 된다. -> 1 3 5에서
start_row = -1

for i in range(six):
    direct, distance = map(int,input().split()) #C,R,C,R,C,R 이나 R,C,R,C
    arr[i] = distance #거리를 계속 대입할 것
    if (direct == 3 or direct == 4) and i == 0:
        start_col = 0
    elif (direct == 1 or direct == 2) and i == 0: #1이나 2이면
        start_row = 0
#이제 원하는 배열이 들어가고
if start_col == 0:
    start_row = 1
else : #col이 -1라면
    start_row = 0
#제일 큰 것 빼고,,, 먼저 시작한 것 모름...