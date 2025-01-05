import sys

sys.stdin = open('input1208.txt')
#최대, 최소는 sort를 사용하면 더 쉽게 구분하고, 판별할 수 있다. -> 단순 loop를 살리는게 문제가 아닐 수 있다.
#단순 배열에 값이 들어있는 경우 최대 최소의 비교는 sort를 통해 할 수 있다.
def my_sort(height): #선택 정렬
    N = len(height)
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if height[min_idx] > height[j]:
                min_idx = j
        height[min_idx], height[i] = height[i], height[min_idx]
    #그냥 단순 정렬을 시켜준다. -> 선택 정렬 실시

#테스트 케이스 개수
T = 10
for tc in range(1, T+1):
    dump = int(input())
    height = list(map(int, input().split()))
    #print(height) : 정렬된 것을 확인할 수 있음
    #일단 지금 input받은 것을 정렬하면 최대, 최소를 구할 수 있음 : 정렬은 최대/최소를 쉽게 정렬할 수 있게 만들어줌 !! -> keypoint
    my_sort(height) #정렬하고 -> 왜냐면 정렬을 먼저하고
    #dump만큼 반복할 것
    for _ in range(dump): #dump만큼 반복
        height[0] += 1 #최소 #셈을 해준 다음에
        height[-1] -= 1 #최대
        my_sort(height)  # 정렬하고 또 정렬을 한다.
    #순서대로 정렬 -> 셈 -> 정렬 -> 셈
    #함수에서 정렬을 했으니까 최종적으로 print에서 셈을 해준다.
    #print(height)
    #여기서 최고 최저 차이 뺴준다.
    print(f'#{tc} {height[-1] - height[0]}')