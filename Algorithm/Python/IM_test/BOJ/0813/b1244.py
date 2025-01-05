import sys
sys.stdin = open('input1244.txt')
N = int(input())
switch = list(map(int, input().split()))
#print(switch)
student = int(input()) #학생수
for _ in range(student): #학생수
    sex, have_switch = map(int, input().split())
    #print(sex, have_switch)
    if sex == 1: #성별이 1일 경우
        idx = 1
        while have_switch * idx <= len(switch):
            result = have_switch * idx #3 --> 3이 들어있는 switch는 2번 idx다
            if switch[result-1] == 0: #3번은 -> 2번쨰 idx이다 이걸 주의
                switch[result-1] = 1
            else :
                switch[result-1] = 0
            idx += 1

print(switch)