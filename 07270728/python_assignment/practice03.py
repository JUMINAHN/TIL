# 지원 언니 코드
def is_user_data_valid(user_data): #dictionary type
    for key in user_data: #for 기본은 key --> key순회
        #isalpha는 문자열만 가능 --> 조건이 `비어있는 문자열?이라서?`
        #숫자로 아이디 값을 받으면 작동이 되지 않음
        #str 자체로 받으면 isalpha 역시 --> 숫자 == 문자타입
        if user_data[key].isalpha(): #해당 경우 숫자라면?
            return True
        else:
            return False
        
#dictionary 타입
id, pw = list(map(str, input().split())) #id, pw 입려하기
user_data = {id : pw}
result = is_user_data_valid(user_data)
print(result)