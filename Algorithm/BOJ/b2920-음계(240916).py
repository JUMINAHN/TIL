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
#1 2 3 4 5 6 7 8

#배열 list가 증가하는지, 감소하는지 확인할 것
result = "ascending"
now = arr[1]
prev = arr[0]
for i in range(1, len(arr)): #해당 값이 증가하는지 감소하는지 확인
    prev = arr[i-1]
    now = arr[i]
    if now == prev + 1 : #now가 prev보다 1 더 크다면
        continue #ascending으로 계속하고
    else : #아니라면?
        if i == 0:
            continue #0일때는 넘겨
        #감소하는지 아닌지 확인할 것
        #따라서 주기적으로 감소한다면 descending
        if now == prev - 1:
            result = "descending"
            break #for 구문 빠져나가기
        #아니라면 mixed
        else :
            result = "mixed"
            break
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