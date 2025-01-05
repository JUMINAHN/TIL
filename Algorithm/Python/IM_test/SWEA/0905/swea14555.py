import sys

sys.stdin = open('input14555.txt')

# Testcase 수
T = int(input()) #테스트 케이스 input
# Testcase 만큼 반복
for tc in range(1, T+1):
    #1.1차원 초원이 있고 그 위에 공이 있다. == 1차원 배열을 사용한다는 뜻 == 입력값자체
        #1-1. 서로 다른 공은  겹치지 않는다.
        #1-2. ...은 초원이다. 공 자체는 ()으로 표현이 된다.
    plant = list(input())
    #print(plant)
    #2. 공은 열린괄호와 닫힌 괄호가 붙어있다.
    #3. 그 사이 사이 잡초가 자라서 몇개의 칸이 가려진다.
    #4. 공의 개수의 최소값을 구해라 --> 일단 이까지 10분 소요 됨
    ball_count = 0
        #4-1.최소값을 구하기 위해선 그냥 (옆에 |하나만 구하면 된다.
    prev = '' #이전 data를 쉽게 저장하기 위해서 ..? idx 접근 말고 이렇게 해도 될듯
    for i in range(1,len(plant)): #i+1권법으로 일단 가보자
        prev = plant[i-1] #이전 데이터 값을 넣어준다.
        now = plant[i]
        # 4-1-1. ')'의 왼쪽에 '|'가 있다면, 즉 i-1이 |이고 i가 )이면 공이다. +1을 해준다.
        if prev == '|' and now == ')':
            ball_count += 1
        #4-1-2. '('의 오른쪽에 '|'가 있다면, 즉 i이 |이고 i-1가 (이면 공이다. +1을 해준다.
        elif prev =='(' and now == '|':
            ball_count += 1
        #4-2.그리고 ()자체 하나를 구하면 된다.
        elif prev == '(' and now == ')':
            ball_count += 1
            #4-2-1. ()가 붙어있는 것을 확인하려면 이전인덱스가 (인지 )인지 확인하면 된다.
            #즉 '('앞의 idx가 이거고 ')' 그 다음 idx가 저거면 그냥 +1을 해준다.
    print(f'#{tc} {ball_count}')