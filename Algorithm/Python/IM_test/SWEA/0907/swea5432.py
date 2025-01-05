import sys
#이건 사실 문제 이해가 100할임
sys.stdin = open('input5432.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    stick = list(input()) #쇠막대기 자체가 들어옴
    #print(stick)
    stack = []
    cut = 0
    for i in range(len(stick)):
        if stick[i] == '(': #안에 넣는다.
            stack.append(stick[i])
        else : # ')'를 만나면
            if stick[i-1] == '(': #이거면
                stack.pop() #안에있는것 없애주고
                cut += len(stack) #스택에 들어있는것 만큼 더해준다.
            else : #아니라면 그냥 +1만큼 더해준다
                stack.pop() #그래도 pop해준다.
                cut += 1
    print(f'#{tc} {cut}')
