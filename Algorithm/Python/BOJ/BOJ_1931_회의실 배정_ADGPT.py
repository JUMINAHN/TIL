def maxMeetings(meetings): #여러개의 회의를 나타내는 리스트 => 리스트 내부에 리스트가 있음
    # 종료 시간, 시작 시간 기준으로 정렬
    # list중 하나 => 즉 각각의 list 하나를 뽑고
    meetings.sort(key=lambda x: (x[1], x[0])) #그 list의 x1, x2를 적절하게 배분
    #sort() 함수는 기본적으로 리스트의 요소를 튜플로 해석하여 첫 번째 요소부터 정렬
    #종료 시간(x[1])과 시작 시간(x)을 기준으로 정렬
    #정렬된 회의를 순회하며 겹치지 않는 최대 개수의 회의를 선택
    #위 코드에서 lambda x: (x[1], x)는 각 회의의 종료 시간과 시작 시간을 기준으로 정렬하기 위해 사용

    count = 0
    last_end_time = 0

    #단순한 일차 for 문만으로 문제를 해결할 수 있는 이유는 문제의 성격이 단계별로 접근하여 해결할 수 있기 때
    #이 과정은 순차적으로 이루어지며, 이전 상태(마지막 종료 시간)만을 기억하면 되기 때문에 단일 for 문으로 충분
    for start, end in meetings:
        if start >= last_end_time: # 현재 회의가 이전에 선택된 회의와 겹치지 않는지를
            #12시에 시작했는데 이전이 13시이면 안되니까
            count += 1
            last_end_time = end #시작과 끝 날짜 재설정
    return count


# 입력 처리
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)] #meeting
#[[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''

# 최대 회의 수 계산
result = maxMeetings(meetings)
print(result)

