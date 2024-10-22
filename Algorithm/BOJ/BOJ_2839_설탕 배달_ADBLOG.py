sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)

'-----------------------------------------'

#A : 5의 배수로 나눠지고 -> 3의을 나누고 -> 그럼에도 나머지가 0인지 확인
#B : 3의 배수로 나누고 -> 5의 배수로 나누고 -> 그럼에도 나머지가 0인지 확인
#그리고 A와 B 모두 나머지가 있다면 ==> 그것은 애초에 돌아가지 않는 코드
N = int(input()) #5를 계산할 N
M = N #N의 값을 그대로 복사한다  => 3을 계산할 M

five = 5
three = 3

first_five = first_three = 0 #first를 five로 넣었을때 frist를 three로 넣었을 때

#first_five
first_five += (N//five) #1
N %= five # five의 나머지  ==> 나머지 1이 됨됨first_five += (N//three)
N %= three
#N의 나머지 유무 ==> 여기는 1이되고

#first_three
first_three += (M//three) #2가되고
M %= three #나머지가 0인인first_three += (M//five)
M %= five

if N == 1 and M == 1:
    print(-1)
#만약 여기서 나머지가 1인게 있으면 ?? == 이케이스가 안되는 것임
#나머지도 없는지 확인을 해야
#나누어 떨어진 케이스를 비교해야하고 -> 그 이후에 대소비교를 해야하는데 // 나누어 떨어진 케이스를 비교하지 않음
elif N == 0 : #5로 나누었을 떄 떨어진다면?
    #여기가 정답
    print(first_five)
elif M == 0: #3으로 나누었을 떄
    print(first_three)