# 10-11 보류
# +, -, ()로 식을 만들고 괄호를 지웠다
# 괄호를 적절히 쳐서 이식의 값을 최소로 만들려고 한다
# 식은 0~9, +, -로만 이루어져있따
# 두개이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다
# 수는 0으로 시작할 수 있따

#입력1번 -> 55 - (50+40)

#피연산자 연산자 피연산자 연산자 피연산자
# 그런데 모두 +일때는 상관이 없음
# 모두 -일떄도 상관이 없음

data = input() #뭔가를 받을 때
#어떻게 나눌 것인가?
#나누고 거기서 공백을 추가해서 split을 해보자
new_data = ''
for d in data:
    if d in ('-', '+') : #이걸 가지고 있다면
        new_data += f' {d} '
    else :
        new_data += d
#이걸 split
my_data = list(new_data.split())
print(my_data) #나옴
total = 0
# for my in my_data:
#     if my.isdigit():
#         total +=