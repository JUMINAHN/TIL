import sys
sys.stdin = open('input2605.txt')

N = int(input()) #학생수
select_num = list(map(int, input().split())) #줄을 선 순서만큼 앞에 가서 선다.

#IndexError: list index out of range
stand_line = [] #줄을 선 순서를 담을 것
for i in range(N): #학생수
    stand_line.insert(len(stand_line) - select_num[i], i+1) #idx번호에 데이터
    #나의 앞에 길이가 바뀔떄마다 변동
#stand_line = stand_line[::-1]
#출력값 문제
print(*stand_line)