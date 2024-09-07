import sys
sys.stdin = open('input2635.txt')

N = int(input())
#Flag = True
max_len = 0
result = 0
#100부터 만드는 것을 까먹고 N-1을 했다.
#경우의 수와 동일
for i in range(N, -1, -1): #양의 정수기 떄문에 100부터 0까지 뒤에서부터 많은 수를 얻기위해 접근 -> '두번쨰는' 양의 정수중 선택
    data = [N]  # N이 들어있는 데이터를 만들어준다.
    data.append(i)
    #print(data)
        #여기서 data = [100,99]가 있을 것
        #이거에 대해서 빼줘
        #여기에 대한 내용이 반복이 되어야 함
    while data[-2] - data[-1] >= 0: #0밑으로 내려가면 종료 0도 들어가는데,,
        #if data[-2] - data[-1] >= 0:
        # if data[-2] - data[-1] >=0:
        data.append(data[-2] - data[-1]) #오탈자 확인할 것
        #print(data)
    #print(data)
    if max_len <= len(data):
        max_len = len(data)
        result = data
print(max_len)
print(*result)