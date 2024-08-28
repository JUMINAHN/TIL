#8:49

import sys
# 8 + 9 + 10 + 11 + 12
# 그런데 10이 넘어가면 1과 0, 1과 1, 1과 2로 나누어 계산한다
sys.stdin = open('input5604.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    arr = []
    for i in range(A, B + 1):
        if i >= 10: #10보다 클 때
            str_num = str(i) # str_num으로 바꾸고
            #str_num을 모두 순회_문자열 속성 이용하기
            for s in str_num:
                arr.append(s)
        else :
            arr.append(str(i))
    #애초에 input을 받고 그 안에서 len이 2이상 이면 split을 해서 하나씩 넣는 것으로?
    #근데 애초에 숫자/문자 자체가 덩어리 하나라서 split을 할 수 있는가? pop을 할 수 있는가..?
    #일단 이걸 기반으로 split 받는게 목표
    # #idx 하나씩 접근
    # for i in range(len(arr)):
    #     if int(arr[i]) >= 10:
    #         str_num = str(arr[i]) #문자열로 변환하고
    #         #하나씩 순회
    #         for s in str_num:
    #             arr.append(s)
    #         #모두 다 append했다면 a 삭제
    #         arr.remove(arr[i])

    #print(arr) 모두 나왔음을 확인한다면 int로 변환해서 total을 센다
    total = 0
    for a in arr:
        total += int(a)
    print(f'#{tc} ', end = "")
    print(total)
