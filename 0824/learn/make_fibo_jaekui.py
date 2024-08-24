# #피보나치 수열 구하기
# #재귀함수
def fibo(n):
    if n == 1 or n == 2: #n에 1이나 2를 넣었을 떄 0이 되기 떄문
        return 1
    else :
        return fibo(n-2) + fibo(n-1)


print(fibo(6)) #8

#메모이제이션으로 접근해보기
#피보나치 재귀 첫번째 조건을 활용해서 메모에 담음
memo = {1:1, 2:1} #둘다 값이 1임을 활용용
def fibo(n):
    if n in memo: #n이 메모에 있는가? dictionary 값에 있는가?
        return memo[n] #키 값이 있다면 memo[n]을 돌려준다.
    else :
        output = fibo(n-1) + fibo(n-2) #재귀 호출
        #한번 계산한 값을 메모에 넣어준다.
        memo[n] = output
        return output

print(fibo(6))