# import sys
#
# sys.stdin = open('input1208.txt')
# #테스트 케이스 개수
# T = 10
# for tc in range(1, T+1):
#     dump = int(input())
#     height = list(map(int, input().split()))
#     #가장 높은 곳, 가장 낮은 곳의 차이 출력
#     #min_height = 0 #가장 낮은 곳의 idx -> 값은? 일단 보류
#     #max_height = 0 #가장 높은 곳의 idx
#     #값을 담는게 아니라 가장 낮은 곳일 경우 그 값을 하나 감소 시키고, 가장 큰 곳일 경우 그 값을 증가시킨다.
#     #이걸 덤프만큼 진행한다.
#     count = 0
#     while count == dump:
#         min_height = 0
#         max_height = 0
#         for i in range(len(height)):
#             if height[min_height] > height[i]:
#                 min_height = i
#             if height[max_height] < height[i]:
#                 max_height = i
#         height[min_height] += 1 #값을 올려준다.
#         height[max_height] -= 1 #값을 감소시켜준다.
#         count += 1
#     #이건 sort를 안하고 일단 생각나는데로
#     #결론적으로 가장 작은 것은?
#     min_height = max_height = 0
#     for i in range(len(height)):
#         if height[min_height] > height[i]:
#             min_height = i
#         if height[max_height] < height[i]:
#             max_height = i
#     print(f'#{tc} {height[max_height] - height[min_height]}')
