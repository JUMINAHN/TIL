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
    for d in data:
        #숫자면 그냥 출력하고
        if d.isdigit():
            print(d,end="")
        #만약 숫자가 아니라면? -> 일단 괄호가 없다고 가정해서
        else:
            #연산 우선자일경우 그냥 stack에 push 한다.
            if d == '*' or '/':
                #근데 이전에 혹시 *, /이 있을경우 그건 pop한다.
                stack.append(d)
            elif d == '+' or '-':
                #stack에 있는 것들 pop해준다. ->
                stack.pop()
