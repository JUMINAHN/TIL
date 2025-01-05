N = int(input())

#글로 써보고 놓친 것이 있는지 다시 확인 후 작성
count = 0
while N >= 0:
    if N % 5 >= 3 : #왜 여기서 --> 이 조건이 문제야...!!!!!!!!!
        count += (N//5)
        if N % 3 == 0:
            pass #while문 종료되는 것 아닌지.. 그래서 패스로
        else :
            N %= 5 #3번돌고


    if N % 3 == 0: #바로 다음으로 -> 내가 가진 값을 기반으로
        count += (N//3)
        N %= 3
        break
    else:
        break
if N == 0:
    print(count)
else :
    print(-1)

#이번에 9랑 11이 틀렸어,,,