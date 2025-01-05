# N명의 사람들이 줄서있다. -> 1번부터 줄서있음
# 사랃들이 줄을 서는 순서에 따라서 인출에 필요한 시간합이 달라짐
# 주어진순서대로 선다면 인출에 소요되는 시간의 합이 달라짐
# 즉 제일 시간이 오래걸리는 애를 맨 뒤로 보내면 되지 않을까?
# 즉 줄서있는 사람 수 N과, 각 사람이 돈을 인출하는데 걸리는 시간이 주어졌을떄
# 최솟값
N = int(input())
line = list(map(int, input().split()))
line.sort() #오름차순
#누적합 ->
sum = 0
result = []
for l in line:
    sum += l #누적으로 확인할 것
    result.append(sum)
total = 0
for r in result:
    total += r
print(total)