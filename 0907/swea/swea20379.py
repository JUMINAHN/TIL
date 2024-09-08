import sys
#회문처럼 접근

def change_stone(data):
    if data == 1:
        return 0
    else :
        return 1


sys.stdin = open('input20379.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #돌의수 N, 뒤집기 횟수 M
    stone = list(map(int, input().split())) #돌의 초기 상태

    #지금 -> 3번만 안돌아가는 중
    #view에서 풀었던 것처럼
    for _ in range(M):
        #사이에 둘 center번째 돌, 마주보는 face_to_face개의 돌
        center, face_to_face = map(int, input().split())
        center -= 1 #idx 잘보기
        for i in range(1, face_to_face+1): #범위를 초과할 수 있기 떄문에
            if 0<=center-i and center+i<N and stone[center-i] == stone[center+i]: #두개가 같다면
                stone[center - i] = change_stone(stone[center-i])
                stone[center + i] = change_stone(stone[center+i])
            # else :
            #     break #해당 되지 않으면 그냥 바로 break -> 그래도 그냥 하기 떄문에 break를 할필요가 없음
    print(f'#{tc}', end =' ')
    print(*stone)
    #print(stone)