def recursive_function(i):
    if i == 100:
        return # 재귀함수 종료
    print(i, '번째 index는', i+1, '을 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 function이 종료됩니다.')

recursive_function(1)