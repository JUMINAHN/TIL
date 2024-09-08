import sys
#
# def change(data):
#     if data == 1:
#         return 0
#     else :
#         return 1

sys.stdin = open('input1289.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #메모리 초기화
    #원래 값알고 있음 -> 0인지 1인지 설정하면 메모리의 끝까지 덮어씌워짐
    #스위치처럼 바꾸는게 아니라 쭉 덮어 씌워짐
    #현재는 초기화상태 000
    init = list(map(int, input()))
    N = len(init)
    now = [0] * N
    fix = 0 #몇번 고쳐야하는 가?

    # print(init)
    # print(now)
    for i in range(0, N): #확인하면 되는 값
        if init[i] == now[i]: #위치가 같으면 skip -> 왜 안돼?
            #print('before', now)
            continue
        else:#그게 아니라면 고쳐
            diff = init[i] #init i의 숫자로 다 바꿔버려 -> 그냥 이전값
            fix += 1
            for j in range(i, N): #여기서부터 N번만큼 순회 => j만큼 다 바꿔주는 것 아닌가
                now[j] = diff
            #print('after', now)

    print(f'#{tc} {fix}')