#A B C에 시간 조절용 버튼이 달려있음
#5분, 1분, 10초
#냉동음식마다 전자레인지로 요리해야할 시간 T가 초단위로 표시되어 있다
#ABC의 버튼을 적절히눌러서 그 시간의 합이 T가 되도록 해야함
#ABC의 버튼을 최소 -> 큰거부터
#시간을 정확하게 맞출 수 없는 경우도 있다.
#T초를 맞추기 위한 최소 조작 버튼을 구하는 프로그램 작성
#ABC 횟수를 첫줄에 출력
#해당버튼을 누르지 않는경우 ㅅ숫자 0, 3개의 버튼으로 맞출 수 없으면 -1 출력
T = int(input())
A = 5 * 60 #초로 변환
B = 1 * 60 #초로 변환
C = 10 #초

timer = [A,B,C]
a=b=c= 0 #count할 친구들
check = [a,b,c] #check할 것
for i in range(3):
    check[i] += (T // timer[i])
    #print(check[i]) #맞게 들어갔는데..?
    T = T % timer[i]
if T == 0:
    for c in check:
        print(c, end= " ")
else :
    print(-1)


# #T의 최소버튼
# if T // A != 0 :
#     a += (T // A)
#     T = (T % A)
# if T // B != 0 :
#     b += (T // B)
#     T = (T % B)
# if T // C != 0 :
#     c += (T // C)
#     T = (T % C)
# if T == 0:
#     print(a, b, c)
# else :
#     print(-1)