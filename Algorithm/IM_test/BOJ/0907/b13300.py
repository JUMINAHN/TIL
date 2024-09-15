# import sys
#
# sys.stdin = open('input13300.txt')
# #테스트 케이스 개수
# T = int(input())
# for tc in range(1, T+1):
years = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]} #학년별 카테고리를 담을 인원 편성
N, K = map(int, input().split()) #학생수, 최대 배정 가능 인원
for _ in range(N): #학생별 내용 확인
    S, Y = map(int, input().split())
    data_list = years.get(Y)
    data_list.append(S) #성별 append 해주기
#같은 학년을 모은다
#print(years)
#값이 담겨진 것 기반으로 계산

room = 0 #편성 방
#모은 학년에서 성별을 확인한다
#성별만큼 loop를 돈다.
for i in range(len(years)):
    # 각 성별이 몇 개 인지 count한다
    data = years.get(i+1)
    girl = data.count(0)
    boy = data.count(1)
    #x//k를 해서 그만큼 방을 편성한다.
    room += girl // K
    room += boy // K
    if girl % K != 0:
        room += 1
    if boy % K != 0:
        room += 1
    #만약 나누어 떨어지지 않을경우 -> x % k !=0일 경우 방에 1을 준다.
print(room)