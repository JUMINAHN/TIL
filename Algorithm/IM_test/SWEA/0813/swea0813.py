#1.
import sys

sys.stdin = open('input0813.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    tc_num = int(input())
    arr = list(map(int, input().split()))
    #pw와 동일한 idx를 만들어야 함
    pw_length = 8  #길이를 정하고
    pw = [0] * pw_length  #미리 size를 만들어 놓는다. #8개가 들어갈 것
    #print(pw)

    #front, rear로 접근하기 --> 현재의 front, rear의 위치는?
    front = 0 #가장 먼저 빠질 것
    rear = 7 #마지막 더 이상 뭔가 넣을 수 없는 것

    #0이 될 떄 까지
    flag = 1
    # 1에서 5까지 감소시키는 반복문
    while flag:
        for i in range(1, 6):
            arr[front] -= i
            # 각 front, rear값

            front = (front + 1) % len(arr)
            rear = (rear + 1) % len(arr)
            # 만약 arr[rear] 값이 0 이하 -> 0으로 지정하고 종료
            # arr[rear] 값이 0이 되면 종료
            if arr[rear] <= 0 :
                arr[rear] = 0
                flag = 0
                break
    print(front)
    print(rear)
    print(arr)
    #arr이 마지막이 될 때 까지
    # 정렬해주기 -> 현재 arr[rear]값이 0이기 때문에 arr[front] 가 1번 부터 정렬되도록

    for k in range(pw_length):
        #front를 맨마지막으로 보낸다.
        idx = (front + k) % pw_length #하나씩 밀어줘야하기 때문
        pw[k] = arr[idx] #pw list하나에 미룬 idx를 담아주면 됨
    print(f'#{tc_num}', *pw)  ##1 6 2 2 9 4 1 3 0