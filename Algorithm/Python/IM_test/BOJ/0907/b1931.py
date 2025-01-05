#import sys
#sys.stdin = open('input1931.txt')

#한개의 회의실이 있는데 -> N개의 회의에 대한 회의실 사용표를 만드려고 한다.
#시작 시간과 끝나는 시간이 주어져 있고, 겹치지 않게 회의실을 사용할 수 있는 최대 개수를 찾아본다.
#한 회의가 끝나는 것과 동시에 다른 회의가 시작할 수 있다. -> 시작시간이 끝나는 시간으로 같을 수 있다.

#입력
#회의수 N
N = int(input())
#회의의 정보 시작~끝
start_time = []
end_time = []
for _ in range(N):
    s, e = map(int, input().split())
    start_time.append(s)
    end_time.append(e)
#끝나는 시간을 기준으로 정렬 -> 시작 부분
for i in range(N-1):
    max_i = i
    for j in range(i+1, N):
        if end_time[max_i] < end_time[j]:
            max_i = j
    end_time[max_i], end_time[i] = end_time[i], end_time[max_i]
    start_time[max_i], start_time[i] = start_time[i], start_time[max_i]
#모든 경우의 수 순회
#print(end_time)
#print(start_time)

use_room = 0
#제일 늦은 끝나는 시간 -> 그에 맞는 시작시간 -> 그 시작 시각과 동일한 끝나는 시간 or 제일 가까운 끝나는 시간
#다양한 경우 계산
s_idx = 0
e_idx = 0

flag = True
while flag:
    now_s = s_idx
    end_s = e_idx
    #print(start_time[s_idx])
    for i in range(N-1, -1, -1):
        if start_time[s_idx] <= end_time[i]:
            #print(end_time[i])
            s_idx = i
            e_idx = i
            break
    if now_s == s_idx:
        break
    use_room += 1
print(use_room)