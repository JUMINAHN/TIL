
#주석이 없는 코드

data = input()
split_data = data.split('-')

for i in range(len(split_data)):
    split_data[i] = split_data[i].split('+')
for i in range(len(split_data)):
    sum_data = 0
    for j in split_data[i]:
        sum_data += int(j)
    split_data[i] = sum_data
result = 0
for i in range(len(split_data)):
    if i == 0:
        result += split_data[i]
    else :
        result -= split_data[i]
print(result)


'-------------------------------------------------------------------'
#주석과 함께 작성한 코드

#괄호
#연속해서 두 개이 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다.
#55-50+40의 경우 - 의 뒤에 있는 것을 묶어주면 좋다 == idea 전달받음
#즉 -를 기준으로 앞, 뒤를 나눠준다.
data = input() #55-50+40 => 하나의 string type
#split_data = [] #일단 - 기준으로 담을 내용
split_data = data.split('-') #기준으로 나눈다 ==> []를  #55-50+40
#print(split_data) # - 기준으로 나뉘어지는 것을 확인할 수 있음
#[55, '50+40']
#이 list들을 합쳐서 계산해야 함 -> HOW? -를 해서
#단, 그전에 내부에 + 값이 있다면 그것을 계산해줘야 함
#split_data의 [0], split_data의 [1]씩 접근해야 함
# for sp in split_data: #여기서 각 한개씩 나올 것이고 => 거기서 또 루프 50
#     sp = sp.split('+') #또 +기준으로 나뉘어짐
# print(split_data)
for i in range(len(split_data)): #list개수
#    for j in split_data[i]: #이게 5, 0, + , ..이 됨
    split_data[i] = split_data[i].split('+') #+도 스플릿해준다.
#그리고 그것을 더해준다.
for i in range(len(split_data)):
    sum_data = 0
    for j in split_data[i]: #50, 40
        sum_data += int(j) #int로 변환
    #그대로 넣어준다.
    split_data[i] = sum_data
#print(split_data) #원하는 결과값이 나옴
result = 0 #첫번째 값
for i in range(len(split_data)):
    if i == 0:
        result += split_data[i] #초기값 설정 ==> 따라서 더해주고
    #그게 아니면
    else : #빼준다
        result -= split_data[i]
print(result)

'---------------------------------------------------'
#핵심은 괄호를 어떻게 나눌 것인가에 대한 아이데이션이 필요