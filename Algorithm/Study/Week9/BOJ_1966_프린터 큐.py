#프린터 기기 == 명령을 받은 순서대로 : 먼저 요청된 것 먼저 인쇄
#queue의 가장 앞에 있는 문서의 중요도를 확인한다.
#나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있따면, 이 문서를 인쇄하지 않고 queue의 가장 뒤에 재배치
#중요도가 높은 순서대로 인쇄를 한다는 뜻 !!
#큐에 있는 문서의 수와 중요도가 주어졌을 떄 어떤 문서가 몇번째로 인쇄되는지 알아야 한다
from collections import deque
import sys

sys.stdin = open('input1966.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #M은 즉 idx위치
    N, M = map(int, input().split()) #문서의 개수N, 몇번쨰인지 궁금한 정수 M == 찾고자하는 값의 M
    #문서의 중요도가 순서대로
    important = deque(map(int, input().split())) #1, 2, 3, 4
    #원형 큐를 사용하면 될 것 같은데,,
    #큐의 크기가 가장 큰 것에서 시작하고 그 것의 인덱스를 찾으면 될 것 같다
    #그리고 그 다음 큰 것을 찾는다 == 그러려면 앞의 제일 큰 것을 pop해주고 count를 해준다.
    #print(important)
    for i in range(N): #문서의 개수
        if important[i] == max(important) : #가장 큰 값일 때
            important.popleft() #해주고
        else : #그게 아니라면
            important.append(important.popleft()) #다시 값을 추가해준다.
    #흠 .. 아이디어만 있다.
    #출력은 idx와 다르게 1부터 시작함