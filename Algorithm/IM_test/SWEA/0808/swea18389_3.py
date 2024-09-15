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
        if data[i].isdigit(): #숫자면 그냥 출력
            print(data[i], end="")
        else:
            if stack:
                if data[i] == '+' or data[i] == '-': #
                    if stack[-1] == '+' or stack[-1] == '-':
                        print(data[i], end = "")
                    elif stack[-1] == '*' or stack[-1] == '/':
                        print(stack.pop(), end = "")
                    else: #*랑 /일 때
                        stack.append(data[i])

                elif data[i] == '*' or data[i] == '/':
                    if stack[-1] == '*' or stack[-1] == '/':
                        print(data[i], end="")
                        stack.append(data[i])
                    else:
                        stack.append(data[i])

            else:
                stack.append(data[i]) #+가 들어가요

