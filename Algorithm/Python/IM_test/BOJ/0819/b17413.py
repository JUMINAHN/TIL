import sys

#태그 자체는 변동이 없음
#split한 것 내용 기반으로

sys.stdin = open('input17413.txt')
#테스트 케이스 개수
T = 1

# 단순 뒤집기
for tc in range(1, T+1):
    str_list = list(input().split()) #baekjoon online
    for i in range(len(str_list)):
        result = str_list[i] #beakjoon  ///  oneline  ///  judge
        result = result[::-1]
        print(result, end = " ")