data = {}
data['과목'] = 'Python'
data['구분'] = '실습'
data['단계'] = 2
data['문제번호'] = 3251
data['이름'] = None
data['일차'] = 22
print(data)

#원본의 값을 문자열로 형변환하고, 단계문자열을 덧셈하여 할당한다
data['단계'] = str(data['단계']) + '단계'
title = '딕셔너리 활용하기'
data['이름'] = title
data['일차'] = data['일차'] - 20 #복합연산자?
print(data)