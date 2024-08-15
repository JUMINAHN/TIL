import sys
sys.stdin = open('input4836.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    #색종이가 놓여질 판의 크기
    #해당 문제는 원하는 부분만 색칠하면 되는 부분이기 때문에 전체 요소에 접근할 필요가 없음
    #또한 0부터 9인덱스까지 필요하기 떄문에 총 10칸을 생성하면 됨
    S = 10 # size로 나타낼 것
    arr = [[0]*S for _ in range(S)]
    N = int(input()) #색종이의 개수

    for _ in range(N): #색종이 개수만큼 굴리기
        r1, c1, r2, c2, color = map(int, input().split())
        #칸을 직접 그려보니 idx로 접근하는게 좋을 것으로 판단
        #r2+1을 한 이유는 4번 idx까지 칠하고 싶으나 접근이 불가하기 때문에 +1하는 것

        #들어가는 값이 이상함
        for row in range(r1, r2+1): #2, 3, 4
            for col in range(c1, c2+1): #2, 3, 4 -> print값을 다 찍어보기 오타로 인한 시간
                arr[row][col] += color
                #기존에 값이 있으면 += color로 다시 더해져야하는 것 아닌가?
        #print(arr)
   # print(arr)

    count = 0 #값이 3일 것을 count할 변수
    for row in range(S):
        for col in range(S):
            if arr[row][col] == 3:
                count += 1
    #현재 0으로 뜬다.
    print(f'#{tc} {count}')
