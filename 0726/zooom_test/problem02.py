#60점 미만인 과목의 개수를 계산하여 반환 under_60 함수
def under_60(subject):
    total = 0
    for sub in subject:
        if sub < 60:
            total += 1
    return total

subject = list(map(int, input().split())) #77 52 88 90 11 65 69 60 59 넣을 예정
result = under_60(subject) #받은 값 전달
print(result) #3개 예상