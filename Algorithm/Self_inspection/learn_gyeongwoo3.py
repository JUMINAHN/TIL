# 두 개의 주사위를 던져서 나올 수 있는 모든 경우의 수를 계산하는 예제
# 결과를 저장할 리스트
# 모든 경우의 수를 담았음
# results = []
# for dice1 in range(1, 7):
#     for dice2 in range(1, 7):
#         data = [dice1, dice2]
#         results.append(data)
# print(results)

#두 개의 주사위를 던져서 나올 수 있는 모든 경우의 수의 합을 계산하는 예제
results2 = []
for dice1 in range(1,7):
    for dice2 in range(1,7):
        total = dice1 + dice2 #경우의 수
        results2.append(total)
print(results2)
print(len(results2)) #모든 경우의 수

#특정 조건을 만족하는 경우의 수
#합이 7인 경우
total = 0
for r in results2:
    if r == 7 :
        total += 1
print(total)
