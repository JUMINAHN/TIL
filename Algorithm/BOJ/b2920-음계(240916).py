# import sys
#
# sys.stdin = open('input2920.txt')
# #테스트 케이스 개수
# T = int(input())
# for tc in range(1, T+1):

#총 8개의 음으로 구성
#주어진 알파벳과 숫자 변환
#1부터 8까지 차례대로 연주된다면 ascending
#8부터 1까지 차례대로 연주된다면 descending
#둘다 아니라면 mixed
arr = list(map(int, input().split())) #들어오는 값

up = [1,2,3,4,5,6,7,8]
down = [8,7,6,5,4,3,2,1]

result = 'mixed'
if arr == up:
    result = 'ascending'
elif arr == down:
    result = 'descending'
print(result)



'''
문제를 처음에 잘 못 이해함

#총 8개의 음으로 구성
#주어진 알파벳과 숫자 변환
#1부터 8까지 차례대로 연주된다면 ascending
#8부터 1까지 차례대로 연주된다면 descending
#둘다 아니라면 mixed

dajangjo = {1:'c', 2:'d', 3:'e', 4:'f', 5:'g', 6:'a', 7:'b', 8:'C'}
arr = list(map(int, input().split())) #들어오는 값
#1 2 3 4 5 6 7 8

result = [] #결과 값을 담을 list
for a in arr: #arr을 순회하면서 dajangjo에 있는 내용으로 변환
    result.append(dajangjo.get(a)) #변환한 내용을 result에 담음

print(result)
'''