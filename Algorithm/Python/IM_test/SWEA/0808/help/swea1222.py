import sys

sys.stdin = open('../input1222.txt')

T = 10
for tc in range(1, T+1):
    num_length = input()
    data = input()

    stack = []
    switch = []
    #후위연산자로 바꿔줍니다. -> 이건 플러스만 있음
    for d in data:
        if d.isdigit():
            switch.append(d)
        else: #숫자가 아니라면 -> 연산자라면
            if not stack:
                stack.append(d) #스택이 비어있는 처음
            else:
                while stack: #연산자인데 값이 있다면
                    switch.append(stack.pop()) #팝한 것을 스위치에 넣고
                stack.append(d) #없으면

        # 남아 있는 연산자를 switch에 추가 -> 여러개 있을 수 있으니까
    while stack:
        switch.append(stack.pop())
    #print(stack) #원하는 것처럼 비어있습니다.
    #print(switch) #원하는 것처럼 채워있습니다.


    #후위 연산자를 기반으로 계산을 하겠습니다.
    for s in switch:
        if s.isdigit():
            stack.append(int(s))
        else: #연산자라면
            #근데 2이상 이어야 가능하겠지
            if len(stack) >= 2:
                n1 = stack.pop()
                n2 = stack.pop()
                result = int(n2) + int(n1)
                stack.append(result)
    print(switch)
    print(stack)
import sys

sys.stdin = open('../input1222.txt')

T = 10
for tc in range(1, T+1):
    num_length = input()
    data = input()

    stack = []
    switch = []
    #후위연산자로 바꿔줍니다. -> 이건 플러스만 있음
    for d in data:
        if d.isdigit():
            switch.append(d)
        else: #숫자가 아니라면 -> 연산자라면
            if not stack:
                stack.append(d) #스택이 비어있는 처음
            else:
                while stack: #연산자인데 값이 있다면
                    switch.append(stack.pop()) #팝한 것을 스위치에 넣고
                stack.append(d) #없으면

        # 남아 있는 연산자를 switch에 추가 -> 여러개 있을 수 있으니까
    while stack:
        switch.append(stack.pop())
    #print(stack) #원하는 것처럼 비어있습니다.
    #print(switch) #원하는 것처럼 채워있습니다.


    #후위 연산자를 기반으로 계산을 하겠습니다.
    for s in switch:
        if s.isdigit():
            stack.append(int(s))
        else: #연산자라면
            #근데 2이상 이어야 가능하겠지
            if len(stack) >= 2:
                n1 = stack.pop()
                n2 = stack.pop()
                result = int(n2) + int(n1)
                stack.append(result)
    print(switch)
    print(stack)
