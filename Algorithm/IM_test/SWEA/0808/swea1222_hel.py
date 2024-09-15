import sys

sys.stdin = open('input1222.txt')

#Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    data_len = int(input())
    data = list(map(str, input())) #9+8+5+9+2+4+1+8+3+9+ etc..

    stack = []
    for d in data:
        if d.isdigit():
            stack.append(int(d)) #stack에 9넣고
        else : #+면 -> 출력
            if len(stack) >= 2:
                if d == '+':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n1 + n2)
    print(stack)