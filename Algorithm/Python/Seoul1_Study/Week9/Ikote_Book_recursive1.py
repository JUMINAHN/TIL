#재귀 함수란 자기 자신을 다시 호출하는 함수
#재귀 함수는 종료 조건을 꼭 명시해야 한다. == 명시하지 않으면 함수가 무한 호출 됨
#재귀 함수의 수행은 스택 구조 활용

#하기는 재귀함수를 이해할 수 있는 가장 쉬운 코드
def recursive_fucntion(i):
    #100번째 출력값에는 종료되도록 종료 조건을 명시한다.
    if i == 100:
        return #break가 아니라 return, 왜냐하면 함수니까
    print(i, '번쨰 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    i += 1
    recursive_fucntion(i) #입력값이 지속해서 증가함
    ##하기 값은 나오지 않음 왜냐하면 계속해서 recursive_function이 호출되고 있기 떄문에
    print(i, '번쨰에서 종료합니다')

recursive_fucntion(1)