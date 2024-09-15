import sys
#10시부터~
sys.stdin = open('input10580.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    # 전봇대 두개
    # N개의 평평한 전선으로 연결됨
    # 교차하는 경우는 존재하나, 끝 점이 같은 경우는 없음
    # 3개 이상의 전선이 하나의 점에서 만나지 않음, 즉 교차하는 선은 두개로 제한됨
   # ----
    # <입력>
    # 1.TC
    # 2.전선의 개수N
    N = int(input()) #N개의 전선
    # 3. N개의 두 양의 정수 A/B가 주어짐 => A의 Xcm에 걸려있고, B의 Ycm에 걸려있음을 의미
    line = [] #전선을 담을 배열
    # 4. 모든 Ai는 다르고 모든 Bi도 다름 -> 즉 겹칠 수 없음
    for _ in range(N):
        a, b = map(int, input().split())
        line.append(a)
        line.append(b)
    min_n = min(line)
    max_n = max(line)
    #print(line)
    line = set(line)
    if len(line) < 2:
        print(f'#{tc} 0')
    else : #2보다 크다면s
        num = len(line) - 2
        print(f'#{tc} {num}')
    #-----
    #- 모든 경우를 탐색해야하는걸까
    #- 생각해보니 모든 전선의 개수는 주어진다.: 10시 26분에 깨닫, 알았는데 까먹었는데 다시 생각해보니 할 수 있는게 없음

    #>> 모르겠다.
    #> 혹시 모든 값을 input받아서 가장 작은곳부터 가장 낮은 곳까지 안에 있는 수들?(근데 만약 그게 한쪽에만 붙어 있다면..?
    #역시 접근법은 틀렸다..

    #list(map(list, zip(*arr)))
    #list(zip(*arr))