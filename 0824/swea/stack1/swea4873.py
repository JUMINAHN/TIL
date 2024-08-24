import sys

sys.stdin = open('input4873.txt')
#테스트 케이스 개수
# 모두 다 진행해도 스택이 차있을 떄 : 뺴려는 값이 없기 떄문에 현재 남은 길이 출력 -> 해당 값은 괄호와 다르기 떄문에 고려x
# 받은 str을 기반으로 for문을 사용해서 유무를 확인한다.
def find_length(str):
    stack = []     #남은 문자열이 없으면 0을 출력한다. -> 그냥 stack이 0인 것
    for s in str:
        if stack: #stack에 값이 있다고 가정했을 때
            #stack의 마지막 값이 같은지 확인해야 함
            if s == stack[-1] : #peek
                #같을경우 마지막 글자와 현재 pop
                stack.pop() #현재 값도 들어갈필요가 없음
            else :
                stack.append(s) #그게 아니면 그냥 넣어도 됨
        else : #stack이 비어있을 경우는 append -> 1번째 값
            stack.append(s)
    return len(stack)

T = int(input())
for tc in range(1, T+1):
    #문자열 s에서 반복된 문자를 지우려고 한다.
    #또 반복되는 문자가 생기면 다시 지운다.
    #남은 문자열이 없을경우 0을 출력한다.
    str = input() #ABCCB자체를 가지고 이제 돌린다.
    result = find_length(str)
    print(f'#{tc} {result}')