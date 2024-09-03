import sys

sys.stdin = open('input5432.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #1.data = 쇠막대기 list로 input받기
    data = list(input()) #split되어 들어갈 친구들
    # 4. total은 쇠막대기를 자를 것을 담을 변수
    total = 0
    #3. 쇠막대기를 담을 stack박스 만들기
    stack = [] #쇠막대기를 담을 stack박스
    #2. for d in data: 즉 data를 통해서 쇠막대기 순회하기
    for i in range(len(data)): #쇠막대기 개수만큼 돌기
        if data[i] == '(':
            stack.append(data[i])
        #2-1.만약 쇠막대기가 '('라면 stack에 append해준다.
        elif data[i] == ')':
        #2-2. 만약 연속된 쇠막대기가 ')'라면(레이저) stack에 pop을 해준다.
            #Q. 쇠막대기가 레이저인지, 쇠막대기인지 구분을 짓기 위해서..? ==> 지금 핵심은 쇠막대기인지 레인저인지 어떻게 구분을 하는 것일까..
                #-> 이전 idx와 비교를 해서? 이전 idx가 ')'일 경우 (즉 '('가 아닐 경우)) == idx를 접근해줘야겠네
        # 2-2-2. 쇠막대기가 레이저가 아닐 때 )가 들어오면 ')'의 개수만큼 +1을 해준다.
            if data[i-1] == ')': #이전 idx가 ')'일 경우
                #지금 ')'가 있으니 그만큼 +1을 해주자
                stack.pop()#그 값을 뺴주지 않았기 때문에 값을 빼줘야 함
                total += 1
            #2-2-1. 쇠막대기를 pop할때(레이저일떄) 만약 stack에 값이 있다면 len(stack)을 total해준다.
            else : #이전에 '('였다는 의미 즉 레이저라는 뜻
                stack.pop()
                total += len(stack) #stack에 있는 내용 만큼
    print(f'#{tc} {total}')
