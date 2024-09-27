#회문 == 팰린드롬
#무의미한 0은 올 수 없음
#입력 마지막 줄은 0이 주어지며 이 줄은 문제에 포함되지 않음
#반복횟수?
#while로 계속해서 받고 0이 주어지면 끝

arr = []
flag = True
while flag:
    data = input()
    if data == '0':
        flag = False
        break #while문 종료
    arr.append(data) #아마 list input때문에 되지 않았던 것 같음
#print(arr) #해당 부분 맞게 들어가는 것으로 확인됨

#arr하나씩 돌면서 회문인지 확인
#arr자체가 회문
for a in arr: #a하나를 나눠서 진행
    data = []
    for small_a in a: #a 하나씩돈다 121
        data.append(small_a) #list 타입으로 바꾼다.
    if data == data[::-1] :#뒤집은게 같다면
        print('yes')
    else :
        print('no')


'''
하기처럼 작성해도 무한루프
arr = []
flag = True
while flag:
    if input() == '0':
        flag = False
        break #while문 종료
    arr.append([input()])
print(arr)

하기 처럼 작성할 경우 무한루프에 늪임
arr = []
while input() != '0': #0이면 들어가지 않음
    arr.append([input()]) #무한 루프가 걸린다.
print(arr)

하기처럼 작성할 경우 반복 횟수를 알 수 없음 
# arr = [input() for _ in range ]
# arr.pop() #맨마지막 데이터 뺴기
'''
