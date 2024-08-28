N = int(input()) #회의 진행 개수
schedule = [] #튜플 형식으로 담을 시작 시간과 종료 시간
for _ in range(N): #회의실 개수 만큼
    s, e = map(int, input().split())
    schedule.append((e,s)) #최적 시간을 찾기 위해 종료 시간 먼저 선 배치
print(schedule)

#종료시간을 기준으로 순서를 확인하기 위해 정렬 : 종료시간이 빠른 것 먼저 확인하기 위해서 정렬
for i in range(N-1):
    min_idx = i
    for j in range(i+1, N):
        if schedule[min_idx] > schedule[i]:
            min_idx = i
    schedule[min_idx], schedule[i] = schedule[i], schedule[min_idx]
print(schedule)

meeting_count = 0 #meeting이 몇 번 진행되는지 카운트
end_time = 0 #끝나는 시간_초기 setting
#0으로 설정하고, 첫번째 start값이 담기며 다음 end와 비교할 수 있도록 장치 설정
#내가 원하는 의도로 구현할 수 있도록 만드는 장치
for e, s in schedule: #end와 start
    if s >= end_time:
        end_time = e #end_time에 e를 넣는다.
        meeting_count += 1
print(meeting_count)