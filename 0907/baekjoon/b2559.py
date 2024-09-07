#import sys
#단순 수열 1개 비교는 windowsliding 가능
#sys.stdin = open('input2559.txt')
#테스트 케이스 개수
# T = int(input())
# for tc in range(1, T+1):
N, K = map(int, input().split()) #배열의 총 크기 N, 구하고자 하는 것 K
arr = list(map(int, input().split()))

#이제는 또 2번 테케만 맞아
data = arr[:K]
add_num = sum(data)
max_num = sum(data)
for i in range(K, N):
    add_num = add_num + arr[i] - arr[i-K]
    if max_num < add_num:
        max_num = add_num
print(max_num)
