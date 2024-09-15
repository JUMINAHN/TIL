import sys

sys.stdin = open('input1231.txt')

def center(node): #root의 정점 노드
    if node == 0:
        return
    center(left[node])
    print(node, end = ' ')
    center(right[node])


# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    parent = [' '] * (N+1)
    right = [0] * (N+1)
    left = [0] * (N+1)
    # 정점 기반으로 리스트 만들기
    for i in range(1, N): #0번 노드는 사용하지 않기 떄문에 기존 노드 기반으로 확인
        arr = list(input().split()) #구분하지 않은 것
        new_arr =  []#int 구분 가능한 것
        #parent = parent_data = child_l = child_r = 0
        for a in arr:
            if a.isdecimal():
                new_arr.append(int(a))
            else :
                new_arr.append(a)
        p, data, child_l, child_r = arr #근데 이게 없는 경우도 존재..
        parent[i] = data #parent에 data 넣고 #parent[i] = data #parent에 data 넣고

        if right[i] == 0:
            right[i] = child_r
        else :
            right[i] = child_l

    root = 1
    center(root)
