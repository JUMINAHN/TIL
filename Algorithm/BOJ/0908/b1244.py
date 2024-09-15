import sys
sys.stdin = open('input1244.txt')

def onoff(data):
    if data == 1:
        return 0
    elif data == 0:
        return 1

N = int(input()) #스위치 개수
switch = [0] + list(map(int ,input().split()))
S = len(switch) #내가 구해야할 길이 기준!
student = int(input())

for _ in range(student): #학생수만큼
    gender, switch_num = map(int, input().split())
    if gender == 1: #남자라면
        for i in range(switch_num, S, switch_num):
            switch[i] = onoff(switch[i])  #스위치를 배수만큼 바꿔준다.
            #print(i)
    elif gender == 2: #여자라면
        #max_len = 1 #일단 나 자신은 기본으로 들어있기 떄문에
        start_idx = switch_num
        end_idx = switch_num #대칭이 발생하지 않을경우 오류 발생
        i = 1
        #유동적으로 언제까지 대칭인지 모르면 while이 더 적합하다/..
        while switch_num - i >= 1 and switch_num + i < S and switch[switch_num - i] == switch[switch_num + i]:
            start_idx = switch_num - i
            end_idx = switch_num + i
            i += 1
        #적절한 범위를 설정하지 않으면, 대칭 범위를 제대로 확인하지 못할 수 있습니다.
        # for i in range(1, N): #범위를 초과할 수도 있음 해당 부분 유의 --> 이 범위가 잘못됨 루프를 돌면서 바뀜
        #     # 현재 i를 구하고, 그것을 기준으로 prev, after로 변수를 나눈다.
        #     # prev = i-1, after = i+1 -> 범위는 S까지 해주긴 해야해 끝 길이니까 그런데 0이 문제임
        #     if (1<= switch_num-i) and (switch_num+i < S):
        #         if switch[switch_num-i] == switch[switch_num+i]: #오탈자 잘보기 -> 실제로는 0과 S가 포함되지 않기 떄문에
        #             #max_len += 2 #대칭이니까 1개 증가
        #             start_idx = switch_num - i
        #             end_idx = switch_num + i #slicing한건 아니잖아 그래서 idx가 맞게 들어갔을텐데
        #     else :
        #         break
        for i in range(start_idx, end_idx+1): #end_id까지 포함이기 떄문에
            switch[i] = onoff(switch[i])

#switch.pop(0)
for i in range(1, N + 1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()  # 20개마다 줄바꿈
if N % 20 != 0:
    print()

'''
#1. 스위치는 1번부터 N번까지 켜진다 -> idx주의
	#idx는 0부터 시작하기 떄문에 list에 새로운 input받은 것을 더해준다.
	#단, 마지막에 스위치를 나타낼때는 pop(0)을 해서 스위치 개수를 맞추어 준다.
#2. 남자는 자기가 받은 스위치 번호의 배수인 스위치를 바꾼다 
	#자기가 받은 스위치의 idx를 기준으로 배수 만큼 스위치를 바꾼다
	#range(3,N,3) -> 3부터 시작하고 끝까지니까, 3의 배수만큼 증가 하는 수
#3. 여자는 자기가 받은 수를 기점으로, 대칭된 구간이 가장 많은 만큼의 스위치를 바꾼다.
	#대칭을 구한다 -> 돌 뒤집기 or 회문 스타일로
	#현재 i를 구하고, 그것을 기준으로 prev, after로 변수를 나눈다.
		#prev = i-1, after = i+1
		#따라서 prev == after이면 대칭의 길이 += 2를 획득
			#만약 아니라면 나를 포함한 현재 길이만큼 스위치를 바꿔준다.
'''