import sys

sys.stdin = open('input1926.txt')

# Testcase 수
#T = int(input())
# Testcase 만큼 반복
#for tc in range(1, T+1):
N = int(input())
for i in range(1, N+1):
    i = str(i)
    if ('3' in i) or ('6' in i) or ('9' in i):
        if '3' in i:
            a = i.count('3')
            #print(a)
            print('-'*a, end='')
        if '6' in i :
            b = i.count('6')
            print('-'*b, end='')
        if '9' in i :
            c = i.count('9')
            print('-'*c, end= '')
        print("", end=' ')
    else:
        print(i, end= ' ')
# for i in range(1, N+1):
#     if i in (3,6,9) :
#         print('-', end =' ')
#     else :
#         print(i, end =' ')