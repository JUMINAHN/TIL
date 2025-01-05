import sys

sys.stdin = open('input2304.txt')
tank_count = int(input())
N = 1000
#핵심은 가장 큰 숫자를 기준으로 좌/우 나누는 것

tank = [0] * (N+1) #1000개? -> 일단 0은 비워둔다고 생각하고 접근한다고 가정했을때 1001개를 만들어줘야 함
for _ in range(tank_count):
    L, H = map(int, input().split())
    tank[L] = H #tank에 높이에 값을 넣는다.
#지금 값이 들어가있는 상태
#가장 높은 height를 가지고 있는 idx를 찾자
max_idx = 0
for i in range(N):
    if tank[max_idx] < tank[i]:
        max_idx = i
#print(max_idx) : 맞게 나오는 것 확인했고
#앞 / 뒤 비교할 것
#앞 비교 : 가장 큰 값 까지
for i in range(max_idx): #왜냐면 i i+1까지할 것이기 떄문에 범위가 초과날일은 없지만 일단 체크
    if tank[i] > tank[i+1]:
        tank[i+1] = tank[i] #tank[i]의 정보를 그대로 준다.
#뒤 비교 : 역순으로
for i in range(N, max_idx, -1): #1001까지니까 1000이 마지막 idx번호긴 함
    if tank[i] > tank[i-1]: #i가 첫번째가 더 크기 떄문에
        tank[i-1] = tank[i]
#현재 탱크값이 맞게 들어와있는지 확인해보자 : print(tank)
#들어와있는 tank들의 높이를 모두 더하면 된다.
total = 0
for t in tank:
    total += t
print(total)

