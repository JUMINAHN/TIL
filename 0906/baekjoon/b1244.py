import sys
sys.stdin = open('input1244.txt')

#스위치를 킬 함수
def on_off(data):
    if data == 1:
        return 0
    else :
        return 1

#1. 스위치 개수
N = int(input())
#2. 스위치 상태 (1010 구성본)
#스위치 0은 건들지 않음
switch = [0] + list(map(int, input().split())) #스위치가 1부터시작하니까
#3. 학생 수
num = int(input())
#print(switch)
#print('---------')
#4. 학생 성별, 받은 스위치 번호
for _ in range(num): #num만큼 순회하고 -> 그 안에서 작업 진행
    gender, switch_num = map(int, input().split())
    #4-1. 만약 남자라면 받은 수의 배수만큼 스위치 변경
    if gender == 1:
        for i in range(switch_num, len(switch), switch_num):
        # for i in range(0, len(switch)//gender):
        #     for j in range(i, len(switch), switch_num-1): #배수만큼 스위치 키기
        #         if j == 0:
        #             continue
            #print(i) #index
            switch[i] = on_off(switch[i]) #바꾼 값을 다시 돌려줄 것이기 때문
        #print(switch)
    #for i in range(1,N)
        #for j in range(i, N, input받은 배수)
            # x = 스위치 변경 함수 대입
    else : #gender가 2라면?
        #swich_num만큼 view에서 사용한 것
        #len switch만큼 하면 범위를 벗어나기 떄문에 그 전에 idex 초과하면 못하도록 break
        #max_len = 1 #이제 제일 작은것도 1로 포함
        first_idx = switch_num
        lax_idx = switch_num
        i = 1
        # while True:
        #     # 범위 체크
        #     if switch_num - i < 1 or switch_num + i >= len(switch):
        #         break
        #
        #     if switch[switch_num - i] == switch[switch_num + i]:
        #         first_idx = switch_num - i
        #         lax_idx = switch_num + i
        #     else:
        #         break
        #
        #     i += 1

        for i in range(1, len(switch)): #범위를 벗어나지 않게 하기 위해서
            if 1<=switch_num-i and switch_num+i < len(switch): #0번부터 시작하기 떄문 #+1까지 안함
                #굳이 슬라이싱 할필요가 없음 그냥 양 옆에 대조하면 됨
                # data = switch[switch_num - i:switch_num + i + 1]
                if switch[switch_num - i] == switch[switch_num + i]:
                    # inner_len = len(switch[switch_num - i:switch_num + i + 1])
                    # if max_len < inner_len:
                    #     max_len = inner_len
                    #max_len += 2 #양 옆의 길이 추가
                    first_idx = switch_num - i
                    lax_idx = switch_num + i
                    #대칭 구간탐색
                else : #아니면 이제 빠져나가기
                    break
            else : #애초에 조건이 성립되지 않으면
                break #break
            #if switch[switch_num-i:switch_num+i+1] #+1을 하면 slicing으로 짤림
    #4-2. 여자라면 받은 수를 기점으로 반을 나눔
        #회문처럼 가운데기점으로 상태가 똑같을 때, 회문 max_len의 길이만큼 돈다
            #for i in range(1,maxlen))
        #맞아요! 슬라이싱을 사용하는 경우와 인덱스 비교를 사용하는 경우가 다릅니다. 여기서는 슬라이싱이 아니라 인덱스 번호만 비교하기 때문에, i + 1을 하지 않아도 됩니다.
                #x = 스위치 변경 함수 대입
        for i in range(first_idx, lax_idx+1):
           switch[i] = on_off(switch[i])
    #     for s in select_list:
    #         s = on_off(s)


switch.pop(0)
for i in range(len(switch)):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
#print(*switch)