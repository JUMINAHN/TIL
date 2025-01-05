import sys

sys.stdin = open('input1222.txt')

#Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    data_len = int(input())
    data = list(map(str, input())) #9+8+5+9+2+4+1+8+3+9+ etc..

    stack = []
    for i in range(len(data)):
        if data[i].isdigit(): #이거 마지막에 append만 됨
            if i == len(data)  :
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1+n2) #stack에 9넣고


        else : #+면 -> 출력
            if len(stack) >= 2:
                if data[i] == '+':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n1 + n2)
    print(stack)