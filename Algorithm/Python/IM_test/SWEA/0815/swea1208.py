import sys

sys.stdin = open('input1208.txt')
#테스트 케이스 개수

#num_list를 sort해줄 것
def num_sort(num_list, row):
    #선택 정렬 사용_idx 접근
    for i in range(row - 1):
        min_idx = i
        for j in range(i+1, row):
            if num_list[min_idx] > num_list[j]:
                min_idx = j
        num_list[min_idx], num_list[i] = num_list[i], num_list[min_idx]
    return num_list


T = 10
for tc in range(1, T+1):
    #최고, 최저 간격 구하기
    #row는 항상 100으로 존재
    dump = int(input()) #평탄화 횟수
    row = 100
    num_list = list(map(int, input().split())) #100개의 상자 예상
    #정렬을 해줄 것이다.
    #덤프를 하고 매번 정렬을 수행해야 한다.
    for _ in range(dump):
        num_list = num_sort(num_list, row) #넣고 빼고의 단점.. #sort를 하니까
        num_list[-1] -=1
        num_list[0] +=1
        #마지막에는 sort가 되지 않는다.
    #그래서 다시 한 번 더 sort를 해줘야함 마지막에는 값만 뺀게 됨
    num_list = num_sort(num_list, row)
    #상자를 sort해야하고, 주기적으로 sort해서 가장 큰값과 낮은 값을 구해야함
    #현재의 numlist가 반환될 것
    print(f'#{tc} {num_list[-1] - num_list[0]}')

