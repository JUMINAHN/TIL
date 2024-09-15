import sys

sys.stdin = open('input1231.txt')

def center(node): #root의 정점 노드
    if node == 0: #양 옆의 노드가 없을  경우
        return #빠져나간다.
    center(left[node]) #왼쪽 노드 확인 W -> F -> O -> S -> S에서 시작
    print(parent[node], end = '')
    center(right[node]) #오른쪽 노드 확인

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    #부모 배열 생성 == 문자열 data를 input 받기 위함
    parent = [' '] * (N+1) #금번에는 문자열을 사용하기 떄문에
    left = [0] * (N+1) #정점 노드 개수 + 1, 0이 포함되기 때문에
    right = [0] * (N+1)

    # 정점 기반으로 리스트 만들기
    #N번만큼 반복될 것 input되는 값이 1부터 N까지기 때문에
    for _ in range(N):
        arr = list(input().split()) #input받는 값들 == 1 W 2 3
        #왼쪽, 오른쪽 좌표가 있는 경우와 없는 경우를 구분하기 위해 len사용
        #1 W 2 3
        #4 O 8
        arrlen = len(arr)
        parent[int(arr[0])] = arr[1] #arr에 있는 0번쨰 idx가 parent가 원하는 idx이기 때문에
        #그리고 parent가 가지고 있어야하는게 data이기 때문에

        if arrlen >= 3: #왼쪽값에 대입
            left[int(arr[0])] = int(arr[2])
        if arrlen >= 4: #오른쪽값에 대입
            right[int(arr[0])] = int(arr[3])
        #원하는 값들 다 대입

    #기존 로직과 동일
    root = 1
    print(f'#{tc}', end = " ")
    center(root)
    print()