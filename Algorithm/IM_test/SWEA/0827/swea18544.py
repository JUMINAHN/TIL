import sys

sys.stdin = open('input18544.txt')

def preorder(node):
    if node == 0:
        return
    print(node, end=' ')
    preorder(left[node])
    preorder(right[node])

N = int(input())
arr = list(map(int, input().split()))
right = [0] * (N+1)
left = [0] * (N+1)
for i in range(0, len(arr), 2): #노드 만들기
    parent, child = arr[i], arr[i+1]
    if left[parent] == 0:
        left[parent] = child
    else :
        right[parent] = child
#이걸 기반으로 이제 전위 순회
root = 1
preorder(root)