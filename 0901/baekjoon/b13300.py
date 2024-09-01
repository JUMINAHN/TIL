#방배정..
# import sys
#
# sys.stdin = open('input13300.txt')
# #테스트 케이스 개수
# T = int(input())
# for tc in range(1, T+1):
N, K = map(int, input().split()) #학생 수, 한방 최대 가능 인원 K
year = {1: [] , 2: [], 3: [], 4: [] , 5: [] , 6: []}
for i in range(N):
    S, Y = map(int, input().split())
    list_data = year.get(Y) #list자체이고 -> 학년 대조
    list_data.append(S) #하면 이제 -> 성별을 기반으로 성별을 인풋하게 됨
#print(year)#: 학년별로 성별이 들어간 것을 확인하 수 있음
#print(len(year)) -> dictionary는 key자체의 길이를 가지고 있기 떄문에
room = 0 #방의 개수
for i in range(len(year)): #학년만큼 돌 것인데
    list_data = year.get(i+1) #하면 key값이 나올 것 -> 1이 들어있는 성별들이 있는 배열 [0,1,0] 예시
    girl = list_data.count(0) #여자를 센다
    boy = list_data.count(1) #남자를 센다
    room += (girl // K)
    room += (boy // K)
    #남은 나머지들은?
    if girl % K != 0: #elif로 설정을 했기 떄문이었다.
        room += 1
    if boy % K != 0:
        room += 1
print(room)