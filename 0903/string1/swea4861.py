import sys
#회문
sys.stdin = open('input4861.txt')
#테스트 케이스 개수
#길이가 M인 회문의 길이를 찾는다.
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #배열의 크기 N, 길이가 M인 회문 찾기
    arr = [list(input()) for _ in range(N)]
    #열 행 순회하면서 길이가 M인 회문을 찾기

    #길이가 M인 것만큼을 찾아야하기 떄문에
    #행 순회하기
    result = '' #배열 자체가 들어가게 됨
    for j in range(0, N-M+1):#0부터 13까지
        for row in range(j, M+j):
            for i in range(0, N - M + 1):  # 0부터 7까지
                data = []
                for col in range(i, M+i): #0부터 13까지 -> 그리고 증가시키는거임 1부터 14까지 2부터 15까지
                    data.append(arr[row][col])
                    reverse_data = data[::-1] #역순으로 뒤집은 것
                if data == reverse_data: #test case를 보고 알았다.
                    result = data
    #스도쿠, 파리퇴치를 생각하면 됨

    #열 순회하기
    result2 = '' #배열 자체가 들어가게
    for j in range(0, N-M+1):#0부터 13까지
        for col in range(j, M+j):
            for i in range(0, N - M + 1):  # 0부터 7까지
                data = []
                for row in range(i, M+i): #0부터 13까지 -> 그리고 증가시키는거임 1부터 14까지 2부터 15까지
                    data.append(arr[row][col])
                    reverse_data = data[::-1] #역순으로 뒤집은 것
                if data == reverse_data:
                    result2 = data
    if result :
        print(f'#{tc} {"".join(map(str, result))}')
    elif result2:
        print(f'#{tc} {"".join(map(str, result2))}')


#    print(result)