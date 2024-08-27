N = int(input()) #100 input 됨
max_len = 0
total = []

for i in range(N, 0, -1): #일단 뒤에서부터 접근 -> 99로 고정해놓음 #똑같은게 나올 수 있음 (양의 정수중에서니까)
    #1차로 진행
    data = [N]
    data.append(i)
    #data에 0이 들어갈때 까지 그게아니면, data[-2] - data[-1]이 음수가 되기 전 까지
    while (data[-2]-data[-1]) >= 0:
        result = data[-2] - data[-1]
        data.append(result)
    #음수가 되기전에 끝날 것
    if max_len < len(data):
        max_len = len(data)
        total = data #append 없이 그냥 list 값을 대입해도 된다.
print(max_len)
print(*total)