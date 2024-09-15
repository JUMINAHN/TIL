import sys

sys.stdin = open('input1959.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = int(input().split()) #A,B
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))