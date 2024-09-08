import sys

def cal_dist(loc, distance):
    if loc == 1:
        return distance
    elif loc == 4:
        return C+distance
    elif loc == 2:
        return C+R+C-distance
    elif loc == 3:
        return C+R+C+R-distance

sys.stdin = open('input2564.txt')
#테스트 케이스 개수
C,R = map(int, input().split())
col_box = [0] * C
row_box = [0] * R

store = int(input())
location = [0] * (store+1) #상점개수만큼 -> 0번 idx는 사용하지 않을 것

dist = []
for i in range(store+1): #상점의 위치와 동근이의 위치 입력받기
    loc, distance = map(int, input().split())
    dist.append(cal_dist(loc, distance))

#동근이의 위치 저장
dong_dist = dist[-1]
#print(dong_dist) #동근이의 위치

total = 0
for i in range(store):
    #동근이와 상점의 절대값을 구한다.
    cal = abs(dist[i] - dong_dist)

    #전체 길이를 구해준다
    h = 2*(C+R)
    total += min(cal, h-cal) #더 짧은 것
print(total)