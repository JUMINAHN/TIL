# import sys
# #쇠막대기 자르기
# sys.stdin = open('input5432.txt')
# #테스트 케이스 개수
# T = int(input())
# for tc in range(1, T+1):
#     stick = list(input()) #쇠막대기가 들어가있음
#     #print(stick)
#
#     #쇠막대기 자르기
#     #')'를 보면 빠져나오기
#     slicing = 0
#     stack = [] #stack에 담기
#     for s in stick:
#         if s == '(':
#             stack.append(s)
#         elif s == ')': #')'일때 한 번 더 추가적으로 더해줘야하는 것..
#             stack.pop() #일단 한 번 pop
#             if stack:
#                 slicing += len(stick) #stick에 값이 들어있는 만큼 추가해주고
#         #stack에 쌓인것이 지금 현재 쇠막대기
#