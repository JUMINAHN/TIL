#슬라이싱, 회문
import sys

def find_reverse(N, K, arr):
    # 행 탐색
    total = 0  # 같으면 회문 카운트
    for row in range(N):
        # 그림을 보았을 떄 모든 행을 돌아야한다고 판단됨
        for i in range(0, N - K + 1):  # 행에 영향을 받지 않음 -> 자체적으로 돌아갈 것
            # 그런데 열이 원하는 크기만큼 돌고, 변동되어야 하기 때문에 이를 받침해줄 주춧돌 i를 선언해야함
            # 이 i는 열에 K만큼 돌것이기 때문에 범위를 초과하지 않도록 장치를 만들어 줘야함 N-K+1 이런식으로
            # 여기를 확인해주어야 겠지? -> col자체를 돌기 떄문에!!!
            data = []
            for col in range(i, i + K):
                data.append(arr[row][col])  # col의 범위만큼 append 해주고
            # 다만, 열은 원하는 크기만큼 돌아야 함 0~K만큼 -> 1부터 ~ K+1만큼
            # 즉 변동되는 것을 볼 수 있음 -> 변수 i로 선언
            if data == data[::-1]:  # 뒤집은것과 나의 data가 같은지 비교
                total += 1
    return  total

sys.stdin = open('input1215.txt')
#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    N = 8
    K = int(input()) #찾을 범위
    arr = [input() for _ in range(N)]
    #print(arr)

    # 행, 열을 탐색해야함 -> 전치행렬을 사용해서 행만 점검해도 유용
    #행 total 값
    row_total = find_reverse(N, K ,arr) #일반 행
    #열 total 값
    #전치 행렬을 해보자
    col_arr = list(map(list, zip(*arr))) #맞는 것 같고 -> 전치 행렬 사용
    col_total = find_reverse(N, K, col_arr)
    print(f'#{tc} {row_total + col_total}')

#    print(col_arr)


