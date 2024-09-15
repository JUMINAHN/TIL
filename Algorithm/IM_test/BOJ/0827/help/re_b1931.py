N = int(input()) #사용할 최대 회의실 개수
schedule = []
for _ in range(N):
    s, e = map(int, input().split())
    schedule.append((e,s)) #회의의 최대 개수를 구하기 위해서, 최적의 개수를 구하기 위해 뒤에서 부터 접근

schedule.sort() #sort해서 정렬하고
#지금 스캐쥴
meeting_count = 0
end_time = 0 #일단 end_time은 유동적으로 바뀌기 떄문에 초기값으로 0설정


for e, s in schedule: #schedule에 들어있는 e,s하나씩 출력 -> 하나에 대한게 e, s로 나눠지는 것
    if s >= end_time: #start가 end보다 크거나 같다면
        end_time = e
        meeting_count += 1
print(meeting_count)
