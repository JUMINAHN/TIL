#롤케이크
#출력에는 가장 많이 받을 것 같은 방청객 번호, 실제로 많이받은 방청객 개수 --> 만약 두명이라면 번호가 더 작은 방청객으로
#continue에 짜피 가장 큰 애가 있을 것이니까 >= 로 설정하지 않는 이상 업데이트가 되지 않을 것임

L = int(input()) #롤케이크 길이
lcake = [0] * L #길이만큼 롤케이크 만들기
N = int(input()) #방청객 수

expect_max = 0
expect_idx = 0
for i in range(1, N+1):
    Pi, Ki = map(int, input().split()) #P부터 K까지
    my_expect = 0
    for j in range(Pi-1, Ki):
        my_expect += 1 #내 예상 케이크 개수
        if not lcake[j] == 0: #내가 원하는 의도가 들어가지 않는 다는 것 --> 조건 수정 --> print 중간 찍어보기
            continue
        else : #이면 -> 아니면
            lcake[j] = i #롤케이크에 각 번호를 넣는다
    if expect_max < my_expect:
        expect_max = my_expect
        expect_idx = i
#print(lcake)
#lcake안의 번호를 counting
count = [0] * (L+1) #0번은 사용하지 않을 것 , 1,2,3만 뽑을 것
for l in lcake:
    if l == 0:
        continue
    count[l] += 1
real_idx = 0
for i in range(len(count)):
    if count[real_idx] < count[i]:
        real_idx = i

print(expect_idx)
print(real_idx)
#print(real_idx)