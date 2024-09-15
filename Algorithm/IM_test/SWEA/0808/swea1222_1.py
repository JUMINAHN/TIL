import sys

sys.stdin = open('input1222.txt')

#Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    data_len = int(input())
    data = list(map(str, input())) #9+8+5+9+2+4+1+8+3+9+ etc..


    stack = []
    result = [] #숫자 출력
    #후위 표기식으로 바꾸어 계산
    #데이터를 넣었을 때 진행되는 것
    for i in range(data_len):
        if data[i].isdigit():
            result.append(data[i]) #숫자 출력
        else:
            stack.append(data[i]) #stack에 기호 쌓기
            if data[i] == '+':
                result.append(stack.pop()) #스택 pop하고--> 출력에 넣음
                stack.append(data[i]) #스택에 +을 넣는다.
    #이제 데이터를 돌지 않고 남아 있는 것 pop -> 항상 데이터를 돌고 stack에는 결과 잔여물이 남을 수 밖에 없다.
    while stack:
        stack.pop() # 이부분 확인 필요
    print(stack)
    print(result) #출력값이 담겨있음

    for i in range(len(result)):
        if data[i].isdigit():
            stack.append(result[i])
        else:
            if data[i] == '+':

        if len(stack) < 2: #일단 총 4번

        elif len(stack) >=2 :
            num1 = stack.pop()
            num2 = stack.pop()
        else: #연산자면

    # for i in range(len(result)-1, -1, -1):
    #     if result[i].isdigit():
    #         stack.append(result[i]) #스택을 추가하고
    #     else:
    #         if len(result) >= 2:
    #             if result[i] == '+':
    #                 n1 = result.pop()
    #                 n2 = result.pop()
    #                 stack.append(int(n1) + int(n2))
    #         #연산자는 계속 출력이 되어야 함
    #         #pop을 해야 함


    #print(stack)
    #print(result)
    #이를 기반으로 연산자 수행 -> result를 stack에 하나씩 넣는다.
    # for i in range(len(result)):
    #     if i == 0:
    #         stack.append(result.pop())
    #     stack.append(result.pop())
    #     if stack()



        #
        # else : #+면 -> 출력
        #     if len(stack) >= 2:
        #         if data[i] == '+':
        #             n1 = stack.pop()
        #             n2 = stack.pop()
        #             stack.append(n1 + n2)
    print(stack)