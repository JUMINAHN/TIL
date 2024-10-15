#visited를 사용할필요 없다는 것만 감으로 잡음

#중복되는 값 가능한데 -> 딱 그까지만
N, M = map(int, input().split())
result = []
#visited = [False] * (N+1) == 이거할필요가 없지 않음?

def recur(num, start): #retu X -> if절 출력만
    if num == M:
        print(" ".join(map(str, result)))
        return #빠져나오기 -> break 같이

    for i in range(start, N+1): #N까지 증가
        result.append(i)
        recur(num+1, i) #이게 증가하지 않음? => i자체가  == 변동되는 값 = 이 왜 진?
        result.pop()

recur(0,1)