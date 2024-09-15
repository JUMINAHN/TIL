import sys

sys.stdin = open('input2605.txt')
N = int(input())
arr = []
select = list(map(int, input().split()))

for stu_idx, s in enumerate(select):
    arr.insert(len(arr) - s, stu_idx+1) #뽑은 번호를 -> idx, 현 idx는 학생
#arr_reverse = arr[::-1] #될까?
print(*arr)