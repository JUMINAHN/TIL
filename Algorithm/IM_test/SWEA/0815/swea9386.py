import sys

sys.stdin = open('input9386.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #수얄의 길이
    #0과 1로 구성된 수열
    num_list = list(map(int, input()))
    #print(num_list)
    #연속한 1의 개수를 구해야 함
    #이를 위해서 최대값을 담을 변수 생성
    max_num = 0
    #1이 있는지 확인하기 위한 조건문과, for문 생성
    #N을 활용하지 않고 일단 생성
    count = 0 #1의 개수를 counting할 변수 생성
    for num in num_list:
        if num == 1:
            count += 1 #1의 개수 counting
        else :
            if max_num < count:  # 비효율적인 count 낭비를 위해서 0으로 초기화되기전에 누적된 count를 담는다.
                max_num = count
            count = 0
    #마지막으로 1이 남아있을 떄를 고려해서 한 번 더 지금의 max값과 count값을 비교한다.
    if max_num < count:
        max_num = count
    #따라서 내가 원하는 불필요한 반복을 더 최소화하고 한 번 더 진행할 수 있다.

    print(f'#{tc} {max_num}')
