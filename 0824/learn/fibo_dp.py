#피보나치 메모이제이션
memo = {1:1, 2:1}
def fibo_m(n):
    if n in memo:
        return memo[n] #n이 들어가있는 것을 돌려줘
    else :
        output = fibo_m(n-1) + fibo_m(n-2)
        #재귀 호출을 끝나고 결과를 얻은 후에 그 값을 저장함
        #필요한 값만 계산함
        memo[n] = output #없으면 그 값을 저장해줘
        return output
print(fibo_m(6))


#dp
#반복적으로 작은문제에서 큰 문제로 올라감
def fibo_dp(n):
    dp = {1:1, 2:1} #단 여기는 내부에서 초기화
    if n in dp:
        return dp[n] #여기까진 메모이제이션과 동일, 있는 값을 반환해줌

    for i in range(3, n+1):
        if i in dp: #dp에 있다면
            continue
        else :
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(fibo_dp(6))