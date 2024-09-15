import sys

#2번째 스택을 사용할 필요가 없다
#숫자를 stack에 넣을 필욘 없고, 연산자만 우선적으로 stack에 넣는것만 하면 된다.
sys.stdin = open('input18389.txt')

#Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1): #1
    data = list(map(str, input())) #2+3*4/5
    stack = [] #상기 데이터를 스택에 담을것임
    for i in range(len(data)):
        #숫자면 그냥 출력하고
        if data[i].isdigit():
            print(data[i],end="") # 먼저 출력
        else:
            if stack:
                # 입력하는 데이터가 연산 우선자일경우 그냥 stack에 push 한다.
                if data[i] == '*' or data[i] == '/':
                    # 근데 이전에 혹시 *, /이 있을경우 그건 pop한다.
                    if stack[-1] == '*' or stack[-1] == '/':
                        print(stack.pop(), end="")  # 이전 것을 pop 이전것을 뺄것
                    else:
                        stack.append(data[i])
                elif stack[-1] == '+' or stack[-1] == '-':
                    # +을 -을 하려고하는데
                    if stack[-1] == '*' or stack[-1] == '/':
                        # stack에 있는 것들이 *, /라면 pop해준다. ->
                        print(stack.pop(), end="")
                    else:
                        stack.append(data[i])
                else:
                    print(stack.pop(), end="")
                # 스택에 아무것도 없을 경우도 존재함
            else:  # stack에 아무것도 없을 경우
                stack.append(data[i])


