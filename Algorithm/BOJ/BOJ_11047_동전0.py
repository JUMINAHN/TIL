#준규가 있는 동전은 총 N종류
#동전을 적절히 사용해서 가치의 합을 K로만들려고 한다.
#필요한 동전 개수의 최소값을 구한다.
#동전 종류 N, 동전 액수 K
#동전 N개

N, K = map(int, input().split()) #10, 4200원
coin = [int(input()) for _ in range(N)] #N만큼 input을 받고
coin.sort(reverse=True) #reverse가 되는지 확인해보자 == 맞게 되고
#print(coin) == 정렬되었고

#COIN의 범위를 최소화하자
# for i in range(N):
#     #print(coin[i])
#     if coin[i] > K : #k보다 크다면 -> 없앤다.
#         coin.pop(i) #index out of range??
# print(coin)
# print(coin)

#가장 큰 것만?
my_coin = []
for c in coin:
    if c > K: #정렬했으니까 괜찮음
        continue
    my_coin.append(c)
#        coin.remove(c) #제거한다
#print(my_coin)

#d이걸로 계산
count = 0
for my in my_coin:
    # if K % my != 0:
    count += K // my
    K = (K % my)
print(count)
#
# count = 0
# for c in coin: #큰 것 부터 50000을 한다.
#     #일단 k보다 C가 크면 안되니까 K보다 c가 크면 모두 패스 -> 굳이 xx
#     #위치 유의
#     if (K % c) != 0: #ZeroDivisionError
#         K -= (K % c)
#         #그리고 계산을 한다.
#         K = (K//c)
#         count += 1
#     #근데 애초에 break를 할필요가 없는게 다 자체적인 필터가 됨
# print(count)