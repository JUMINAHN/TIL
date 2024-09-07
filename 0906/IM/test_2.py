#스위치 LED번호는 1부터 시작
#1번 스위치 1의 배수, 2번 스위치 2의 배수 클릭
#꺼져있으면 0, 켜져있으면 1
#LED 패턴 입력 받고, 꺼져있는 LED에서 입력받은 패턴의 LED 만들려면 최소 몇번 스위치 --> `꺼져있는` 기본이 00000
import sys

def switch_btn(data): #data는 init[j]
    if data == 0:
        return 1
    elif data == 1:
        return 0

sys.stdin = open('input.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    switch = [0]+list(map(int, input().split())) #1 1 0 0 1
    init = [0] * len(switch) #스위치 번호가 1부터 시작하기 떄문에 switch 길이만큼

    #input받은 스위치를 기반으로 init 스위치 켜보기
    count = 0
    for i in range(1,len(switch)): #내부 한 줄을 순회해야 함
        if switch[i] != init[i]:
            #조건이 성립되야 스위치를 켜
            for j in range(i, len(switch), i):
                init[j] = switch_btn(init[j])
                #print(init)
            count += 1
    #       = else :
    #           count += 1  # 스위치를 켰으니까 도는거겠지 -> 같지 않으니까
    print(f'#{tc} {count}')
