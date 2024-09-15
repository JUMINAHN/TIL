#참가하는 수, 최대 인원 수
N, K = map(int, input().split())
#성별S(여0/남1), 학년Y
student = []
for _ in range(N):
    student.append(list(map(int, input().split())))
print(student)

count = [0] * 7
for s in student:
    count[s[1]] += 1
#print(count)





# student = {}
# for _ in range(N):
#     S, Y = map(int, input().split())
#     new_dict = {Y:S}
#     student.update(new_dict)
#     # dictionary로 담으면 키 중복값이 없어짐 --> 키 중복이 없어짐
# print(student)









# student = [] #학생 정보들 가득함 --> 2번째 idx가 학년
# for _ in range(N):
#     SY = list(map(int, input().split()))
#     student.append(SY)
#
# year = [0] * 7 #1~6학년 -> 0은 사용x
# man_year = [0] * 7
# woman_year = [0] * 7
# for s in student:
#     year[s[1]] += 1
# print(year) #-> 학년 카테고리됨
#
# #성별 방배정