#변수를 사용하지 않고, 정수와 연산자만을 사용해서 요구사항 충족하는 표현식
#그 후에 변수를 사용해서 요구사항을 충족하도록 표현식

result_1 = 3*2
result_2 = 3**2
result_3_1, result_3_2 = (3**2 //2, 3**2 % 2)
result_4 = 3**2 + (-3**2)  #0이 될듯 --> 왜냐면 제곱 연산자가 우선임
print(result_1)
print(result_2)
print(result_3_1, result_3_2)
print(result_4)