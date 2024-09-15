#6시 42분 6시 58분
import sys

sys.stdin = open('input1983.txt')
#테스트 케이스 개수
#9시50분~10시25분
T = int(input())
for tc in range(1, T+1):
    #N명의 학생, 동일한 평점 K번쨰 학생의 번호
    N, K = map(int, input().split())
    score = []
    student_idx = []
    #학점 변환
    grade = {0:'A+', 1:'A0', 2:'A-', 3:'B+', 4:'B0', 5:'B-', 6:'C+', 7:'C0', 8:'C-', 9:'D0'}

    #1. input받은 값들을 가중치를 기반으로 계산하고 저장한다
        #저장은 두가지로 한다. -> 학생 idx를 담을 배열과, score의 합산을 다을 배열로 저장한다.
    for i in range(N):
        middle, last, assignment = map(int, input().split())
        sum = 0
        sum = (middle * 0.35) + (last * 0.45) + (assignment * 0.2)
        score.append(sum)
        student_idx.append(i+1)
    #2. scroe로 합산한 배열을 sort하는데 오름차순이 아닌 내림차순의 기준으로 sort를 진행한다.
        #단 학생 idx도 같이 솔트를 해야하는데, 이는 score기준으로 솔트되는 것과 동일하다. 따라서 단순히 sort()메서드를 사용하면 위험할 수 있음
    #print(score)
    #선택정렬을 하고 reverse를 한다면? -> 선택 정렬을 거꿀로
    for i in range(N-1):
        max_idx = i
        for j in range(i+1, N):
            if score[max_idx] < score[j]:
                max_idx = j
        score[max_idx], score[i] = score[i], score[max_idx]
        student_idx[max_idx], student_idx[i] = student_idx[i], student_idx[max_idx]
    #print(score)
    #print(student_idx)
    #4. 해당 값은 dictionary를 통해서 해당하는 i에 걸맞은 data를 get으로 가져와서 변환을 한다
    #3. 계산한 값을 sort하고 현재 학생 수 N을 기반으로 10을 나눈다.
        #80명의 경우 8명까지가 A+학점을 취득할 수 있기 떄문에 -> N // 10 을 한 것에 대해서 작업을 진행해야 한다.
        #N // 10 = achieve (8)
        #따라서 10만큼 순회를 돌리되, 범위를 arr[0*i:achivev*i] #이런식으로 계속 값이 바뀌게 한다
    for i in range(10): #10을 기준으로 돌리면 0:8, 8:16, 16:... 72:80
        select = N // 10 #80명 중에 -> 8명 -> line 1번
        #score[i*select:(2*i*select)+1]
        for j in range(i*select, (i*select)+select):
            score[j] = grade.get(i)
    #맞게 값이 들어갔고
    #print(score)
        # student = score[i:(N//10)*i+1] #0부터 8까지 생각
        # print(student) #덩어리로 나오지 않는다
        # data = grade.get(i)
        # for j in score[i:(N//10)*i+1]:
        #     score[i] = data #원하는대로 들어갔는데..
        #print(data) data를 그 값에 삽입
        # for i in range(len(student)): #student 정보
        #     student[i] = data #값을 전달
    #5. 최종적으로 원하는 값을 찾기 위해서 찾는 K의 idx의 학점을 변환해서 전달한다.
    #지금 idx의 위치를 찾아라
    result = 0
    for i in range(N):
        if student_idx[i] == K: #지금뽑힌 idx의 -> d위에서 +1을 해줌
            result = score[i]
    print(f'#{tc} {result}')
