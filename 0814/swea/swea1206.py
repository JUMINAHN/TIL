import sys

sys.stdin = open('input1206.txt')
#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    N = int(input()) #건물의 개수
    height = list(map(int, input().split())) #맨왼쪽, 맨오른쪽 높이 항상 0

    zomang = 5
    total = 0
    for i in range(N-zomang): #돌려보고 안되면 점검해보기
        height_list = height[i:i+zomang] #0부터 5인덱스
        #여기에 대한 정렬을 실시해서 맨뒤에것들 pop하기
        #선택정렬실시 -> idx 기반 접근
        #print(height_list)

        k = 0
        for j in range(len(height_list)-1): #변수명 설정 조심
            min_idx = j
            for j in range(i+1, len(height_list)):
                if height_list[min_idx] > height_list[k]:
                    min_idx = k
            height_list[i], height_list[min_idx] = height_list[min_idx] + height_list[i]
        #정렬을 기반으로 제일 큰것과 두번쨰 큰 값 비교
        print(height_list)
        # max_1 = height_list.pop()
        # max_2 = height_list.pop()
        # total += (max_1 - max_2)
    print(f'#{tc} {total}')


