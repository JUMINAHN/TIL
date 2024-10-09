'''
5
55 185
58 183
88 186
60 175
46 155
'''
N = int(input())
student = [list(map(int, input().split())) for _ in range(N)]
#print(student)

for standard in student: #기준으로
    rank = 1  # rank는 계속해서 갱신
    for compare in student: #비교대상
        if standard[0] < compare[0] and standard[1] < compare[1]:
            rank += 1
    print(rank, end= " ")