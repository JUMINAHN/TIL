def fibo(n):
    if n < 2 : #2보다 작을경우 -1이 될 수 있음
        return n
    else :
        return fibo(n-1) + fibo(n-2) #이 부분을 손 로직으로 그려보기