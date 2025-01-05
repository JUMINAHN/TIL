import sys

sys.stdin = open('input1288.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = input() #data를 입력받음
    arr = []
    for i in N: #입력받은 데이터를 arr에 넣어준다.
        arr.append(i)
    #입력받은 데이터 끝

    #반복될 행위들
    #먼저 도달횟수를 셀 변수 설정 == count
    count = 1
    one_bon = int(N)
    #idx = 1 #첫번째 이후 두번째부터 while돌것이니까 -> 그래서 그냥 1로
    while len(set(arr)) != 10: #0부터 9까지니까 총 10이 될 때 까지 순회
        N = int(N) #N으로 바꿔주고
        N += one_bon #배수 #나 자체가 증가하니까 나를 계속 더해주자
        #이것을 다시 문자로 변환해서 넣어주는 것
        N = str(N)
        for i in N:
            arr.append(i)
        count += 1 #count도 증가하고
        #idx += 1 #index도 배수를 증가시킨다. -> idx는 증가시킬 필요가 없음 N자체가 증가하니까
        #print(N)
    #이상하게 풀었다
    print(f'#{tc} {count*one_bon}')