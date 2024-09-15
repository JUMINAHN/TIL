# 3개의 숫자 중 2개를 선택하는 모든 경우의 수를 찾는 예제
numbers = [1, 2, 3]

#중복된 숫자를 모두 보여준다.
# for n1 in numbers:
#     for n2 in numbers:
#         print(n1, n2)

#i + 1부터 시작하는 두 번째 루프는 이미 선택한 요소를 다시 선택하지 않도록
for i in range(len(numbers)) : #numbers의 개수만큼 순회
    #모든 idx 를 순회 -> 마지막 요소도 첫번쨰 선택항목이 될 수 있어야 함
    for j in range(i+1, len(numbers)): #두 번째 루프의 조건(i + 1)을 통해 자연스럽게 중복을 피하고 필요한 조합만을 생성
        #중복과 불필요한 조합 제외를 위해 i+1을 해준다.
        #i가 마지막 인덱스일 때 range(i + 1, len(numbers))는 빈 범위가 되어 루프가 실행되지 않음음
            #numbers = [1, 2, 3]인 경우:
            #i = 0일 때: j는 1, 2를 순회 (1,2 1,3 출력) --> 중복적으로 1은 포함하지 않음
            #i = 1일 때: j는 2만 순회 (2,3 출력)
            #i = 2일 때: j는 순회하지 않음 (아무것도 출력하지 않음)
        print(numbers[i], numbers[j])