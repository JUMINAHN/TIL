import sys

sys.stdin = open('../input1231.txt')

def center(node): #root의 정점 노드
    if node == 0:
        return
    center(int(left[node]))
    print(node, end = ' ')
    center(int(right[node]))

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    parent = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    infos = [0, parent, left, right]

    for _ in range(N) : #N번만큼 순회
        info = list(input().split()) #받는 것을 기준으로 split
        for i in range(1, len(info)): #1부터 info 개수 만큼
            infos[i][int(info[0])] = info[i]
    print(f'#{tc}', end = " ")
    root = 1
    center(root)
    print()
