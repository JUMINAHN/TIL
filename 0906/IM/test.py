def switch_btn(data): #data는 init[j]
    if data == 0:
        return 1
    elif data == 1:
        return 0
import sys
sys.stdin = open('input.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    switch = [0]+list(map(int, input().split())) #1 1 0 0 1
    init = [0] * len(switch) #스위치 번호가 1부터 시작하기 떄문에 switch 길이만큼

    #input받은 스위치를 기반으로 init 스위치 켜보기
    count = 0
    for i in range(1,N): #내부 한 줄을 순회해야 함
        #해당 되는 순번에
        ##1번 스위치 1의 배수, 2번 스위치 2의 배수 클릭
        #i만큼 이동하는거 아냐
        for j in range(i, N, i):
            if switch[j] != init[j]:  # 두개가 같지 않다면?
                init[j] = switch_btn(init[j])
        count += 19
    print(f'#{tc} {count}')
