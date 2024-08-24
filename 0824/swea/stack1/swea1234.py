import sys

sys.stdin = open('input1234.txt')
#테스트 케이스 개수
T = 10

#pw 만들기
def mk_pw(data):
    stack = []
    # stack에 값이 있는가 없는가의 차이부터 시작
    for d in data:
        # 무작정 pop을 하는가? -> x, 바로 stack의 옆값과 같을 때
        # 그런데 해당 부분은 한 번 만 수행이 된다.
        if stack:  # stack이 있을때까지
            if stack[-1] == d:
                stack.pop()
            else:
                stack.append(d)
            # 그게 아니라면 append
        else:
            stack.append(d)
    return stack

for tc in range(1, T+1):
    N, data = map(str, input().split()) #10 , 1238099084가 될 것..
    result_stack = mk_pw(data)
    print(f'#{tc}', end = " ")
    for r in result_stack:
        print(r, end="")
    print()