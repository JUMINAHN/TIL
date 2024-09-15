import sys

sys.stdin = open('input4865.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복

for tc in range(1, T+1):
    alpha = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0
             , 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    str1 = input() #key값
    str2 = input() #탐색할 것
    #일단 str2 자체를 모두 탐색해서 ,count를하고,
    #str1자체에사 순회해서 가장 max인 것 추출
    for s2 in str2:
        num = alpha.get(s2)
        num += 1 #num += 1
                    #TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int' -> 값이 없는 것은 int와 비교불가
        alpha[s2] = num

    max_num = 0
    for s1 in str1:
        num = alpha.get(s1)
        if max_num < num:
            max_num = num
    print(f'#{tc} {max_num}')

    # for s2 in str2:
    #     if s2 in str1:
    #         num = alpha.get(s2)
    #         num += 1 #TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'
    #         alpha[s2] = num
    #print(alpha)