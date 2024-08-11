import sys
sys.stdin = open("input1330.txt")

N, K = map(int, input().split())
student = []
for _ in range(N):
    SY = list(map(int, input().split()))
    student.append(SY)
#student 배열 만들어짐
#print(student)]

# 학년별로 남학생과 여학생 수를 저장할 2차원 배열
count = [[] for _ in range(7)]
for s in student:
    gender = s[0]
    year = s[1]
    count[year].append(gender)
print(count)