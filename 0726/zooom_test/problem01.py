#김싸피 전체 점수 중 최저점을 반환하는 min_score 함수를 완성
def min_score(humber_list):
    number_list.sort()
    return number_list[0]

number_list = list(map(int, input().split())) #list에 내용을 담습니다. -> 100 88 27 33 94 65를 담을 예정임
result = min_score(number_list)
print(result)