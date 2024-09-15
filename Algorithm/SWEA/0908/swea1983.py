import sys

sys.stdin = open('input1983.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    grade = {1 : 'A+', 2: 'A0', 3:'A-', 4:'B+', 5:'B0', 6:'B-', 7:'C+', 8:'C0', 9:'C-', 10:'D0'}

    N, K = map(int,input().split()) #총학생수, 찾는 학생 번호 -> 학생 번호는 1부터 시작한다. -> idx번호 유의
    score = [] #학점 -> 일단 넣고
    student = [] #student idx번호
    for i in range(1, N+1):
        g, k, a = map(int, input().split()) #중간 / 기말 / 과제
        total = g*0.35 + k*0.45 + a*0.2
        score.append(total)
        student.append(i)
    #print(score)
    #print(student)
    #순서대로 정렬하기 -> 학점을 기준으로
    for i in range(N-1):
        max_idx = i
        for j in range(i+1, N):
            if score[max_idx] < score[j]:
                max_idx = j
        score[max_idx], score[i] = score[i], score[max_idx]
        student[max_idx], student[i] = student[i], student[max_idx]
    #print(score)
    #정렬이 되었음 이제 학생수만큼 나눠서 접근하면 됨 -> 딕셔너리로 학점 접근 -> 비율만큼
    target = N // 10  # 8명 -> 0부터 8까지 -> 8부터 16까지
    for i in range(1, 11): #10명씩나눠짐 -> 80명이면 8번 돌 것
        target_grade = grade.get(i)
        for j in range(target*(i-1), target*i):
            score[j] = target_grade
    for i in range(N):
        if student[i] == K:
            print(f'#{tc} {score[i]}') #무엇을 구하는지 잘보기
            break
    # print(score)
    # print(student)


