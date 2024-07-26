#신규 생성 아이디의 마지막 글자는 반드시 0부터 9사이에 숫자로 끝나야 한다
#user_data가 python의 dictionary로 들어올 때, 사용자가 입력한 아이디어 위 조건을 만족하면 T, 아니면 F
def is_id_valid(user_data):
    if user_data.get(id)[-1] in [f'{i}' for i in range(0,10)]:
        print(True)
    else :
        print(False)

#내가 이해한 것은 dictionary에 키가 id고 값이 입력한 숫자
user_data = {id : input()}
is_id_valid(user_data)