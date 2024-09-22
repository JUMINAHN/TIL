#재귀함수로 팩토리얼 접근하기
#5*4*3*2*1 사용하기
def recursive_function(i):
    if i <= 1:
        return 1 #팩토리얼의 마지막 * 1을 할 것
    print('현재 i =', i)
    return i * recursive_function(i-1) #이 뜻은 5*4*3*2*1
print('재귀로 구현', recursive_function(5))

'''
recursive_function(5) 호출
recursive_function(4) 호출
recursive_function(3) 호출
recursive_function(2) 호출
recursive_function(1) 호출 (종료 조건 도달)
'''