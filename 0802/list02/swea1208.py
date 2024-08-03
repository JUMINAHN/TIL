import sys

#ys.stdin = open('input1208.txt')

T = 10
for tc in range(1, T+1):
    dump_count = int(input()) #덤프횟수
    box_height = list(map(int, input().split())) #입력으로 들어오는 값
    #버블 정렬 or 선택정렬 가능 --> 인덱스 자체를 구하는게 아니기 때문에 전반적으로 솔트해보자

    #선택 정렬 -> 가로길이는 항상 100으로 주어진다. --> index가 기준
    for i in range(100 - 1): #0부터 99까지
        min_idx = i #제일 작은 값으로 가정
        for j in range(i+1, 100):
            if box_height[min_idx] > box_height[j]:
                min_idx = j
        box_height[min_idx], box_height[i] = box_height[i], box_height[min_idx]
    print(box_height)