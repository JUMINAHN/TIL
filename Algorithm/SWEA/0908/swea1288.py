import sys

sys.stdin = open('input1288.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #N의 배수의 양을 세기시작했다
    #K번 양을 센다
    #0~9까지 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점인가?
    #최소 몇번 양을 센시점 * N
    N = input()#모두 하나씩 조합해야 하기 떄문에

    data = []
    #몇 번 셀지 모름
    first_num = int(N)
    count = 0
    while len(set(data)) != 10: #10일떄
        word = str(N)
        for w in word:
            data.append(w)
        #print(set(data))
        count += 1 #이떄 세게 된다.
        if len(set(data)) == 10:
            break
        N = int(N)
        N += first_num #N의 배수만큼 증가 됨
    print(f'#{tc} {count * first_num}')