#피보나치

#재귀 이용
def fibo(n):
    if n == 1 or n == 2:
        return 1 #1이 나올 것
    else :
        return fibo(n-2) + fibo(n-1)


#메모이제이션 이용
memo = {1 : 1, 2 : 1} #2와 1 모두 1을 도출
def memo_fibo(n):
    if n in memo:
        return memo[n] #key 값이 n인 value 값 전달
    else :
        #원래 return으로 바로 전달되어야할 것 output에 넣음
        output = fibo(n-2) + fibo(n-1)
        memo[n] = output
        return output

print(fibo(6))
print(memo_fibo(6))
