import sys

sys.stdin = open('input1215.txt')
#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    # 8 * 8의 글자판은 고정된 상태
    N = 8
    F = int(input()) #찾아야하는 회문의 길이
    arr = [list(input()) for _ in range(N)] #8만큼의 길이
    #arr을 하나씩 순회할 것

    #회문이 있는 곳을 카운트할 변수
    total_count = 0

    #행 먼저 순회한다.
    #여기서 주의해야할 점은 내가 찾는 수 만큼 순회를 해야한다는 것
    #전체 열을 다 도는게 중점이 아니라 내가 원하는 만큼 돌아야 함

        #자 0부터 4까지 돈다. 이게 row와 col에 적용이되면 먼저 0부터 4까지돌 것
        #row는 F에
    for row in range(N): #F만큼의 길이를 찾을 것 -> 일단 원하는만큼의 행은 다 돌아야 하기 떄문에
        #행 순회로 한 행의 모든 열을 비교할 것
        # 문제를 발견함 CBBC에서 -> CCCB 바로 다음 row를 찾아가는 문제가 발생함..
        for i in range(N - F + 1):  # N-F만큼 돌아야 내가 원하는 F의 길이에 도달할 수 있음
            find_row = []
            for col in range(i, i+F):
                find_row.append(arr[row][col])
            reverse_row = find_row[::-1] #findrow의 반대
            #결국 가운데를 갈라서 같은 것을 비교하나 전체를 비교하나 똑같다고 판단이 되기 떄문에 일단 전체비교
            if reverse_row == find_row:
                total_count += 1

    for row in range(N): #F만큼의 길이를 찾을 것 -> 일단 원하는만큼의 행은 다 돌아야 하기 떄문에
        #행 순회로 한 행의 모든 열을 비교할 것
        # 문제를 발견함 CBBC에서 -> CCCB 바로 다음 row를 찾아가는 문제가 발생함..
        for i in range(N - F + 1):  # N-F만큼 돌아야 내가 원하는 F의 길이에 도달할 수 있음
            find_row = []
            for col in range(i, i+F):
                find_row.append(arr[col][row])
            reverse_row = find_row[::-1] #findrow의 반대
            #결국 가운데를 갈라서 같은 것을 비교하나 전체를 비교하나 똑같다고 판단이 되기 떄문에 일단 전체비교
            if reverse_row == find_row:
                total_count += 1


    print(f'#{tc} {total_count}')